from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(
            request,
            "core/index.html",
        )
