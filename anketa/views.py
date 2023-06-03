from django.shortcuts import render, redirect
from .forms import QuestionnaireForm
from .models import Questionnaire


def questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            questionnaire = form.save()
            return redirect('result', pk=questionnaire.pk)
    else:
        form = QuestionnaireForm()
    return render(request, 'questionnaire/questionnaire.html', {'form': form})


def result(request, pk):
    questionnaire = Questionnaire.objects.get(pk=pk)
    bmi = questionnaire.calculate_bmi()
    return render(request, 'questionnaire/result.html', {'questionnaire': questionnaire, 'bmi': bmi})
