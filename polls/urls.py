from django.urls import path

from polls.models import Question

from . import views

urlpatterns = [
    #ex: /polls/
    #polls/ にアクセスするとviews.indexを呼び出す
    path('', views.index, name='index'),

    #ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    #ex: /polls/results/5
    path('<int:question_id>/results/', views.results, name='results'),
    #ex: /polls/vote/5
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
