from django.http import HttpResponse
#from django.template import loader
from .models import Question
from django.shortcuts import get_object_or_404, render

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

    #テンプレートの読み込み
    #template = loader.get_template('polls/index.html')

    #テンプレートで使う変数を設定
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)

#詳細ページ
def detail(request, question_id):
    # try:
    #     questtion = Question.objects.get(pk=question_id)
    #     #主キーはそのカラム名に関わらず pk= で検索できる
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # return render(request, 'polls/detail.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls.detail.html', {'question': question})
    
#結果ページ
def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response .format(question_id))

#投票ページ
def vote(request, question_id):
    return HttpResponse("You're vooting on question {}.".format(question_id))
