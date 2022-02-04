from django.shortcuts import render

# Create your views here.
def Show_IndexPage(request):
    contest = {}
    return render(request,"IE/index.html",contest)