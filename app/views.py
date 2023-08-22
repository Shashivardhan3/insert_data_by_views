from django.shortcuts import render

from app.models import *
from django.http import HttpResponse

# Create your views here.


def insert_topic(request):
    tn=input('enter the topic :')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    return HttpResponse('topic data inserted')

def insert_webpage(request):
    tn=input('enter the topic:')
    n=input('enter the name:')
    u=input('enter the url:')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('webpage data inserted')

def insert_AC(request):
    tn=input('enter the topic:')
    n=input('enter the name:')
    u=input('enter the url:')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input('enter the date:')
    a=input('enter the author:')
    e=input('enter the email: ')
    ao=accessrecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    return HttpResponse(' accessrecord data inserted')




