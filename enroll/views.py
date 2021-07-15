from enroll.models import Students
from django.shortcuts import redirect, render
from .models import Students


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        reg = Students(name = username , email = email , password = password)
        reg.save()
    else:
        username = ''
        email = ''
        password = ''

    students = Students.objects.all()
    return render(request , 'home.html', {'students':students})


def delete(request , pk):
    reg = Students.objects.get(id= pk)
    reg.delete()
    return redirect('/')

def edit(request , pk):
    rec = Students.objects.get(id = pk)
    nm = rec.name
    em = rec.email
    ps = rec.password
    Id = rec.id
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rec = Students(id=Id,  name = username , email = email , password = password )
        rec.save()
    else:
        username = ''
        email = ''
        password = ''

    return render(request , 'edit.html' , {'name':nm , 'email':em , 'password':ps , 'id':Id})