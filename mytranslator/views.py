from django.shortcuts import render
from django.http import HttpResponse
import googletrans
from googletrans import Translator
from gtts import gTTS
import gtts
from playsound import playsound
import os
import random
import string
import speech_recognition as sr

def index(request):
    return render(request, 'mytranslator/index.html')

def source_speech(request):
    display_flag = False
    text=""
    result=""
    d = {}
    d.update({'display_flag': display_flag})
    languages = googletrans.LANGUAGES
    d.update({'languages': languages})
    if request.method == 'POST':
        display_flag = True
        d.update({'display_flag': display_flag})
        s = request.POST['source']
        s = str(s)
        s = s.lower()
        print('source ---------- ', s)
        d.update({'source': s})
        de = request.POST['destination']
        de = str(de)
        de = de.lower()
        print("destination ---------------- ", de)
        d.update({'destination': de})
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say Something")
            audio = r.listen(source)
            print("Time Over, Thanks")
        try:
            print("source type === ", type(source))
            text = r.recognize_google(audio, language = str(source))
            d.update({'text': text})
            print("text - ", text)
        except Exception as e:
            print("exception here 1 - ", e)
        translator = Translator()
        try:
            result = translator.translate(text, src=s, dest=de)
            print(result.text)
            d.update({'result': result.text})
        except Exception as e:
            print("main erro is - ", e)
        #------------------------------------------
        # speech ----------------------------------
        try:
            tts = gtts.gTTS(result.text)
            random_str = ''.join(random.choices(string.ascii_uppercase+string.digits, k=10))    # generating random string -
            tts.save("audio_files/"+str(random_str)+".mp3")
            playsound("audio_files/"+str(random_str)+".mp3")
        except Exception as e:
            print("e = ", e)
        #------------------------------------------
    return render(request, 'mytranslator/source_speech.html', d)


def source_text(request):
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
        # translator ------------------------------
        translator = Translator()
        result = translator.translate(text, src=source, dest=destination)
        # print(result)
        d.update({'result': result.text})
        #------------------------------------------
        # speech ----------------------------------
        try:
            tts = gtts.gTTS(result.text)
            random_str = ''.join(random.choices(string.ascii_uppercase+string.digits, k=10))    # generating random string -
            tts.save("audio_files/"+str(random_str)+".mp3")
            playsound("audio_files/"+str(random_str)+".mp3")
        except Exception as e:
            print("e = ", e)
        #------------------------------------------ 
    return render(request, 'mytranslator/source_text.html', d) 

