from django.shortcuts import render,redirect
from PyDictionary import PyDictionary
from django.contrib import messages
from googletrans import Translator

# Create your views here.
def index(request):
    return render(request,'index.html')

def word(request):
    search=request.GET.get('search')

    dictionary=PyDictionary()
    trans=Translator()
    meaning=dictionary.meaning(search)
    if meaning is None:
        return redirect('/')
    meaning1=trans.translate(search,dest='hi')
    meaning2 = trans.translate(search, dest='mr')
    mean=meaning.values()
    for i in mean:
        mean=i[0]

    context={
        'mean':mean,
        'meaning1':meaning1.text,
        'meaning2':meaning2.text
    }

    return render(request,'word.html',context)