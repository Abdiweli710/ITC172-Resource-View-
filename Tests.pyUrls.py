from django.shortcuts import render
from .models import Meeting

# Create your views here
def index (request):

def getmeetings(request):
	type_list=Meeting.objects.all() 
	return render(request, 'clubapp/meeting.html', {'type_list': type_list})
