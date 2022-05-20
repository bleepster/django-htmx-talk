from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Question, Choice
from .forms import PollsAuthenticationForm, PollsUserCreationForm


def register(request):
    if request.method == "POST":
        form = PollsUserCreationForm(request.POST, label_suffix="")
        if form.is_valid():
            form.save()
            return redirect("polls:login")
    else:
        form = PollsUserCreationForm(label_suffix="")
    return render(request, "polls/register.html", context={"register_form": form})

def user_login(request):
    if request.method == "POST":
        form = PollsAuthenticationForm(request, data=request.POST, label_suffix="")
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("polls:index")
        messages.error(request, "Invalid username or password.")
    else:
        form = PollsAuthenticationForm(label_suffix="")
    return render(request, "polls/login.html", context={"login_form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("polls:login")

@login_required
def index(request):
    if request.method == "POST":
        question_id = request.POST["question"]
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            context = {
                "question": question,
                "error_message": "You didn't select a choice",
            }
            return render(request, "polls/detail.html", context)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # See django documentation on why this should be a redirect
            # https://docs.djangoproject.com/en/4.0/intro/tutorial04/#write-a-minimal-form
            return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    else:
        questions = Question.objects.order_by("-pub_date")
        context = {
            "questions": questions,
        }
    return render(request, "polls/index.html", context)

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "polls/results.html", context)

@login_required
def get_choices(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choices = Choice.objects.filter(question=question)
    except (KeyError, Choice.DoesNotExist):
        response = {
            "choices": [],
            "question": question,
            "error_message": "Not Found",
        }
    else:
        response = {
            "choices": [{"choice_id": choice.id, "choice_text": choice.choice_text} for choice in choices],
            "question": question.question_text,
            "error_message": None,
        }
    return JsonResponse(response)

