from django.contrib import admin
from akun.models import LevelUser, pegawai, pelanggan
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class User_BsAdmin(UserAdmin):
    # inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(User_BsAdmin, self).get_inline_instances(request, obj)

    list_display = ['username','is_active','is_admin', 'is_teknisi', 'is_pelanggan']
    search_fields = ['username']
    list_per_page = 5
    fieldsets = (
        (('Personal info'), {'fields': ('username',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'is_admin', 'is_teknisi', 'is_pelanggan')}),
        (('Important dates'), {'fields': ('date_joined', 'last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_admin', 'is_teknisi', 'is_pelanggan'),
        }),
    )

admin.site.register(LevelUser, User_BsAdmin)
admin.site.register(pegawai)
admin.site.register(pelanggan)