from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

from .models import Department, Event, News, Follow, DepartmentCoordinator
from .forms import RegisterForm, NewsForm, EventForm, DepartmentForm



def home(request):
    departments = Department.objects.all()
    selected_department = request.GET.get('department')
    events = Event.objects.all()
    news = News.objects.all()

    if selected_department:
        events = events.filter(department__id=selected_department)
        news = news.filter(department__id=selected_department)

    return render(request, 'core/home.html', {
        'departments': departments,
        'events': events,
        'news': news,
        'selected_department': selected_department
    })



@login_required
def follow_department(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    department.followers.add(request.user)
    return redirect('department_overview')

@login_required
def unfollow_department(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    department.followers.remove(request.user)
    return redirect('department_overview')



@login_required
def department_overview(request):
    departments = Department.objects.all()
    return render(request, 'core/department_overview.html', {
        'departments': departments
    })



def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'core/event_list.html', {
        'events': events
    })



@login_required
def dashboard(request):
    user = request.user
    joined_events = user.joined_events.all()
    upcoming_events = Event.objects.exclude(participants=user).order_by('date')
    followed_departments = user.followed_departments.all()  

    return render(request, 'core/dashboard.html', {
        'joined_events': joined_events,
        'upcoming_events': upcoming_events,
        'followed_departments': followed_departments  
    })




@login_required
def join_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.participants.all():
        messages.info(request, f"You already joined {event.title}.")
    else:
        event.participants.add(request.user)
        messages.success(request, f"You successfully joined {event.title}!")
    return redirect('dashboard')

@login_required
def leave_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.participants.remove(request.user)
    messages.info(request, f"You left {event.title}.")
    return redirect('dashboard')





def is_admin(user):
    return user.is_staff


@user_passes_test(is_admin)
def admin_dashboard(request):
    departments = Department.objects.all()
    events = Event.objects.all()
    news = News.objects.all()

    context = {
        'departments': departments,
        'events': events,
        'news': news,
    }

    return render(request, 'core/admin-dashboard.html', context)



@user_passes_test(is_admin)
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = DepartmentForm()

    return render(request, 'core/add_department.html', {'form': form})


@user_passes_test(is_admin)
def edit_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'core/edit_department.html', {'form': form})


@user_passes_test(is_admin)
def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    department.delete()
    return redirect('admin_dashboard')



@user_passes_test(is_admin)
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EventForm()

    return render(request, 'core/add_event.html', {'form': form})


@user_passes_test(is_admin)
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EventForm(instance=event)

    return render(request, 'core/edit_event.html', {'form': form})


@user_passes_test(is_admin)
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('admin_dashboard')



@user_passes_test(is_admin)
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.posted_by = request.user
            news.department = DepartmentCoordinator.objects.get(user=request.user).department
            news.save()
            return redirect('admin_dashboard')
    else:
        form = NewsForm()
    return render(request, 'core/add_news.html', {'form': form})



@user_passes_test(is_admin)
def edit_news(request, item_id):
    news_item = get_object_or_404(News, id=item_id)

    if request.method == 'POST':
        
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'News updated successfully!')
            return redirect('admin_dashboard') 
        else:
            print(form.errors)  
    else:
        form = NewsForm(instance=news_item)

    return render(request, 'core/edit_news.html', {'form': form})


@user_passes_test(is_admin)
def delete_news(request, item_id):
    news_item = get_object_or_404(News, id=item_id)
    news_item.delete()
    return redirect('admin_dashboard')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})



def get_followed_departments(self):
    return Department.objects.filter(followers=self)

User.add_to_class('followed_departments', property(get_followed_departments))



@login_required
def upload_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.posted_by = request.user
            news.save()
            messages.success(request, "News uploaded successfully.")
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'core/upload_news.html', {'form': form})


def is_admin(user):
    return user.is_staff  

@user_passes_test(is_admin)
def manage_department(request):
    
    departments = Department.objects.all()

    if request.method == 'POST':
        action = request.POST.get('action')
        department_id = request.POST.get('department_id')

        if action == 'delete':
            department = get_object_or_404(Department, id=department_id)
            department.delete()
            messages.success(request, "Department deleted successfully.")
            return redirect('manage_department')

        elif action == 'edit':
            
            return redirect('edit_department', department_id=department_id)

    return render(request, 'core/manage_department.html', {
        'departments': departments
    })