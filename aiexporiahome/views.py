from django.shortcuts import render 
from django.http import JsonResponse
from aiexporia import templates
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.db.models import Q



from aiexporiahome.models import AI,blog,indianAI
# def display(request):
#     return render(request,"index.html")

def like_ai(request, ai_name):
    ai = get_object_or_404(AI, name=ai_name)
    ai.likes += 1
    ai.save()
    return JsonResponse({'likes': ai.likes})
def form(request):
    return render(request,"form.html")
def uploadAI(request):
  if request.method=="POST":
    name=request.POST.get("name")
    image=request.FILES.get("image")
    description=request.POST.get("description")
    url=request.POST.get("trade_url")
    category=request.POST.get("category")
    formsubmit=AI(name =name,image=image,description=description,url=url,category=category)
    formsubmit.save()
    return HttpResponse("form submitted successfully")
def display(request):
    displayAI=AI.objects.all()
  
    paginator=Paginator(displayAI,30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
    return render(request,'index.html',{'page_obj': page_obj}) 

# def blo(request):
#     return render(request,"blo.html")

def blo(request):
    displayblogs=blog.objects.all()

    paginator=Paginator(displayblogs,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
    return render(request,'blo.html',{'page_obj': page_obj}) 

def displayin(request):
    displayinAI=indianAI.objects.all()
    
    paginator=Paginator(displayinAI,30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
    return render(request,'indian.html',{'page_obj': page_obj}) 
def searchresults(request):
    if request.method=='GET':
      query=request.GET.get("search")
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query))
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'index.html',{'page_obj': page_obj}) 
def searchres(request):
     if request.method=='GET':
      query=request.GET.get("searches")
      displayinAI=indianAI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query))
      paginator=Paginator(displayinAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'indian.html',{'page_obj': page_obj}) 
def searchresultsss(request):
       if request.method=='GET':
         query=request.GET.get("searchsss")
         displayblogs=blog.objects.filter(Q(title__icontains=query)|Q(descrip__icontains=query))
         paginator=Paginator(displayblogs,1)
         page_number = request.GET.get('page')
         page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
         return render(request,'blo.html',{'page_obj': page_obj}) 
