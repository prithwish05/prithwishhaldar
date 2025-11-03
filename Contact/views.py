from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

# Create your views here.
def contact(request):
    if request.method=='POST':
        form=ContactForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form=ContactForm(initial={'host':request.user})

    return render(request,'contact.html',{'form':form})
