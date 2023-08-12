from django.contrib import admin
from .models import ContactMessage,ContactInformation,Serivieinfo,whychoose,CarouselItem,Indexser,Abt_us,Abt_us1,meetteam
admin.site.register(meetteam)
admin.site.register(Abt_us1)
admin.site.register(Abt_us)
admin.site.register(Indexser)
admin.site.register(CarouselItem)
admin.site.register(whychoose)
admin.site.register(Serivieinfo)
admin.site.register(ContactInformation)
admin.site.register(ContactMessage)