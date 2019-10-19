from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import AddForm
from .models import DiaryModel


def entry(request):
    form = AddForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            note = request.POST['note']
            content = request.POST['content']
            posted_date = datetime.now()

            todays_diary = DiaryModel()
            todays_diary.note = note
            todays_diary.posted_date = posted_date
            todays_diary.content = content

            todays_diary.save()

        """
            Clear the form and return.
            3:21 PM 10/19/19 by Arjun Adhikari
        """
        return HttpResponseRedirect('')

    return render(
        request,
        'entry/add.html',
        {
            'title': 'Add Diary',
            'add_highlight': True,
            'addform': form,
        }
    )


def show(request):
    """
        We need to show the diaries sorted by date posted in descending order
        5:32 PM 10/19/19 by Arjun Adhikari
    """
    diaries = reversed(DiaryModel.objects.order_by('posted_date'))

    return render(
        request,
        'entry/show.html',
        {
            'show_highlight': True,
            'title': 'Diaries till now',
            'diaries': diaries
        }
    )
