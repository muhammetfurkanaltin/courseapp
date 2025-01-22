from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return redirect(request, "account/login.html",{ "error":"Bu sayfayı görüntülemek için admin girişi yapmalısınız"})
    
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')


            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Giriş Başarılı')
                nextURL = request.GET.get("next",None)
                if nextURL is None:
                    return redirect("index")
                else:
                    return redirect(nextURL)
            else:
                return render(request, 'account/login.html', {'form': form })
        else:
            return render(request, 'account/login.html', {'form': form })
    else:
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form })

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password != repassword:
            return render(request, 'account/register.html', {'error':'parola eşlesmiyor',"username":username,"email":email})
        
        if User.objects.filter(username = username).exists():
            return render(request, 'account/register.html', {'error':'Bu kullanıcı adı daha önce alınmış',"username":username,"email":email})
        
        if User.objects.filter(email = email).exists():
            return render(request, 'account/register.html', {'error':'Bu email daha önce alınmış',"username":username,"email":email})
            
        user = User.objects.create_user(username=username,email=email ,password=password)
        user.save()
        return redirect("user_login")
    else:
        return render(request, 'account/register.html')

def user_logout(request):
    messages.add_message(request, messages.SUCCESS, 'çıkıs Başarılı')
    logout(request)
    return redirect("index")
