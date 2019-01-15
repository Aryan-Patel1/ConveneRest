from django.shortcuts import render
from survey.models import Survey,Block,Question,Choice,JsonAnswer
from userroles.models import UserRoles
from beneficiary.models import Beneficiary,BeneficiaryType
from facilities.models import Facility
from masterdata.models import Boundary
from django.contrib.contenttypes.models import ContentType
from rest_framework.views import APIView
from rest_framework.response import Response
from .ReportManager import *
from survey.views.survey_views import  get_user_partner_list
from MutantApp.models import *
from django.apps import apps
from math import ceil
from masterdata.views import CustomPagination
from common_methods import *

# Create your views here.

kwargs = {'survey_id':48,
          'question_ids':[250,253],
          }

{ 'survey_id':48,
  'question_ids':[250,253],
  'cluster_type':'beneficiary',
  'cluster_id':123
}
def get_survey_info(*args,**kwargs):
    answers = JsonAnswer.objects.filter(active=2,survey__id=kwargs.get('survey_id'),
                cluster__0__beneficiary__id=kwargs.get('cluster_id'))
    answer_resp = {}
    for i in answers:

        for q in Question.objects.filter(id__in=kwargs.get('question_ids')).order_by('code'):
            if q.qtype in ['S','C','R']:

                choice = Choice.objects.get_or_none(id=i.response.get(str(q.id)))
                answer_resp[str(q.id)] = str(choice.text) if choice else " "
            else:
                answer_resp[str(q.id)]=i.response.get(str(q.id))
    return answer_resp
    #return 0

{'model':'beneficiary',
 'model_filter_value':'4',
 'model_field_filter':'beneficiary_type_id',
 'required_fields':['boundary_id','partner','age','gender','name','address'],
 'boundary_levels':[3,4],
 'boundary_helper':{3:'District',4:'Block',7:'Village'},
 'model_filter':{''}
 }

def get_cluster_info(*args,**kwargs):
    try:
        ct = ContentType.objects.get(model=kwargs.get('model'))
        print ct
        field_values = ct.model_class().objects.filter(**{kwargs.get('model_field_filter'):
        kwargs.get('model_filter_value')}).custom_values(kwargs.get('required_fields'))
        for value in field_values:
            b_id = eval(value.get('address')[0]).get('address_0').get('boundary_id')
            boundary_parent={}
            [boundary_parent.update(i) for i in Boundary.objects.get(id=b_id).get_parent_locations([])]
            value['Village']=Boundary.objects.get(id=b_id).name
            for i in kwargs.get('boundary_levels'):
                value[kwargs.get('boundary_helper').get(i)]=boundary_parent.get('level'+str(i)+'_id')
            value.update(get_survey_info(**{'survey_id':48,
          'question_ids':[250,253],'cluster_id':value.get('id')}))
            print value
        return field_values
    except Exception as e:
        return e.message


class GetReportDisplay(APIView):
    def get(self,request,id,uid):
        p_list = get_user_partner_list(uid)
        print p_list
        rm = ReportManager()
        data = rm.display_report(id,p_list)
        return Response(data)

class GetReportConfigured(APIView):
    def get(self,request):
        data = AggregateReportConfig.objects.filter(active=2).values('id','report_name')
        return Response({'status':2,'data':data})

class ExportReport(APIView):
    def get(self,request,id,uid):
        p_list = get_user_partner_list(uid)
        res = ReportManager().export_report(id,p_list,request)
        return Response(res)
        
class MutantReportView(APIView):
    def get(self, request):
        dict_table = {"NE":"never_enrolled_dropped_out", "DO":"dropped_out", "NEA":"ece_non_enrollment", "IC":"irregular_child_quarter", "EC":"child_involved_economic_activity", "BR":"birth_reg_yet_to_be_done", "CE":"child_engaged_or_married", "MC":"list_of_missing_child", "MGC":"list_of_migrated_child", "HPW":"health_pregnant_women","HCS":"health_centre_survey_1","SLI":"school_level_information_2","ACI":"anganwadi_centre_information_3","LM":"lactating_mothers_60","GM":"growth_monitoring_47","CVI":"child_vaccination_and_immuniza_49","PW":"pregnant_women_57"}
        model = apps.get_model('MutantApp', dict_table.get(request.GET.get('table')))
        headers =  [f.name for f in model._meta.get_fields()]
        display_headers =  [f.verbose_name for f in model._meta.get_fields()]
        #response = [{j:getattr(f, j) for j in headers} for f in model.objects.all()]
        ## from 
        fields_dict = {}
        [fields_dict.update({field.name:field.verbose_name}) for field in model._meta.get_fields()]
        partner = filter(None,str(request.GET.get('part')).split(','))
        if len(partner) != 0:
            qmnth = request.GET.get('qid')
            qyr = request.GET.get('yid')
            fcn_yr = get_fincal_yr(qmnth,qyr)
            data = model.objects.filter(partner_id__in=partner).values(*fields_dict.keys())#,financial_month_year=fcn_yr)
        else:
            data = model.objects.all().values(*fields_dict.keys())
        for d in data:
            for k in d.keys():
                try:
                    if int(k):
                        choice = Choice.objects.get_or_none(id=d.get(k))
                        if choice:
                            d[k]=choice.text
                except Exception as e:
                    pass
        ## to
        get_page = ceil(float(len(data)) / float(10))
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(data, request)
        return paginator.get_paginated_response(result_page, '200', 'Successfully Retreieved', 37, get_page,\
        headers=display_headers, download=headers, table=request.GET.get('table'))



class MutantReportFilterView(APIView):
    def get(self,request,uid):
        try:
            usr = UserRoles.objects.get(user_id=uid)
            if usr.user.is_superuser and not request.GET.get('pid'):
                b = Boundary.objects.filter(active=2).values_list('region_id',flat=True)
                rgn = [{"id":str(rg.id),"name":str(rg.name)} for rg in MasterLookUp.objects.filter(id__in=b,active=2)]
                stat = [{"id":"","name":""}]
                part = [{"id":"","name":""}]
                autopop = "False"
                msg = "Success"
                status = 2
            elif request.GET.get('pid') and usr.user.is_superuser:
                part_obj = Partner.objects.get(id=request.GET.get('pid'))
                part = [{"id":str(part_obj.id),"name":str(part_obj.name)}]
                rgn = [{"id":str(part_obj.state.region.id),"name":str(part_obj.state.region.name)}]
                stat = [{"id":str(part_obj.state.id),"name":str(part_obj.state.name)}]
                autopop = "True"
                msg = "Success"
                status = 2
            else:
                part = [{"id":str(usr.partner.id),"name":str(usr.partner.name)}]
                rgn = [{"id":str(usr.partner.state.region.id),"name":str(usr.partner.state.region.name)}]
                stat = [{"id":str(usr.partner.state.id),"name":str(usr.partner.state.name)}]
                autopop = "True"
                msg = "Success"
                status = 2
        except Exception as e:
            rgn = []
            part=stat=rgn
            autopop = "False"
            msg = str(e.message)
            status = 0
        res = {"region":rgn,"state":stat,"partner":part,"autopop":autopop,"message":msg,"status":status}
        return Response(res)


class RegoinStateView(APIView):
    def get(self,request,uid,rgid):
        try:
            usr = UserRoles.objects.get(user_id=uid)
            stat = [{"id":str(rg.id),"name":str(rg.name)} for rg in Boundary.objects.filter(active=2,boundary_level=2,region_id=rgid)]
            msg = "Success"
            status = 2
        except Exception as e:
            stat = []
            msg = str(e.message)
            status = 0
        res = {"state":stat,"message":msg,"status":status}
        return Response(res)


class StatePartnerView(APIView):
    def get(self,request,uid,pid):
        try:
            usr = UserRoles.objects.get(user_id=uid)
            part = [{"id":str(rg.id),"name":str(rg.name)} for rg in Partner.objects.filter(active=2,state_id=pid)]
            msg = "Success"
            status = 2
        except Exception as e:
            part = []
            msg = str(e.message)
            status = 0
        res = {"partner":part,"message":msg,"status":status}
        return Response(res)
