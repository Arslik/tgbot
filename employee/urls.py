from django.urls import path
from .views import EmployeeDetail, EmployeeInfo, EmployeeUsernameSearch, \
    EmployeeEmailSearch, EmployeePhoneSearch, StatusDetail

urlpatterns = [

    path("emp/", EmployeeDetail.as_view(), name="emp"),
    path("emp/<int:employee_id>", EmployeeInfo.as_view()),
    path("emp/<str:username>", EmployeeUsernameSearch.as_view()),
    path("email", EmployeeEmailSearch.as_view(), name="email"),
    path("phone", EmployeePhoneSearch.as_view(), name="phone"),
]
