from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
from Api.views import Customerviewsetview

router=DefaultRouter()
router.register("customer",Customerviewsetview,basename="customer")

urlpatterns=[

    path("token/",ObtainAuthToken.as_view()),
    # path("creatework/<int:pk>",workcreateview.as_view())
        
]+router.urls