from django.urls import path
from .views import FaqDetails, FaqInfo

urlpatterns = [

    path("faq/", FaqDetails.as_view(), name="faq"),
    path("faq/<int:faq_id>", FaqInfo.as_view()),
    path("faq/<str:question>", FaqInfo.as_view())

]
