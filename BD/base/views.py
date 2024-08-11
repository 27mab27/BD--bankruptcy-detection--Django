from django.shortcuts import render


def homePage(request):
    return render(request,'home.html')

def table(request):
    return render(request,'table.html')

def ourModel(request):
    return render(request,'OurModel.html')
