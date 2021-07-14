from django import forms
from .models import Answer, Question
from django.forms import fields, widgets

# cats_menu = Category.objects.all().values_list('name', 'name')
# choice_list = []

# for item in cats_menu:
#     choice_list.append(item)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'author']

        widgets = {
            'answer' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Type your answer'}),
            'author' : forms.Select(attrs={'class' : 'form-control'}),
            # 'category' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Category'}),
        }

class EditAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']

        widgets = {
            'answer' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Update your answer'}),
            # 'category' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Category'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'category', 'author', 'question')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Title'}),
            'category' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Category'}),
            'author' : forms.Select(attrs={'class' : 'form-control'}),
            'question' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Type your query' }),
        }


class EditQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'category', 'question']

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Title'}),
            'category' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Category'}),
            'question' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Update your query' }),
        }






# class UserLoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
# Category ---> Web Framework , Python, Django, 
