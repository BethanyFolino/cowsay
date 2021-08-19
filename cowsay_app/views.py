from django.shortcuts import render
from cowsay_app.models import WhatDoesTheCowSay
from cowsay_app.forms import WhatDoesTheCowSayForm

import subprocess

# Create your views here.
def index_view(request):
    if request.method == "POST":
        form = WhatDoesTheCowSayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cowsays = WhatDoesTheCowSay.objects.create(
                text=data['text']
            )
            sub = subprocess.run(f'cowsay "{cowsays}"', capture_output=True, shell=True).stdout.decode('utf-8').strip()
            form = WhatDoesTheCowSayForm()
            return render(request, 'index.html', {'form': form, 'subprocess': sub})
    form = WhatDoesTheCowSayForm()
    return render(request, 'index.html', {'form': form})

def most_recent(request):
    topten = WhatDoesTheCowSay.objects.all().order_by('-id')[:10]
    return render(request, 'most_recent.html', {'toptens': topten})