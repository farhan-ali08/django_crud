from django.shortcuts import render
from home.models import contactus
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    context = {
        'variable':"this"
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        lastname=request.POST.get('last')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact=contactus(name=name, lastname=lastname, email=email, password=password)
        contact.save()
        messages.success(request, '<strong>data save</strong> successfully')
        return redirect('contact')
    return render(request, 'contact.html')

def showdata(request):
    show=contactus.objects.all().order_by('-id')
    #data={
     #   'contactus' : show
    #}
    return render(request, 'showdata.html', {'contactus' : show}) #add ,data tp use key

def editdata(request, id):
    user=contactus.objects.get(id=id)
    return render(request, "editdata.html", {'user':user})
    
def updatedata(request, id):
    if request.method == 'POST':
        id=request.POST['uid']
        name=request.POST['uname']
        lastname=request.POST['ulast']
        email=request.POST['uemail']
        password=request.POST['upassword']
        con= contactus(
            id=id,
            name=name,
            lastname=lastname,
            email=email,
            password=password,
        )
        con.save()
        return redirect('index')
    return render(request, 'index.html')

def delete(request, id):
    con=contactus.objects.filter(id=id).delete()
    return redirect('contact')
