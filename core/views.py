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
        number_of_combinations = int(request.POST.get("number_of_combinations"))
        repition_number = int(request.POST.get("repition_number"))
        possible_combinations = list(
            combinations(
                range(start_number, stop_number + 1),
                number_of_combinations,
            )
        )

        num_limit = repition_number
        num_count = {}

        filtered_list = []

        for t in possible_combinations:
            for n in t:
                try:
                    if num_count[n] < num_limit:
                        filtered_list.append(t)
                        num_count[n] = num_count.get(n, 0) + 1
                except KeyError:
                    num_count[n] = num_count.get(n, 0) + 1
                    continue

        possible_combinations = filtered_list
        possible_string_combinations = []

        for combination in possible_combinations:
            combination_array = []
            for number in combination:
                stringed_number = str(number)
                combination_array.append(stringed_number)
            possible_string_combinations.append("-".join(combination_array))

        combinations_length = len(possible_string_combinations)
        context = {
            "combinations": possible_string_combinations,
            "combinations_length": combinations_length,
        }

        return render(
            request,
            "core/index.html",
            context,
        )


def words(request):
    if request.method == "GET":
        return render(
            request,
            "core/words.html",
        )
    if request.method == "POST":
        words = request.POST.get("words").strip()
        number_of_combinations = int(request.POST.get("number_of_combinations"))
        word_list = words.split(",")
        possible_combinations = list(combinations(word_list, number_of_combinations))

        possible_string_combinations = []

        for combination in possible_combinations:
            possible_string_combinations.append("-".join(combination))

        combinations_length = len(possible_string_combinations)
        context = {
            "combinations": possible_string_combinations,
            "combinations_length": combinations_length,
        }

        return render(
            request,
            "core/words.html",
            context,
        )
