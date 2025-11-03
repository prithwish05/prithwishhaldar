from django.shortcuts import render
from django.db import OperationalError
from .models import Skills


# Create your views here.
def home(request):
    """Render homepage. If the Skills table/columns aren't migrated yet,
    avoid crashing by returning an empty skills list so the page still loads.
    """
    try:
        # force evaluation to trigger DB access inside try/except
        skills_qs = Skills.objects.all()
        skills = list(skills_qs)
    except OperationalError:
        skills = []

    # Split into two columns dynamically
    half = len(skills) // 2 + len(skills) % 2
    left_skills = skills[:half]
    right_skills = skills[half:]

    return render(request, 'home.html', {
        'skills': skills,
        'left_skills': left_skills,
        'right_skills': right_skills,
    })

