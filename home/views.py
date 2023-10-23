from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    view_users = [{'name': 'Alice', 'age': 25},
                  {'name': 'Bob', 'age': 12},
                  {'name': 'Charlie', 'age': 17},
                  {'name': 'David', 'age': 28}
    ]
    return render(request,"index.html",context={"users":view_users})

# Create your views here.
