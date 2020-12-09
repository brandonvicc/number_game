from django.shortcuts import render, redirect
from .models import User
import random

# Create your views here.

def index(request):
    if 'random_num' not in request.session:
        request.session['guess_counter'] = 0
        request.session['random_num'] = random.randint(1,100)
        print(request.session['random_num'])
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def guess(request):
    if int(request.POST['guess']) > request.session['random_num']:
        request.session['answer'] = 'Your Guess was too high! Try again?!'
        request.session['answer_class'] = 'wrong'
    elif int(request.POST['guess']) < request.session['random_num']:
        request.session['answer'] = 'Your Guess was too low! Try again?!'
        request.session['answer_class'] = 'wrong'
    else:
        request.session['answer'] = 'You got it!! Congratulations!!!!!'
        request.session['answer_class'] = 'correct'
    request.session['guess_counter'] += 1
    return redirect('/')

def clear_session(request):
    request.session.flush()
    return redirect('/')


def create(request):
    User.objects.create(name= request.POST['name'], score= request.POST['score'])
    return redirect('/leaderboards')

def leaderboards(request):
    context = {
        'users': User.objects.all()
    }
    return render(request,'leaderboard.html', context)

def destroy(request,id):
    user = User.objects.get(id= id)
    user.delete()
    return redirect('/leaderboards')


