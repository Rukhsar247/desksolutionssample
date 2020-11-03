from django.contrib import admin
from .models import OrganizationHead
from django.contrib.auth.admin import UserAdmin
from .forms import OrganizationHeadForm


class OrganizationHeadAdmin(UserAdmin):
    add_form = OrganizationHeadForm
    list_display = ('email', 'title',)
    list_filter = ('is_superuser', 'is_staff',)
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('email', 'password', 'title')}),
        ('Permissions', {'fields': ('is_staff',
                                    'is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        ('Personal Information', {
            # To create a section with name 'Personal Information' with mentioned fields
            'description': "hello g",
            # To make char fields and text fields of a specific size
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups',)}
         ),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(email=request.user)


admin.site.register(OrganizationHead, OrganizationHeadAdmin)
