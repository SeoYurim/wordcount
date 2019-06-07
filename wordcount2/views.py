from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request,'about.html') 

def result(request):
  text = request.GET['fulltext']
  words = text.split()
  words_dictionary = {}

  for word in words:
    if word in words_dictionary:
      words_dictionary[word] += 1
    else:
      words_dictionary[word] = 1

  return render(request,'result.html', {'full': text, 'total': len(words), 'dictionary' : words_dictionary.items()})
