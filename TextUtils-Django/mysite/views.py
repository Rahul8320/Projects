# I have created this file -> Rahul
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('''<h1>About Django</h1><br>
                        <button type="button" onclick="window.location.href='http://127.0.0.1:8000';"> Home </button>''')

def analyzer(request):
    # get the text data
    text = request.POST.get('textarea', 'Default')
    # chack the checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    removextraspace = request.POST.get('removextraspace', 'off')
    charcount = request.POST.get('charcount', 'off')
    # ans string
    analyzer = []
    
    # for remove punctuations
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in text:
            if char not in punctuations:
                analyzed += char
        analyzer.append('Remove Punctuations')
        text = analyzed
        
    # for Upper Case
    if fullcaps == 'on':
        analyzed = ""
        for char in text:
            analyzed += char.upper()
        analyzer.append('Changed to Upper Case')
        text = analyzed
    
    # for remove extra space
    if removextraspace == 'on':
        analyzed = ""
        for index,char in enumerate(text):
            if(index+1 < len(text)):
                if not(text[index]==" " and text[index+1]==" "):
                    analyzed += char
        analyzer.append('Removed Extra Spaces')
        text = analyzed
        
    # for remove new lines
    if removenewline == 'on':
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed += char
        analyzer.append('Removed New Lines')
        text = analyzed
        
    # for char count
    if charcount == 'on':
        count = 0
        for char in text:
            count += 1
        analyzer.append('Character Count')
        text = text +"\n||  Character Count : "+str(count)+"  || "

    params = {'purpose':analyzer,'analyzed_text':text}
    return render(request, 'analyzer.html', params)
    