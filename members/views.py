from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question, Answer, User
from django.urls import reverse

# Create your views here.

def LikeView(request, pk):
    detail1 = request.POST.get('upvote')
    detail2 = request.POST.get('downvote')

    if(detail2 == None):
        post = get_object_or_404(Answer, id=request.POST.get('upvote'))
        if(post.userDownVotes.filter(id = request.user.id).exists()):
            post.userDownVotes.remove(request.user)
        post.userUpVotes.add(request.user)
    elif(detail1 == None):
        post = get_object_or_404(Answer, id=request.POST.get('downvote'))
        if(post.userUpVotes.filter(id = request.user.id).exists()):
            post.userUpVotes.remove(request.user)
        post.userDownVotes.add(request.user)
    return HttpResponseRedirect(reverse('question_details', args=[str(pk)]))

def home(request):
    allquestionswithanswers = Question.objects.filter(answered = True).order_by('created')
    answered_questions = Answer.objects.filter(answered = True).order_by('-created')
    question_lists = Question.objects.filter(answered = False).order_by('-created')
    return render(request, 'home.html', {'question_lists' : question_lists, 'answered_questions' : answered_questions, 'allquestionswithanswers': allquestionswithanswers})


def QuestionDetailView(request, pk):
    que = Question.objects.filter(id=pk)
    answered_questions = Answer.objects.filter(question_id = que[0].id).order_by('-created')
    return render(request, 'question_details.html', {'que':que[0], 'answered_questions' : answered_questions})


def AddQuestionView(request, pk):
    if request.method == "POST":
        title = request.POST.get('title', '')
        question = request.POST.get('question', '')
        category = request.POST.get('category', '')
        user_kundli = User.objects.filter(id=pk)
        que = Question(title=title, question=question, author=user_kundli[0], category=category)
        que.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'add_question.html')

def AddAnswerView(request, pk):
    ques_kundli = Question.objects.filter(id = pk)
    user = request.user
    if request.method == "POST":
        answer = request.POST.get('answer', '')
        author = user
        ans = Answer(question_id = ques_kundli[0], answered = True, author = author, answer = answer)
        votesscore = ques_kundli[0].votesscore + 1
        Question.objects.filter(id = pk).update(answered = True, votesscore = votesscore)
        ans.save()
        return HttpResponseRedirect(reverse('question_details', args=[str(ques_kundli[0].id)]))
    return render(request, 'add_answer.html', {'ques_kundli': ques_kundli[0]})

def UpdateQuestionView(request, pk):
    ques_kundli = Question.objects.filter(id = pk)
    user = request.user
    if user.id != ques_kundli[0].author.id:
        return render(request, 'update_question.html')
    if request.method == "POST":
        question = request.POST.get('question', '')
        title = ques_kundli[0].title
        category = ques_kundli[0].category
        author  = ques_kundli[0].author
        Question.objects.filter(id = pk).update(question = question, title = title, category = category, author = author)
        return HttpResponseRedirect(reverse('question_details', args=[str(ques_kundli[0].id)]))
    return render(request, 'update_question.html', {'ques_kundli' : ques_kundli[0]})


def UpdateAnswerView(request, pk):
    ans_kundli = Answer.objects.filter(id = pk)
    ques_kundli = Question.objects.filter(id = ans_kundli[0].question_id.id)
    user = request.user
    if user.id != ans_kundli[0].author.id:
        return render(request, 'update_answer.html')
    if request.method == "POST":
        answer = request.POST.get('answer','')
        Answer.objects.filter(id=pk).update(answer=answer)
        return HttpResponseRedirect(reverse('question_details', args=[str(ques_kundli[0].id)]))
    return render(request, 'update_answer.html', {'ans_kundli' : ans_kundli[0], 'ques_kundli' : ques_kundli[0]})

def DeleteQuestionView(request, pk):
    ques_kundli = Question.objects.filter(id = pk)
    user = request.user
    if user.id != ques_kundli[0].author.id:
        return render(request, 'delete_question.html')
    if request.method == "POST":
        Question.objects.filter(id = pk).delete()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'delete_question.html')

def DeleteAnswerView(request, pk):
    ans_kundli = Answer.objects.filter(id = pk)
    ques_kundli = Question.objects.filter(id = ans_kundli[0].question_id.id)
    user = request.user
    if user.id != ans_kundli[0].author.id:
        return render(request, 'delete_answer.html')
    if request.method == "POST":
        votesscore = ques_kundli[0].votesscore - 1
        if(ques_kundli[0].votesscore == 1):
            Question.objects.filter(id = ans_kundli[0].question_id.id).update(answered = False)
        Question.objects.filter(id = ans_kundli[0].question_id.id).update(votesscore = votesscore)
        Answer.objects.filter(id = pk).delete()
        return HttpResponseRedirect(reverse('question_details', args=[str(ques_kundli[0].id)]))
    return render(request, 'delete_answer.html')


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allQuestions = Question.objects.none()
    else:
        allQuestionTitle = Question.objects.filter(title__icontains=query)
        #allQuestionAuthor = Question.objects.filter(author__icontains=query)
        allQuestionsQuestion = Question.objects.filter(
            question__icontains=query)
        search = allQuestionTitle.union(allQuestionsQuestion)
        print(search)
    if search.count() == 0:
        return HttpResponse("<h1>No matching results")
    #params = {'allQuestions': allQuestions, 'query': query}
    return render(request, 'search.html', {'search': search})
