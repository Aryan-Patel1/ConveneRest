from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FacilityAdd, FacilityTypeListing, FacilityDetail, FacilityUpdate, \
                    FacilitySubTypeListing, FacilityListing, ThematicAreaListing, \
                    FacilityWtPaginationListing

urlpatterns = [
    url(r'^facilityadd/$', FacilityAdd.as_view(), {'key':'facility'}),
    url(r'^facilitytype/$', FacilityTypeListing.as_view()),
    url(r'^facilitysubtype/$', FacilitySubTypeListing.as_view()),
    url(r'^thematicarealisting/$', ThematicAreaListing.as_view()),
    url(r'^facilitydetail/$', FacilityDetail.as_view(), {'key':'facility'}),
    url(r'^facilityupdate/$', FacilityUpdate.as_view(), {'key':'facility'}),
    url(r'^facilitylisting/$', FacilityListing.as_view(), {'key':'facility'}),
    url(r'^facilitydatewiselisting/$', FacilityWtPaginationListing.as_view(), {'key':'facility'}),

#    url(r'^facilitycenteradd/$', FacilityCentreAdd.as_view()),
#    url(r'^facilitycenterupdate/$', FacilityCentreUpdate.as_view()),
#    url(r'^facilitycenterdetail/$', FacilityCentreDetail.as_view()),
#    url(r'^facilitylisting/$', FacilityListing.as_view()),
#    url(r'^centrelisting/$', ParentCentreListing.as_view()),
#    url(r'^centretypelisting/$', CentresListing.as_view()),
]
