from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.shortcuts import (
    redirect,
    render,
)
from django.contrib.auth.decorators import login_required

from .forms import (
    CustomLoginForm,
    RegisterForm
)
from .decorators import only_authenticated_user, redirect_authenticated_user, group_required
from apps.users.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import Group


@only_authenticated_user
def home_view(request):
    return redirect('/hits/')


@redirect_authenticated_user
def login_view(request):
    error = None
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email'].split("@")
            user = authenticate(
                request,
                username=username[0],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('/hits/')
            else:
                error = 'Invalid Credentials'
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form, 'error': error})


@only_authenticated_user
@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


@redirect_authenticated_user
def registeration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            description = form.cleaned_data['description']
            email = form.cleaned_data['email']
            username = email.split("@")
            username = username[0]
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            user = User.objects.create_user(
                name=name,
                username=username,
                description=description,
                email=email
            )
            user.set_password(password)
            user.save()
            hitmen_group = Group.objects.get(name="Hitmen")
            hitmen_group.user_set.add(user.pk)
            messages.success(request, 'Hitmen creado!')
            return redirect("users:login")
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@only_authenticated_user
@group_required('Manager', 'Boss',raise_exception=True)
def hitmen_view(request):
    user_type_manager = request.user.groups.all()[0].name == "Manager"
    user_type_boss = request.user.groups.all()[0].name == "Boss"

    if user_type_manager:
        list_user_manager = list(User.objects.filter(manager=request.user).values_list("pk", flat=True))
    elif user_type_boss:
        list_user_manager = User.objects.all()
    paginator = Paginator(list_user_manager, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/hitmen.html', {'page_obj': page_obj})


@only_authenticated_user
def hitmen_inactive(request, pk):
    hitmen = User.objects.get(pk=pk)
    hitmen.inactive()
    hitmen.save()
    return redirect('/hitmen/')


@only_authenticated_user
@group_required('Boss',raise_exception=True)
def asign_hitman_to_manager(request):
    print("Aca")
    if request.method == 'POST':
        print("Aca")
        hitman_toasign = request.POST['hitman_toasign']
        manager = request.POST['manager']
        manager = User.objects.get(pk=manager)
        User.objects.filter(pk=hitman_toasign).update(manager=manager)
        messages.success(request, 'Hitman asignado correctamente!')
    url = '/hitmen/' + str(manager.pk)
    return redirect(url)


@only_authenticated_user
@group_required('Manager', 'Boss',raise_exception=True)
def hitmen_detail(request, pk):
    hitmen = User.objects.get(pk=pk)
    users_manager = User.objects.filter(manager=hitmen)
    hitmans = User.objects.filter().exclude(pk=request.user.pk)
    return render(request, 'users/hitmen_detail.html', {'hitmen': hitmen, 'manager': users_manager, "hitmans":hitmans})
