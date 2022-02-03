from django.shortcuts import render

# Create your views here.
def Show_IndexPage(request):
    content = {}
    return render(request,"IE/index.html",content)