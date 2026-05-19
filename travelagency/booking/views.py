from django.shortcuts import render,redirect
from .models import TravelPackage,Booking
from django.contrib.auth.decorators import login_required

# Create your views here.
def package_list(request):
    packages = TravelPackage.objects.all()

    return render(request,'package_list.html',{'packages': packages})

@login_required
def book_package(request,package_id):
    package = TravelPackage.objects.get(id=package_id)
    if package.available_slots > 0:
        Booking.objects.create(user=request.user,package=package)
        package.available_slots -= 1
        package.save()

        return redirect('book_package')
    else:
        # FIX: render() must have template_name as 2nd argument
        return render(request, 'error.html', {'message': 'No slots available'})