from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('question/<int:pk>', views.QuestionDetailView, name='question_details'),
    path('add_question/<int:pk>', views.AddQuestionView, name='add_question'),
    path('add_answer/<int:pk>', views.AddAnswerView, name='add_answer'),
    path('question/edit/<int:pk>', views.UpdateQuestionView , name='update_question'),
    path('answer/edit/<int:pk>', views.UpdateAnswerView, name='update_answer'),
    path('question/<int:pk>/remove', views.DeleteQuestionView, name='delete_question'),
    path('answer/<int:pk>/remove', views.DeleteAnswerView, name='delete_answer'),
    path('like/<int:pk>' , views.LikeView, name = 'like_post'),
]
