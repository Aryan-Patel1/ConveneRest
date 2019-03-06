from uuid import uuid4
import calendar
import datetime
from datetime import date, timedelta
from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps
from django.http import JsonResponse
from django.db.models import Max
from survey.serializers import *
from survey.models import *
from userroles.models import UserRoles,UserPartnerMapping
from masterdata.models import (MasterLookUp, Boundary, DocumentCategory)
from facilities.models import Facility
from workflow.models import WorkFlowBatch, WorkFlowSurveyRelation
from dynamic_listing.views import (get_quarter, month_range, get_last_quarter_dates,
                                   get_last_quarter_months, get_last_yearly_months, get_last_half_yearly_dates, get_last_month_date,)
from box import Box
from partner.models import Partner
from .custom_dates import CustomDates
from survey_views import get_user_partner,SurveyResponses
from .custom_dates import CustomDates
from common_methods import convert_list_args_to_str
import csv
from django.http import HttpResponse
from ccd.settings import HOST_URL,BASE_DIR,FY_YEAR
import pytz     



class EditQuestion(APIView):
    def post(self , request):
        form_data = request.data
        try:
            q = Question.objects.get(id = form_data.get('id') , active = 2)
            question_dict = dict()
            question_dict['questionType'] = q.qtype
            question_dict['questionLabel'] = q.text
            question_dict['questionCode'] = q.code
            question_dict['questionMandatory'] = q.mandatory
            question_dict['questionProfile'] = q.is_profile if q.is_profile else ''
            question_dict['questionChoice']  = []
        question_dict['constraints'] = dict()
        qv = QuestionValidation.objects.get(question__id = form_data.get('id') , active = 2)
        question_dict['constraints']['charactersType'] = q.validation
        question_dict['constraints']['minLength'] = qv.max_value
        question_dict['constraints']['maxLength'] = qv.min_value
        question_dict['constraints']['validationOption'] = 
        
        
        
        
        
        
        
        
        
        
        {"blockId":"96","questionType":"T","questionLabel":"Test Text","questionCode":"118","questionMandatory":"False","questionProfile":"True","questionChoice":[],"constraints":{"charactersType":"3","minLength":"12","maxLength":"123","validationOption":"O","validationMessage":"Success",
        "question_validation":"","question_condition":""},
        "masterProfile":"False","categoryType":[]}: 
        
    {"blockId":"96","questionType":"S","questionLabel":"Test Drodown","questionCode":"119","questionMandatory":"False","questionProfile":"True","questionChoice":[],"constraints":{},"masterProfile":"True","categoryType":[{"type":"BF","id":"1"}]}: 
    
    {"blockId":"96","questionType":"S","questionLabel":"Test text","questionCode":"120","questionMandatory":"True","questionProfile":"False","questionChoice":[{"choiceLabel":"optiontest","choiceValue":"12","choiceShortCode":"123"}],"constraints":{},"masterProfile":"False","categoryType":[]}: 
    
    
    
    {"blockId":"96","questionType":"C","questionLabel":"Test Checkbox","questionCode":"121","questionMandatory":"False","questionProfile":"True","questionChoice":[],"constraints":{},"masterProfile":"True","categoryType":[{"type":"BF","id":"1"}]}: 
    
    
    
    
    {"blockId":"96","questionType":"C","questionLabel":"Test choice","questionCode":"122","questionMandatory":"False","questionProfile":"False","questionChoice":[{"choiceLabel":"choice test","choiceValue":"12","choiceShortCode":"123"}],"constraints":{},"masterProfile":"False","categoryType":[]}: 
    
    
    
    {"blockId":"96","questionType":"R","questionLabel":"test radio","questionCode":"123","questionMandatory":"False","questionProfile":"False","questionChoice":[{"choiceLabel":"choice 1","choiceValue":"12","choiceShortCode":"123"}],"constraints":{},"masterProfile":"False","categoryType":[]}: 
    
    
    
    
    {"blockId":"96","questionType":"D","questionLabel":"test date","questionCode":"124","questionMandatory":"False","questionProfile":"True","questionChoice":[],"constraints":{"dateFormat":"mm-dd-yyyy","defaultDate":"2019-02-20","minDate":"2019-02-12","maxDate":"2019-02-19","charactersType":"8","question_condition":"current","validationMessage":"Success"},"masterProfile":"False","categoryType":[]}: 
    
    
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        "questionType":"T","questionLabel":"Auto question","questionCode":"121","questionMandatory":"False","questionProfile":"True","questionChoice":[],"constraints":{"charactersType":"12","minLength":"1","maxLength":"20000","validationOption":"O","validationMessage":"sdbjhh","question_validation":[726,727],"question_condition":"divide","question_sequence":"726,727"},"masterProfile":"False","categoryType":[]}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
