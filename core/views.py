from django.shortcuts import render, HttpResponse
from itertools import combinations

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(
            request,
            "core/index.html",
        )
    if request.method == "POST":
        start_number = int(request.POST.get("start_number"))
        stop_number = int(request.POST.get("stop_number"))
        possible_combinations = list(combinations(range(start_number, stop_number+1),3))

        possible_string_combinations = []

        for combination in possible_combinations:
            combination_array = []
            for number in combination:
                stringed_number =str(number)
                combination_array.append(stringed_number)
            possible_string_combinations.append("-".join(combination_array))

        print(possible_string_combinations)

        context = {"combinations": possible_string_combinations}

        return render(request, "core/index.html", context,)
