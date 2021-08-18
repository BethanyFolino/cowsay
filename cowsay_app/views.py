from django.shortcuts import render, HttpResponseRedirect, reverse
from cowsay_app.models import WhatDoesTheCowSay
from cowsay_app.forms import WhatDoesTheCowSayForm

# Create your views here.
def index_view(request):
    if request.method == "POST":
        form = WhatDoesTheCowSayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cowsays = WhatDoesTheCowSay.objects.create(
                text=data['text']
            )
            return HttpResponseRedirect(reverse('home'))
    text = WhatDoesTheCowSay.objects.latest()
    return render(request, 'index.html', {'form': form})

def most_recent(request):
    topten = WhatDoesTheCowSay.objects.order_by('id')[:10]
    return render(request, 'most_recent.html', {'topten': topten})