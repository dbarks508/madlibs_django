from django.shortcuts import render
from django.http import HttpResponse
from .forms import word_form
from .models import madlib_model

def madlibs_view(request):
    if request.method == "POST":
        form = word_form(request.POST)
        if form.is_valid():
            words = form.cleaned_data                  # dictionary of words passed in from form submission
            madlib = madlib_model.random_template()    # get a random madlib template
            completed = madlib.fill_template(words)    # use the class method to fill the template with words
            context = {"madlib": madlib, "completed": completed}
            return render(request, "madlibs/completed.html", context)
    else:
        form = word_form()   
    
    return render(request, "madlibs/madlibsform.html", {"form": form, })
