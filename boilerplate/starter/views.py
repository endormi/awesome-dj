from django.shortcuts import render


def home(request):

    context = {"active": "home"}
    return render(request, "index.html", context=context)


def about(request):

    context = {"active": "about"}
    return render(request, "about.html", context=context)


def contact(request):

    context = {"active": "contact"}
    return render(request, "contact.html", context=context)
