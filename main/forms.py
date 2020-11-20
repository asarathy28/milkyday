from django.forms import ModelForm
from .models import ContactMessage

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__' #['subject', 'sender_name', 'email', 'message', 'sent_date']
