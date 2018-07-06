from django.shortcuts import render

# Create your views here.

def team_site(request):
    return render(request, 'website/team.html')