from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.http import FileResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.utils import timezone
from .models import Project

# Create your views here.
def index(request):
    context = {
        "variable":"Jadhav Brothers"
    }
    #messages.success(request, "This is a text message")
    return render(request, 'index.html',context)
    #return HttpResponse("This is homepage")

def about(request):
    context = {
        'title': 'About Us',
        'developer_name': 'Omkar Jadhav',
        'bio': 'I am a full-stack web developer with 1+ years of experience...',
        'skills': ['Django', 'Python','Java','AI/ML' 'React', 'JavaScript', 'PostgreSQL','MongoDB'],
        'experience_years': 1,
        'projects_count': 20,
        'now': timezone.now(),
    }
    return render(request, 'about.html',context)
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")

def webdev(request):
    return render(request, 'Services/webdev.html')
    #return HttpResponse("This is services page")

def mobileapp(request):
    return render(request, 'Services/mobileapp.html')
    #return HttpResponse("This is services page")

def design(request):
    return render(request, 'Services/design.html')
    #return HttpResponse("This is services page")

def mobile_projects(request):
    projects = Project.objects.all()
    return render(request, 'mobile_projects.html', {'projects': projects})

def start_payment(request, project_id):
    # In real case, integrate Razorpay/Stripe
    # After successful payment, redirect:
    return redirect('download_pdf', project_id=project_id)

def download_pdf(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if not project.is_paid:
        return redirect(project.github_url)

    if project.pdf_file:
        return FileResponse(project.pdf_file.open('rb'), as_attachment=True, filename=project.pdf_file.name)
    return HttpResponse("PDF not found.", status=404)


def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact= Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent successfully...")
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")