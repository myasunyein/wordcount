from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return HttpResponse('Hello server')

def eggs(request):
    return HttpResponse('Hello eggs are great')    

def home(request):
    return render(request, 'home.html',{'hithere': 'this is me'})


def count(request):
    fulltext=request.GET['fulltext']
        
    print(fulltext)

    wordlist=fulltext.split()

    worddictionary = {}
    
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word]=1

    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary.items(),'sortedwords':sortedwords})


def about(request):

    about=request.GET['about']


    return render(request, 'about.html', {'about':about})