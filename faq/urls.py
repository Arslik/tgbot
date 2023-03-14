from django.urls import path
from .views import FaqDetails, FAQByQueryAPIView

urlpatterns = [

    path("faq/", FaqDetails.as_view(), name="faq"),
    path('', FAQByQueryAPIView.as_view()),

]
