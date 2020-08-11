from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    users = User.objects.all()
    for user in users:
        print(user.email)
    if messages in request.session:
        context = {
            'messages': request.session['messages']
        }
        del request.session['messages']
    else:
        context = {
            'messages': [],
            'users': users
        }
    return render(request, 'social_network/index.html', context)

def register(request):
    if request.method == 'POST':
        messages = User.objects.register(request.POST)
    if not messages:
        print("No messages! Success!")
        user_list = User.objects.all().filter(email=request.POST['email'])
        request.session['id'] = user_list[0].id
        request.session['name'] = user_list[0].first_name
        return redirect('/')
    else:
        print(messages)
        return redirect('/landing')

def login(request):
    users = User.objects.all()
    if request.method == 'POST':
        messages = User.objects.login(request.POST)
        email = request.POST['email']
        password = request.POST['password'].encode('utf-8')
        postData = {
            'email': email,
            'password': password
        }
    if not messages:
        print ("No messages! Success!")
        user_list = User.objects.all().filter(email=request.POST['email'])
        request.session['id'] = user_list[0].id
        request.session['name'] = user_list[0].first_name
        return redirect('/landing')
    else:
        print("Messages: {}".format(messages))
        request.session['messages'] = messages
        return redirect('/landing')

def landing(request):
    session_name = request.session['name']
    users = User.objects.all()
    context = {
        'session_name': session_name,
        'users': users
    }
    return render(request, 'social_network/landing.html', context)
