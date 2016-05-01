from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from random import randint

# Create your views here.

questions_list = []
answers_list = []

for i in range(100):
    questions_list.append({
        'id': i,
        'title': 'Question #{}.How to build a moon park?'.format(i),
        'body': "Guys, i have trouble with a moon park. Can't find the black-jack...",
        'tag': ['tag' + str(j) for j in xrange(1, randint(1, 10))]
    })

for i in range(5):
    answers_list.append({
        'body': "Lorem bla bla bla Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
    })


def paginate(param, request, num_of_list):
    contact_list = param
    paginator = Paginator(contact_list, num_of_list)  # Show 25 number_page per page
    page = request.GET.get('page')
    try:
        number_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        number_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        number_page = paginator.page(paginator.num_pages)
    return number_page


def index(request):
    page = paginate(questions_list, request, 7)
    return render(request, 'index.html', {"questions": page})


def hot(request):
    page = paginate(questions_list, request, 7)
    return render(request, 'index.html', {"questions": page})


def tag(request, tagName):
    questions_list_tag = []
    for i in questions_list:
        if tagName in i['tag']:
            questions_list_tag.append(i)
    page = paginate(questions_list_tag, request, 7)
    return render(request, 'tag.html', {"questions": page, "tagName": tagName})


def question(request, question_id):
        return render(request, 'question.html', {"question": questions_list[int(question_id)], "answers": answers_list})


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def ask(request):
    return render(request, 'ask.html')


def hello(request):
    answer = '<h1>Hello world!</h1><h2>' + request.method + ' REQUEST:</h2>'
    if (request.method == 'GET'):
        d = request.GET
    elif (request.method == 'POST'):
        d = request.POST
    for key in sorted (d.keys()):
        answer += '<p>' + key + ' : ' + str(d.get(key)) + '</p>'
    return HttpResponse(answer)



