from .views import Home,AddPersonView,AddExpView,ExpDeleteView,AddEduView,EduDeleteView,SummaryView
from django.urls import path

app_name = 'cv'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('add_cv/',AddPersonView.as_view(),name='add_cv'),
    path('add_exp/',AddExpView.as_view(),name='add_exp'),
    path('exp_delete/<int:pk>/',ExpDeleteView.as_view(),name='exp_delete'),
    path('add_edu/',AddEduView.as_view(),name='add_edu'),
    path('edu_delete/<int:pk>/',EduDeleteView.as_view(),name='edu_delete'),
    path('summary',SummaryView.as_view(),name='summary')
]