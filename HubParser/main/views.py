from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Hub
from .forms import HubForm
from .sync_hubs_with_db import sync_hubs


def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def index(request):
    sync_hubs()
    hubs = Hub.objects.all()
    return render(request, 'main/index.html', {'hubs': hubs})

@login_required
@user_passes_test(is_admin)
def add_hub(request):
    if request.method == 'POST':
        form = HubForm(request.POST)
        if form.is_valid():
            form.save()
            sync_hubs()
            return redirect('index')
    else:
        form = HubForm()
    return render(request, 'main/add_hub.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_hub(request, hub_id):
    hub = get_object_or_404(Hub, id=hub_id)
    if request.method == 'POST':
        form = HubForm(request.POST, instance=hub)
        if form.is_valid():
            form.save()
            sync_hubs()
            return redirect('index')
    else:
        form = HubForm(instance=hub)
    return render(request, 'main/edit_hub.html', {'form': form, 'hub': hub})

@login_required
@user_passes_test(is_admin)
def delete_hub(request, hub_id):
    hub = get_object_or_404(Hub, id=hub_id)
    if request.method == 'POST':
        hub.delete()
        sync_hubs()
        return redirect('index')
    return render(request, 'main/delete_hub.html', {'hub': hub})