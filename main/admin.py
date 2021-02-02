from django.contrib import admin
from .models import ContactMessage
from .models import MerchItem
from .models import MerchOrder

admin.site.register(ContactMessage)
admin.site.register(MerchItem)
admin.site.register(MerchOrder)
