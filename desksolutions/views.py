from django.shortcuts import render
from .forms import OrganizationHeadForm
from .models import OrganizationHead
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from ProjectDeskSolutions import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def OrganizationRegister(request):
    context = {}
    if request.method == "POST" and request.is_ajax():
        form = OrganizationHeadForm(request.POST or None)
        if form.is_valid():
            organization = form.save()
            group, created = Group.objects.get_or_create(
                name=settings.GROUP_ALLOCATE)

            ct = ContentType.objects.get_for_model(OrganizationHead)
            if created:
                permission = Permission.objects.filter(content_type=ct)

                for perm in permission:
                    group.permissions.add(perm)
                group.save()
                organization.groups.add(group)
            else:
                organization.groups.add(group)

            # ser_instance = serializers.serialize('json', organization)
            # context['success'] = True
            # form.save()
            return JsonResponse(context)
            # return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            print("invalid form")
            # context['form'] = form
            context['form'] = form.errors
            return JsonResponse(context)
    else:
        form = OrganizationHeadForm()
        context['form'] = form

    return render(request, 'desksolutions/base.html', context)
