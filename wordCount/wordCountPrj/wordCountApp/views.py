from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()
    print(word_list)
    word_dictionary = {}
    sum = 0

    for word in word_list:
        print(word)
        print(len(word))
        sum = sum + len(word)
        print(sum)

        if word in word_dictionary:
            word_dictionary[word] += 1
    
        else:
            word_dictionary[word] = 1     

    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'length': len(word_list), 'count': len(entered_text), 'nocount' : sum})


def hello(request):
    entered_name = request.GET['name']
    return render(request,"hello.html", {'alltext': entered_name})