from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

#インデックスページ
def index(request):
    # Question を order_by(-pub_date)でソートし,前から5つの配列を取得(降順)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    #リスト内法表記,以下と同じ意味
    #queston_array = []
    #for q in latest_question_list:
    #   question_array.append(q.question_text)
    #output = ', '.join(question_array)

    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

#詳細ページ
def detail(request, question_id):
    return HttpResponse("You're looking at question {}.".format(question_id))

#結果ページ
def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response .format(question_id))

#投票ページ
def vote(request, question_id):
    return HttpResponse("You're vooting on question {}.".format(question_id))
