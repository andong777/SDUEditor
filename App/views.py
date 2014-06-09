from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext, redirect
from django.http import HttpResponse
from App import forms, xmlhelper, models
from datetime import datetime
import json

def home(request):
    records = models.Record.objects.order_by('-add_time')
    print(records)
    return render_to_response('home.html', {'records':records})

def editor(request):
    return redirect('file/editor.html')

def load():
    return redirect('file/editor.html')

def edit_new(request):
    if request.method == 'GET':
        if 'title' in request.GET and 'writer' in request.GET and 'nation' in request.GET and 'content' in request.GET:
            xmlhelper.write(request.GET)
            return HttpResponse('成功！')
    return redirect('file/edit_new.html')

def save(request):
    lst = request.GET
    now = datetime.now()
    models.Record.objects.create(title=lst['title'],writer=lst['writer'],nation=lst['nation'],content=lst['content'],add_time=now)
    xmlhelper.write(request.GET)
    return render_to_response('export.html',{'title':lst['title']})

def search(request):
    if request.method == "GET" and 'q' in request.GET:
        q = request.GET['q']
        print(q)
    response_data = {}
    response_data['status'] = 'OK'
    response_data['char'] = '曌'
    return HttpResponse(json.dumps(response_data), content_type="application/json")