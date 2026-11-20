from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.contrib.auth.models import User
from .models import Category, Company, Job, Application


def home(request):
    job_stats = Job.objects.aggregate(total_jobs=Count('id'), avg_salary=Avg('salary'))
    application_stats = Application.objects.aggregate(total_applications=Count('id'))
    companies = Company.objects.annotate(jobs_count=Count('jobs'))
    latest_jobs = Job.objects.select_related('company', 'category').order_by('-created_at')[:6]
    return render(request, 'home.html', {'job_stats': job_stats, 'application_stats': application_stats, 'companies': companies, 'latest_jobs': latest_jobs})


def job_list(request):
    jobs = Job.objects.all().select_related('company', 'category')
    q = request.GET.get('q', '')
    category = request.GET.get('category', '')
    company = request.GET.get('company', '')
    salary_min = request.GET.get('salary_min', '')
    salary_max = request.GET.get('salary_max', '')
    no_part_time = request.GET.get('no_part_time', '')
    if q:
        jobs = jobs.filter(title__icontains=q)
    if category:
        jobs = jobs.filter(category__id=category)
    if company:
        jobs = jobs.filter(company__id=company)
    if salary_min:
        jobs = jobs.filter(salary__gte=salary_min)
    if salary_max:
        jobs = jobs.filter(salary__lte=salary_max)
    if no_part_time:
        jobs = jobs.exclude(employment_type='part_time')
    jobs = jobs.order_by('-created_at')
    categories = Category.objects.all()
    companies = Company.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs, 'categories': categories, 'companies': companies, 'q': q, 'category': category, 'company': company, 'salary_min': salary_min, 'salary_max': salary_max, 'no_part_time': no_part_time})


def job_detail(request, pk):
    job = get_object_or_404(Job.objects.select_related('company', 'category', 'created_by').prefetch_related('applications__user'), pk = pk)
    applications = job.applications.all()
    return render(request, 'job_detail.html', {'job': job, 'applications': applications})


@login_required
def create_job(request):
    if request.user.username != 'admin':
        return redirect('home')
    companies = Company.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        job = Job.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            salary = request.POST['salary'],
            location = request.POST['location'],
            employment_type = request.POST['employment_type'],
            company = Company.objects.get(id = request.POST['company']),
            category = Category.objects.get(id = request.POST['category']),
            created_by = request.user
        )
        return redirect('job_detail', pk = job.pk)
    return render(request, 'job_create.html', {'companies': companies, 'categories': categories, 'employment_types': Job.EMPLOYMENT_TYPES})


@login_required
def update_job(request, pk):
    job = get_object_or_404(Job, pk = pk)
    if job.created_by != request.user and request.user.username != 'admin':
        return redirect('job_detail', pk = pk)
    companies = Company.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.salary = request.POST.get('salary')
        job.location = request.POST.get('location')
        job.employment_type = request.POST.get('employment_type')
        job.company = Company.objects.get(id = request.POST.get('company'))
        job.category = Category.objects.get(id = request.POST.get('category'))
        job.save()
        return redirect('job_detail', pk = pk)
    return render(request, 'job_update.html', {'job': job, 'companies': companies, 'categories': categories, 'employment_types': Job.EMPLOYMENT_TYPES})


@login_required
def delete_job(request, pk):
    job = get_object_or_404(Job, pk = pk)
    if job.created_by != request.user and request.user.username != 'admin':
        return redirect('job_detail', pk = pk)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'job_delete.html', {'job': job})


@login_required
def applications(request):
    applied_jobs = request.user.applications.values_list('job__id', flat=True)
    jobs = Job.objects.select_related('company').exclude(id__in=applied_jobs)
    my_applications = request.user.applications.select_related('job', 'job__company')
    if request.method == 'POST':
        job = get_object_or_404(Job, pk = request.POST['job'])
        if job.id in applied_jobs:
            return render(request, 'applications.html', {'jobs': jobs, 'my_applications': my_applications, 'error': 'You already applied to this job'})
        Application.objects.create(
            job = job,
            user = request.user,
            cover_letter = request.POST['cover_letter']
        )
        return redirect('applications')
    return render(request, 'applications.html', {'jobs': jobs, 'my_applications': my_applications})


@login_required
def admin_panel(request):
    if request.user.username != 'admin':
        return redirect('home')
    categories = Category.objects.annotate(jobs_count=Count('jobs'))
    companies = Company.objects.annotate(jobs_count=Count('jobs'))
    jobs = Job.objects.select_related('company', 'category', 'created_by')
    applications = Application.objects.select_related('job', 'user')
    return render(request, 'admin_panel.html', {'categories': categories, 'companies': companies, 'jobs': jobs, 'applications': applications, 'statuses': Application.STATUS_CHOICES})


@login_required
def update_status(request, pk):
    if request.user.username != 'admin':
        return redirect('home')
    application = get_object_or_404(Application, pk = pk)
    if request.method == 'POST':
        application.status = request.POST.get('status')
        application.save()
    return redirect('admin_panel')


@login_required
def create_category(request):
    if request.user.username != 'admin':
        return redirect('home')
    if request.method == 'POST':
        Category.objects.create(
            name = request.POST['name']
        )
        return redirect('admin_panel')
    return render(request, 'create_category.html')


@login_required
def update_category(request, pk):
    if request.user.username != 'admin':
        return redirect('home')
    category = get_object_or_404(Category, pk = pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.save()
        return redirect('admin_panel')
    return render(request, 'update_category.html', {'category': category})


@login_required
def delete_category(request, pk):
    if request.user.username != 'admin':
        return redirect('home')
    category = get_object_or_404(Category, pk = pk)
    if request.method == 'POST':
        category.delete()
        return redirect('admin_panel')
    return render(request, 'delete.html', {'object': category})


@login_required
def create_company(request):
    if request.user.username != 'admin':
        return redirect('home')
    if request.method == 'POST':
        Company.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            website = request.POST['website']
        )
        return redirect('admin_panel')
    return render(request, 'create_company.html')


@login_required
def update_company(request, pk):
    if request.user.username != 'admin':
        return redirect('home')
    company = get_object_or_404(Company, pk = pk)
    if request.method == 'POST':
        company.name = request.POST.get('name')
        company.description = request.POST.get('description')
        company.website = request.POST.get('website')
        company.save()
        return redirect('admin_panel')
    return render(request, 'update_company.html', {'company': company})


@login_required
def delete_company(request, pk):
    if request.user.username != 'admin':
        return redirect('home')
    company = get_object_or_404(Company, pk = pk)
    if request.method == 'POST':
        company.delete()
        return redirect('admin_panel')
    return render(request, 'delete.html', {'object': company})


@login_required
def create_application(request):
    if request.user.username != 'admin':
        return redirect('home')
    jobs = Job.objects.all()
    users = User.objects.all()
    if request.method == 'POST':
        Application.objects.create(
            job = Job.objects.get(id = request.POST['job']),
            user = User.objects.get(id = request.POST['user']),
            cover_letter = request.POST['cover_letter'],
            status = request.POST['status']
        )
        return redirect('admin_panel')
    return render(request, 'create_application.html', {'jobs': jobs, 'users': users, 'statuses': Application.STATUS_CHOICES})


@login_required
def update_application(request, pk):
    if request.user.username != 'admin':
        return redirect('home')
    application = get_object_or_404(Application, pk = pk)
    jobs = Job.objects.all()
    users = User.objects.all()
    if request.method == 'POST':
        application.job = Job.objects.get(id = request.POST.get('job'))
        application.user = User.objects.get(id = request.POST.get('user'))
        application.cover_letter = request.POST.get('cover_letter')
        application.status = request.POST.get('status')
        application.save()
        return redirect('admin_panel')
    return render(request, 'update_application.html', {'application': application, 'jobs': jobs, 'users': users, 'statuses': Application.STATUS_CHOICES})


@login_required
def delete_application(request, pk):
    if request.user.username != 'admin':
        return redirect('home')
    application = get_object_or_404(Application, pk = pk)
    if request.method == 'POST':
        application.delete()
        return redirect('admin_panel')
    return render(request, 'delete.html', {'object': application})
