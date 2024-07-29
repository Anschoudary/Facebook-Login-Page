from django.shortcuts import render
from .models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = User(email= email, password= password)
        data.save()
        return render(request, template_name='index.html')
    else:
        return render(request, template_name='index.html')
    
    return render(request, template_name='index.html')
    
def users(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})