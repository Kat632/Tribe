from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

"""
This is the home page that takes all forums and discussion objects and passes them to the templates through a dictionary named context. 
This page links to both the other pages and shows all the required information to the user with the feature of adding more information in any forum.
"""


def home(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())
    context = {
        'forums': forums,
        'count': count,
        'discussions': discussions}
    return render(request, 'forumHome.html', context)


"""
This function is used to create a new forum through an instance of CreateInForum() object defined in forms.py and also, 
it takes the filled data through request.POST and checks if the data is valid to save it in our database 
and after successfully storing it redirects to the home page otherwise it again asks user to fill the correct information.
"""


def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form}
    return render(request, 'addInForum.html', context)


"""
This is very similar to the previous function, the only change is it is used to add opinions to existing forums.
"""


def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'addInDiscussion.html', context)
