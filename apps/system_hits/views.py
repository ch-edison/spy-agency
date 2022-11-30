from apps.users.decorators import only_authenticated_user, group_required
from apps.system_hits.models import Hit
from django.core.paginator import Paginator
from .forms import HitForm
from apps.users.models import User
from django.shortcuts import (
    redirect,
    render,
)
from django.contrib import messages


@only_authenticated_user
def hits_view(request):
    form = HitForm(user=request.user)
    user_type_hitmen = request.user.groups.all()[0].name == "Hitmen"
    user_type_manager = request.user.groups.all()[0].name == "Manager"
    user_type_boss = request.user.groups.all()[0].name == "Boss"

    if user_type_hitmen:
        list_hit = Hit.objects.filter(assigned_to=request.user)
    elif user_type_manager:
        list_user_manager = list(User.objects.filter(manager=request.user).values_list("pk", flat=True))
        list_user_manager.append(request.user.pk)
        list_hit = Hit.objects.filter(assigned_to__pk__in=list_user_manager)
    elif user_type_boss:
        list_hit = Hit.objects.all()
    paginator = Paginator(list_hit, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'hits.html', {'page_obj': page_obj, "form": form})


@only_authenticated_user
@group_required('Manager', 'Boss',raise_exception=True)
def hit_create_view(request):
    error = None
    if request.method == 'POST':
        form = HitForm(request.POST, user=request.user)
        if form.is_valid():
            objetive_name = form.cleaned_data['objetive_name']
            description = form.cleaned_data['description']
            assigned_to = form.cleaned_data['assigned_to']
            user_assigned_to = User.objects.get(username=assigned_to)
            user_created_by = User.objects.get(username=request.user)
            Hit.objects.create(
                objetive_name=objetive_name,
                description=description,
                assigned_to=user_assigned_to,
                created_by=user_created_by
            )
            messages.success(request, 'Hit creado!')
            return redirect('/hits/')
    else:
        form = HitForm(user=request.user)
    return render(request, 'hits_create.html', {'form': form, 'error': error})

@only_authenticated_user
def hit_update_failed(request, pk):
    hit = Hit.objects.get(pk=pk)
    hit.failed()
    hit.save()
    messages.success(request, 'Hit actualizado!')
    return redirect('/hits/')

@only_authenticated_user
def hit_update_completed(request,pk):
    hit = Hit.objects.get(pk=pk)
    hit.completed()
    hit.save()
    messages.success(request, 'Hit actualizado!')
    return redirect('/hits/')

@only_authenticated_user
def hits_detail(request, pk):
    hit = Hit.objects.get(pk=pk)
    return render(request, 'hits_detail.html', {'hit': hit})


@only_authenticated_user
@group_required('Manager', 'Boss',raise_exception=True)
def hits_reasign(request):
    form = HitForm(user=request.user)
    user_type_manager = request.user.groups.all()[0].name == "Manager"
    user_type_boss = request.user.groups.all()[0].name == "Boss"
    if user_type_manager:
        list_user_manager = list(User.objects.filter(manager=request.user).values_list("pk", flat=True))
        list_user_manager.append(request.user.pk)
        list_hit = Hit.objects.filter(assigned_to__pk__in=list_user_manager)
    elif user_type_boss:
        list_hit = Hit.objects.all()
    paginator = Paginator(list_hit, 10)  # Show 25 contacts per page.
    user_assigned = User.objects.filter().exclude(pk=request.user.pk)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        list_hit = request.POST.getlist('hit_checkboxes')
        assigned_to = request.POST['assigned_to']
        print(list_hit,assigned_to)
        for h in list_hit:
            assigned = User.objects.get(pk=assigned_to)
            Hit.objects.filter(pk=h).update(assigned_to=assigned)
    return render(request, 'reassign_hits.html', {'page_obj': page_obj, "form": form, "assigned":user_assigned})


def page_notfound(request, exception):
    return render(request, "404.html", {})


def page_permission_denied(request, exception):
    return render(request, "403.html", {})
