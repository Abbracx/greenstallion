from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from .models import user_create



# Create your views here.

def profile (request):
    return render(request, 'user/profile.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def client(request):
    context = {'message':"Hello client"} 
    render(request,'client.html', context)

def register(request):
    if request.method == "POST":
        title = request.POST.get('title', "")
        first_name = request.POST.get('first_name', "")
        last_name = request.POST.get('last_name', "")
        gender = request.POST.get('gender', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        phone = request.POST.get('phone', "")
        status = request.POST.get('status', "")
        dob = request.POST.get('dob',)
        identification = request.POST.get('identification', "")
        category = request.POST.get('category', "")
        username = request.POST.get('username', "")
        password1 = request.POST.get('password1', "")
        password2 = request.POST.get('password2', "")
        checkbox = request.POST.get('checkbox', False)
        role = request.POST.get('role',default= 'CL')

        #import  pdb; pdb.set_trace()

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username Taken')
                return redirect('accounts')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('accounts')
            else:
                user_obj = User.objects.create_user(username=username, password=password1, first_name=first_name, 
                last_name=last_name, email=email, birth_date = dob,  category= category, role = role)
                
                user = Profile.objects.create(title=title, user = user_obj, gender=gender, address=address, city=city, phone=phone, status=status,
                identification=identification, password2=password2, checkbox =checkbox)
                user.save();
                print('user created')
                return redirect('/')

        else:
            messages.info(request, 'Password not matching...')
            return redirect('register')
        #return render(request, 'client.html')
    else:
        return render(request, 'accounts.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            next_url = request.GET.get ('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return redirect('dashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')





def dashboard(request):
    return render(request, 'dashboard.html')

#users part starts here


def view_users(request):
    all_users = User.objects.all
    return render(request, 'user/data.html', {"all_users": all_users})

def manage_user_roles(request):
    return render(request, 'user/role/data.html')

def user_creation(request):
    if request.method == "POST":
        title = request.POST.get('title', "")
        first_name = request.POST.get('first_name', "")
        last_name = request.POST.get('last_name', "")
        gender = request.POST.get('gender', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        phone = request.POST.get('phone', "")
        status = request.POST.get('status', "")
        birth_date = request.POST.get('birth_date', )
        identification = request.POST.get('identification', "")
        category = request.POST.get('category', "")
        username = request.POST.get('username', "")
        password1 = request.POST.get('password1', "")
        password2 = request.POST.get('password2', "")
        role = request.POST.get('role', "")
        note = request.POST.get('note',"")

        # import  pdb; pdb.set_trace()

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username Taken')
                return redirect('user_creation')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('user_creation')
            else:
                user = user_create.objects.create(title=title, first_name=first_name, last_name=last_name, gender=gender,
                                               email=email, address=address, city=city, phone=phone, status=status,
                                               birth_date=birth_date, identification=identification,
                                               category=category, username=username, password1=password1,
                                               password2=password2, role=role, note=note)
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                                last_name=last_name, birth_date=birth_date, email=email, role=role, category = category)
                user.save();
                print('user created')
                return redirect('user_creation')

        else:
            messages.info(request, 'Password not matching...')
            return redirect('user_creation')
        return render(request, 'user/create.html')
    else:
        return render(request, 'user/create.html')

#

#reports part starts here

def report_borrower(request):
    return render(request, 'report/borrower_report.html')

def report_loan(request):
    return render(request, 'report/loan_report.html')

def report_company(request):
    return render(request, 'report/company_report.html')


#this is the settings part

def settings(request):
    return render(request, 'setting/data.html')


#the repayment part starts here

def repayments(request):
    return render(request, 'repayment/data.html')

def repayment_create(request):
    return render(request, 'repayment/create.html')





