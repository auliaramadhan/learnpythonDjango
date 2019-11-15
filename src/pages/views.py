from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(req, *args, **kwargs):
    print(args, kwargs)
    print(req.user)
    # return HttpResponse('dsadas')
    return render(req, "home.html", {})


def about_view(req, *args, **kwargs):
    context = {
        "title": "about us",
        "my_number": 123,
        'list': [i for i in range(10) if i%2==0]
    }
    return render(req, "about.html", context)


def contact_view(req, *args, **kwargs):
    return render(req, "contact.html", {})

