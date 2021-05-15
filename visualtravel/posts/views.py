from django.shortcuts import render
from datetime import datetime
from . import models

def all_posts(request):
    now = datetime.now()
    hungry = True
    return render(request, "all_posts.html", context={"now": now, "hungry": hungry})

