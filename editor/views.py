from django.shortcuts import render

def editor(request):
    return render(request, 'editor/editor.html')
