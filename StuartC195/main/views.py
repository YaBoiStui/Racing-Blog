from django.shortcuts import render, redirect
from .models import RaceResult, Comment, Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django import forms


# Home page
def home(request):
    # Show latest 3 races
    top_races = RaceResult.objects.order_by('-date')[:3]
    return render(request, 'home.html', {'top_races': top_races})


# Timeline page
def timeline(request):
    races = RaceResult.objects.order_by('-date')
    return render(request, 'timeline.html', {'races': races})


# User registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# User login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


# User logout
def user_logout(request):
    logout(request)
    return redirect('login')


# Add comment to a race
@login_required
def add_comment(request, race_id):
    race = RaceResult.objects.get(id=race_id)
    if request.method == "POST":
        text = request.POST['comment_text']
        Comment.objects.create(user=request.user, race_result=race,
                               comment_text=text)
        return redirect('timeline')
    return render(request, 'add_comment.html', {'race': race})


# Form for adding a race result
class RaceResultForm(forms.ModelForm):
    class Meta:
        model = RaceResult
        fields = ['race_name', 'date', 'position', 'car_used', 'notes']


# Add Race Result page (only for logged-in users)
@login_required
def add_race(request):
    if request.method == 'POST':
        form = RaceResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timeline')
    else:
        form = RaceResultForm()
    return render(request, 'add_race.html', {'form': form})


# Add events to Contact page
def contact(request):
    events = Event.objects.order_by('date')
    return render(request, 'contact.html', {'events': events})
