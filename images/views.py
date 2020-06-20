from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import ImageCreateForm
from .models import Image
from common.decorators import ajax_required


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()

            messages.success(request, 'Image added successfully')
            return redirect(new_image)
    else:
        form = ImageCreateForm()

    ctx = dict(section='images', form=form)
    return render(request, 'images/image/create.html', ctx)


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    ctx = dict(section='images', image=image)
    return render(request, 'images/image/detail.html', ctx)


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 5)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        return HttpResponse()

    ctx = dict(section='images', images=images)
    if request.is_ajax():
        return render(request, 'images/image/list_ajax.html', ctx)
    return render(request, 'images/image/list.html', ctx)