from django.shortcuts import get_object_or_404,render,HttpResponseRedirect,redirect
from .forms import UserForm
from .models import User
# Create your views here.
# This function will add new  item and show item list
def addshow(request):
    stud = User.objects.all()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            #form.save()
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            pw=form.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            form = UserForm()
    else:
        form = UserForm()
        #stud=User.objects.all()
    return render(request,'templates/addandshow.html',{'form':form,'stu':stud})

# This function will update the data
def update_data(request,id):
    pi = get_object_or_404(User, pk=id)
    if request.method=='POST':
        #pi=User.objects.get(pk=id)
        fm=UserForm(request.POST,instance=pi)#,instance=pi
        if fm.is_valid():
            fm.save()
            return redirect('addshow')

    else:
       # pi=User.objects.get(pk=id)
        fm=UserForm(instance=pi)#instance=pi
    return render(request,'templates/update.html',{'form':fm,})


# This function will delete
def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


