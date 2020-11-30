# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User

# Model
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin. """
    
    list_display = ('pk','user','phone_number', 'website', 'picture') #Muestra el encabezado con los campos descritos
    list_display_links = ('user','pk') #redirecciona al detalle dando click en user o phone_number
    list_editable = ('phone_number','website','picture') #Edita los datos desde la tabla
    search_fields = ('user__email','user__username','user__first_name','user__last_name','phone_number') #filtro por campos
    
    list_filter = ('created','modified','user__is_active','user__is_staff') #Añade filtros
    
    fieldsets =(
        ('Profile',{
            'fields':(('user','picture'),),
            }),
        ('Extra Info',{
            'fields':(('website','phone_number'),
                        ('biography'),),
            }),
        ('Metadata',{
            'fields':(('created','modified'),),
            }),
    )
    
    readonly_fields = ('created','modified')
    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    varbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_staff'
        )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)