from django.shortcuts import render


# Create your views here.
def home_screen_view(request):
   # print(request.headers)
  #  return render(request,"personal/home.html",{})
    context = {}
    context['some_string'] = "this is some string that i'm passing to the view"
    return render(request,"base.html",{})

def boot_temp(request):
  return render(request,"E:\DjangoProject\demo3\vir\src\templates\material-kit-master\index.html",[])    