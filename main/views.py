from django.shortcuts import render, redirect
from .milky_spotify import Music
from .forms import ContactForm
from .models import MerchItem
from .models import MerchFeature
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def home(request):

    myMusic = Music()

    new_single = {'name':myMusic.ns_name, 'image':myMusic.ns_image}
    playlists = zip(myMusic.pl_name, myMusic.pl_id, myMusic.pl_image)

    return render(request, "main/home.html", {'new_single':new_single, 'playlists':playlists})

def music(request):
    myMusic = Music()
    #'1216336460'

    #playlists = {'name':myMusic.pl_name, 'id':myMusic.pl_id, 'image':myMusic.pl_image}
    albums = zip(myMusic.album_name, myMusic.album_id, myMusic.album_image)

    return render(request, "main/music.html", {'albums':albums})

def portfolio(request):

    form = ContactForm()

    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():

            name = request.POST['name']
            subject = request.POST['subject']
            message = request.POST['message']
            email =request.POST['email']


            context = {'subject':subject, 'message':message, 'name':name, 'email':email}
            template = render_to_string('main/email-temp.html', context)

            send_mail(f'{name} : {subject}', message, settings.EMAIL_HOST_USER, ['milkyday99@gmail.com'], fail_silently=False)

            form.save()

            return redirect('../home/')
    else:  # 5
        # Create an empty form instance
        form = ContactForm()

    context = {'form':form}

    return render(request, "main/portfolio.html", context)

def merch(request):
    items = MerchItem.objects.all()
    feature = MerchFeature.objects.first()

    return render(request, "main/merch.html", {'items':items, 'f':feature})

def checkout(request):
    return render(request, "main/checkout-base.html", {})
