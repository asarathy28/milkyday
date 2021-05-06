from django.shortcuts import render, redirect
from .milky_spotify import Music
from .forms import ContactForm
from .forms import OrderForm
from .models import MerchItem
from .models import MerchFeature
from .models import HomeSettings
from .models import PortfolioSettings
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages #import messages
import requests


# Create your views here.
def home(request):
    h_settings = HomeSettings.objects.first()
    myMusic = Music()

    new_single = {'name':myMusic.ns_name, 'image':myMusic.ns_image, 'id':myMusic.ns_id}
    playlists = zip(myMusic.pl_name, myMusic.pl_id, myMusic.pl_image)

    return render(request, "main/home.html", {'new_single':new_single, 'playlists':playlists, 's':h_settings})

def music(request):
    myMusic = Music()
    #'1216336460'

    #playlists = {'name':myMusic.pl_name, 'id':myMusic.pl_id, 'image':myMusic.pl_image}
    albums = zip(myMusic.album_name, myMusic.album_id, myMusic.album_image)

    return render(request, "main/music.html", {'albums':albums})

def portfolio(request):
    p_settings = PortfolioSettings.objects.first()
    form = ContactForm()

    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            ''' reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,'response': recaptcha_response}
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            print(result)

            if result['success']:
                name = request.POST['name']
                subject = request.POST['subject']
                message = request.POST['message']
                email =request.POST['email']


                context = {'subject':subject, 'message':message, 'name':name, 'email':email}
                template = render_to_string('main/email-temp.html', context)

                send_mail(f'{name} : {subject}', message, settings.EMAIL_HOST_USER, ['milkyday.mgmt@gmail.com'], fail_silently=False)

                form.save()
                messages.success(request, "Message sent." )
                return redirect('../home/')
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

        messages.error(request, "Error. Message not sent.")
    else:  # 5
        # Create an empty form instance
        form = ContactForm()

    context = {'form':form, 'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY, 's':p_settings}

    return render(request, "main/portfolio.html", context)

def merch(request):
    items = MerchItem.objects.all()
    feature = MerchFeature.objects.first()
    form = OrderForm()

    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            ''' reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,'response': recaptcha_response}
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            print(result)

            if result['success']:
                name = request.POST['name']
                item = request.POST['item']
                email =request.POST['email']
                quanity = request.POST['quanity']


                context = {'name':name, 'item':item, 'quanity':quanity, 'email':email, 'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY}
                template = render_to_string('main/order_temp.html', context)

                send_mail(f'{name} : ordering {item}', template, settings.EMAIL_HOST_USER, ['milkyday.mgmt@gmail.com'], fail_silently=False)

                form.save()
                messages.success(request, "Message sent." )
                return redirect('../home/')
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

        messages.error(request, "Error. Message not sent.")
    else:  # 5
        # Create an empty form instance
        form = OrderForm()

    context = {'form':form, 'items':items, 'f':feature, 'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY}

    return render(request, "main/merch.html", context)
