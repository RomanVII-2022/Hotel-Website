from django.shortcuts import render, redirect
from .models import Image, Reservation, Contact
from .forms import ReservationForm

# Create your views here.
def homeview(request):
    return render(request, 'home.html')


def aboutview(request):
    return render(request, "about.html")


def galleryview(request):
    images = Image.objects.all().order_by("-created_at")
    return render(request, 'gallery.html', {'images':images})


def addimageview(request):
    if request.method == "POST":
        image = request.FILES["filename"]
        save_data = Image(image=image)
        save_data.save()
        return redirect('gallery')
    return render(request, "addimage.html")


def deleteview(request, image_id):
    image = Image.objects.get(pk=image_id)
    image.delete()
    return redirect('gallery')


def menuview(request):
    return render(request, "menu.html")


def reservationview(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation')
    else:
        form = ReservationForm()
    
    return render(request, "reservation.html", {"form":form})


def contactview(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        save_data = Contact(name=name, email=email, subject=subject, message=message)
        save_data.save()
        return redirect('contact')
        
    return render(request, "contact.html")



