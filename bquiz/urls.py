from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    path('list/',views.get_quiz, name='Get_quizes'),
    #path('view/<int:id>/',views.view_quiz, name='View_quiz'),
    #path('view/question/<int:id>/',views.view_question, name='View_question'),
    path('view/question/<int:id>/answer/',views.submit_ans, name='submit_ans')
    ]
