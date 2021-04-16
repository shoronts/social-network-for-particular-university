from django.urls import path, include
from .views import IndexView as users


urlpatterns = [
    path('register/', users.register, name='register'),
    path('teacher-register/', users.teacherRegister, name='teacherregister'),
    path('student-register/', users.studentRegister, name='studentregister'),
    path('company-register/', users.companyRegister, name='companyregister'),
    path('login/', users.login, name='login'),
    path('logout/', users.logout, name='logout'),
    path('profile/', users.profile, name='profile'),
    path('recommend/', users.recommend, name='recommend'),
    path('recommend-list/', users.recommendlist, name='recommendlist'),
    path('recommend-list/<slug>/', users.recommendlistedit, name='recommendlistedit'),
    path('recommend-list-delete/<slug>/', users.recommendlistdelete, name='recommendlistdelete'),
    path('recommend-list-view/<slug>', users.recommendpdf, name='recommendpdf'),
]
