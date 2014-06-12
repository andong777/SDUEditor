from django.shortcuts import render_to_response, redirect
#from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from App import models
from datetime import datetime
import json
from Util import scode, sformat, xmlhelper


def home(request):
    records = models.Record.objects.order_by('-add_time')
    print(records)
    return render_to_response('home.html', {'records':records})

def editor(request):
    return redirect('/file/editor.html')

def load():
    return redirect('/file/editor.html')

def edit_new(request):
    return redirect('file/edit_new.html')

def save(request):
    lst = request.GET
    now = datetime.now()
    models.Record.objects.create(title=lst['title'],writer=lst['writer'],nation=lst['nation'],content=lst['content'],add_time=now)
    xmlhelper.write(request.GET)
    return render_to_response('export.html',{'title':lst['title']})

def search(request):
    if request.method == "GET" and 'side' in request.GET and 'num' in request.GET and 'pinyin' in request.GET:
        side = request.GET['side']
        num = request.GET['num']
        pinyin = request.GET['pinyin']
    response_data = {}
    response_data['status'] = 'OK'
    response_data['char'] = "".join(scode.fetch(side=side, num=num, pinyin=pinyin))
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def export(request, type, title):
    type = type.strip().lower()
    title = title.strip().lower()
    if type=='pdf':
        sformat.exportPDF(title)
    elif type=='image':
        sformat.exportImage(title)
    elif type=='html':
        sformat.exportHTML(title)


