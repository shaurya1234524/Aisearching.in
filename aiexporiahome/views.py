from django.shortcuts import render 
from django.http import JsonResponse
from aiexporia import templates
from django.core.paginator import Paginator
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.db.models import Q

from aiexporiahome.models import  AIToolAdvantage,AIToolDisadvantage,AIToolRating,LikedAI

from aiexporiahome.models import AI,blog,indianAI
def ad(request):
    return render(request,'ads.txt')
def robots_txt(request):
    context = {
        "allow_indexing": True,  # Change based on your logic
        "sitemap_url": "https://www.aisearchlibrary/sitemap.xml",
    }
    return render(request, "robots.txt", context, content_type="text/plain")
@csrf_exempt
def sitemap(request):
    return render(request,'sitemap.xml')

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
    displayAI=AI.objects.all().order_by('-like_count') 
  
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
    displayinAI=indianAI.objects.all().order_by('-like_count') 
    
    paginator=Paginator(displayinAI,30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
    return render(request,'indian.html',{'page_obj': page_obj}) 
def searchresults(request):
    if request.method=='GET':
      query=request.GET.get("search")
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'index.html',{'page_obj': page_obj}) 
def searchres(request):
     if request.method=='GET':
      query=request.GET.get("searches")
      displayinAI=indianAI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
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

def code(request):
    if request.method=='GET':
      query="coding"
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'Coding.html',{'page_obj': page_obj}) 
def NewAi(request):
    if request.method=='GET':
      query="new Ai"
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'NewAI.html',{'page_obj': page_obj}) 
def Imagegen(request):
    if request.method=='GET':
      query="Image"
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'ImageGenerate.html',{'page_obj': page_obj}) 
def MusicsAi(request):
    if request.method=='GET':
      query="Music"
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'Music.html',{'page_obj': page_obj}) 
      
def VideoGeneration(request):
    if request.method=='GET':
      query="Video"
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'VideoGeneration.html',{'page_obj': page_obj}) 

def Study(request):
    if request.method=='GET':
      query="Study"
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'StudyAi.html',{'page_obj': page_obj}) 
def chatbot(request):
    if request.method=='GET':
      query="chatbot"
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'Chatbot.html',{'page_obj': page_obj}) 
def buisnesses(request):
    if request.method=='GET':
      query="business"
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'Chatbot.html',{'page_obj': page_obj}) 
def HomeworkAi(request):
    if request.method=='GET':
      query="homework"
      displayAI=AI.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__icontains=query)).order_by('-like_count') 
      paginator=Paginator(displayAI,30)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
    # context={'displayAI':displayAI}
      return render(request,'Homework.html',{'page_obj': page_obj})

def form(request):
    return render(request,"form.html")


def like_ai(request, ai_id):
    tool = get_object_or_404(AI, id=ai_id)

    # Get liked tools from session
    liked_tools = request.session.get('liked_tools', [])

    # Prevent duplicate likes
    if ai_id in liked_tools:
        return JsonResponse({'error': 'Already liked'}, status=400)

    # Increase like count
    tool.like_count += 1
    tool.save()

    # Store the liked tool ID in session
    liked_tools.append(ai_id)
    request.session['liked_tools'] = liked_tools

    return JsonResponse({'likes': tool.like_count})


