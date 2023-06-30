from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,WebPage,AccessRecord

# Create your views here.
def index(request):
    # dictanory={'santhosh':" code coming fromviews.py file"}
    Webpage_list =AccessRecord.objects.order_by('date')
    date_dict = {'access_records':Webpage_list}

    return render(request,'first_app/index.html',context=date_dict)
