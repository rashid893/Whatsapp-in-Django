from django.http.request import HttpRequest
from django.shortcuts import render,HttpResponse

# # Create your views here.
def index(request):
     return render(request,"index.html")
def senddata(request):
  if request.method =="POST":
    num=request.POST['number']
    msg=request.POST['message']
    print(num)
    print(msg)
    info="Message Sent has been Successfuly"
    return render(request,'index.html',{'info':info})
  else:
    return HttpResponse('404')
  
    
