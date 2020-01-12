from django.shortcuts import render
from feedbackapp1.models import FeedbackData
from feedbackapp1.forms import FeedbackForm
from django.http.response import HttpResponse
import datetime as dt
date1=dt.datetime.now()

# Create your views here.
def Feedbackview(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name1=request.POST.get('Name')
            rating1=request.POST.get('Rating')
            feedback1=request.POST.get('Feedback')
            data=FeedbackData(
            Name=name1,
            Rating=rating1,
            Date=date1,
            Feedback=feedback1
            )
            data.save()
            fform=FeedbackForm()
            Feedbacks=FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'Feedbacks':Feedbacks})
        else:
            return HttpResponse("User Missed Some Value")
    else:
        fform=FeedbackForm()
        #Feedbacks=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform})

