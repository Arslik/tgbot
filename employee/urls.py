from django.urls import path
from .views import EmployeeDetail, EmployeeByQueryAPIView


urlpatterns = [

    path("detail/", EmployeeDetail.as_view(), name="detail"),
    path('', EmployeeByQueryAPIView.as_view()),
    # 127.0.0.1:8000/employee/?type=username&value=mashkanov

]
