from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['text']
    wordlist = text.split()
    worddDictionary = {}
    for word in wordlist:
        if word in worddDictionary:
            worddDictionary[word] += 1
        else:
            worddDictionary[word] = 1

    sortedList = sorted(worddDictionary.items(), key=operator.itemgetter(1))

    #sortedList = worddDictionary.items()

    return render(request, 'count.html', {'text':text, "count":len(wordlist), 'fullInfo':sortedList} )
