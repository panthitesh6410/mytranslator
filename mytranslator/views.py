from django.shortcuts import render
from django.http import HttpResponse
import googletrans
from googletrans import Translator

def index(request):
    display_flag = False
    d = {}
    d.update({'display_flag': display_flag})
    languages = googletrans.LANGUAGES
    d.update({'languages': languages})
    if request.method == 'POST':
        display_flag = True
        d.update({'display_flag': display_flag})
        text = request.POST['text']
        d.update({'text': text})
        source = request.POST['source']
        d.update({'source': source})
        destination = request.POST['destination']
        d.update({'destination': destination})
        print(text, source, destination)
        translator = Translator()
        print("1st-------")
        result = translator.translate(text, src=source, dest=destination)
        print(result)
        d.update({'result': result.text})
    return render(request, 'mytranslator/index.html', d) 

