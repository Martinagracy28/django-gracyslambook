from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Slam

# Create your views here.

def home(request):
	
	if request.method=="POST":
		name = request.POST['name']
		return render(request,'slambook.html',{'name':name})
	else:
		return render(request,'home.html')


def slambook(request):
    s = Slam()
    if request.method=="POST":
        s.name = request.POST['name']
        s.relationship = request.POST['relationship']
        s.nick_name = request.POST['nick_name']
        s.image = request.FILES['image']
        s.like = request.POST['like']
        s.dislike = request.POST['dislike']
        s.video = request.FILES['video']
        s.gift = request.POST['gift']
        s.last_word = request.POST['last_word']
        s.message = request.POST['message']
        s.save()
        print("saved")
        return redirect("thank")
    else:
        return render(request,"slambook.html")
        
def thank(request):
	return render(request,'thank.html')
	