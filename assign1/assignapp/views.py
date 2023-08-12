from django.shortcuts import render
from .models import ContactMessage,ContactInformation,Serivieinfo,whychoose,CarouselItem,Indexser,Abt_us,Abt_us1,meetteam
# Create your views here.
def home(request): 
   abt=Abt_us.objects.all().first()
   info = ContactInformation.objects.all().first()
   carousel_items = CarouselItem.objects.all()
   index_ser=Indexser.objects.all()
   meet = meetteam.objects.all()
   return render(request, 'index.html',{'carousel_items': carousel_items,'index_ser':index_ser,'meet':meet,'abt':abt,'info':info})
def about_Us(request):
   info = ContactInformation.objects.all().first()
   why=whychoose.objects.all()
   abt=Abt_us.objects.all().first()
   abt1=Abt_us1.objects.all()
   return render(request, 'about_us.html',{'why_data':why,'abt':abt,'abt1':abt1,'info':info})

def services(request):
   abt=Abt_us.objects.all().first()
   info = ContactInformation.objects.all().first()
   
   ser = Serivieinfo.objects.all()
   why=whychoose.objects.all()
   return render(request, 'services.html',{'ser_data':ser,'why_data':why,'abt':abt,'info':info})
def Blog(request):
   info = ContactInformation.objects.all().first()
   return render(request, 'blog.html',{'info':info})
def Contact_us(request):   
   abt=Abt_us.objects.all().first()
   info = ContactInformation.objects.all().first()
   if request.method == 'POST':    
      name1  = request.POST.get('name')
      email1  = request.POST.get('email')
      phone1 = request.POST.get('phone')
      subject1  = request.POST.get('subject')
      message1  = request.POST.get('message')     
      contact = ContactMessage()     
      contact.name = name1
      contact.email = email1
      contact.phone=phone1
      contact.subject = subject1
      contact.message =message1     
      contact.save()   
   else:
      pass
   return render(request,'contact_us.html',{'abt':abt,'info':info}) 