from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


def index(request):
    questions = Question.objects.order_by("-pub_date")
    context = {
        "questions": questions,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
        "choices": [choice for choice in question.choice_set.all()],
    }
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "polls/results.html", context)


def vote(request, question_id):
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
        context = {
            "question": question,
        }
        return render(request, "polls/results.html", context)
