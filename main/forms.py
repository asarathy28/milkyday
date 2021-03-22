from django.forms import ModelForm
from .models import ContactMessage
from .models import MerchOrder

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__' #['subject', 'sender_name', 'email', 'message', 'sent_date']

class OrderForm(ModelForm):
    class Meta:
        model = MerchOrder
        fields = '__all__'
