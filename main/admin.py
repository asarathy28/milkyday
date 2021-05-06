from django.contrib import admin
from .models import ContactMessage
from .models import MerchItem
from .models import MerchFeature
from .models import MerchOrder
from .models import HomeSettings
from .models import PortfolioSettings

admin.site.register(ContactMessage)
admin.site.register(MerchItem)
admin.site.register(MerchFeature)
admin.site.register(MerchOrder)
admin.site.register(HomeSettings)
admin.site.register(PortfolioSettings)
