from django.shortcuts import render

def index(request):
    remembrancies=["Интервью у памятника","Школьные годы","333","444","555"]
    data = {"color": "green", "remembrancies": remembrancies}
    return render(request, "firstapp/index.html", context=data)

def fapp_aa(request):
    return render(request, 'firstapp/aa.html', {})

def colr(request, productid='green'):
    data = {"color": productid}
    
    return render(request, "firstapp/index.html", context=data)


