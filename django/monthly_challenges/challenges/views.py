from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django!",
    "april": "Do 10 push-ups every day!",
    "may": "Stay hydrated and sleep well!",
    "june": "Exercise regularly!",
    "july": "Listen to your body and eat nutritious food!",
    "august": "Create a healthy diet!",
    "september": "Get enough sleep!",
    "october": "Eat a balanced diet!",
    "november": "Stay motivated and achieve your goals!",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(
        request,
        "challenges/index.html",
        {
            "months": months,
        },
    )


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is not supported!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:

        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {
                "text": challenge_text,
                "month_name": month,
            },
        )

    except:
        raise Http404()
