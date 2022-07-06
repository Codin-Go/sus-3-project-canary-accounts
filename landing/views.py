from django.shortcuts import render
from datetime import datetime

# def homepage(request):
#     return render(request, "index.html")

def homepage(request):
    return render(request, "index.html")


def landing(request):
    context = {
                "weather":"hot",
                "temperature":"30"
    }

    context_dict = {
                "weather":"hot",
                "temperature":"30"
    }

    context["weather_data"] = context_dict 

    context["days"] = "3days"
    print(context)

    context_list = [
        "Codingo", "AnErang", "MinLim"
    ]

    context["top_average"] = context_list
    print(context)

    context_object = [
        {
            "name": "Lee",
            "average": "0.5"
        },
        {
            "name": "Lim",
            "average": "0.6"
        },
    ]

    context["top_hitter"] = context_object

    return render(
        request,
        "landing/index.html",
        context 
    )