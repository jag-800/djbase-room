from django.contrib import admin
from .models import Todo, WebColor
    
class WebColorAdmin(admin.ModelAdmin):
    list_display = ['title', 'app']

    # アクションバーの設定
    actions = ['make_app', 'no_app']

    # 公開用のカスタムメソッド
    def make_app(self, request, queryset):
        queryset.update(app=True)
    make_app.short_description = '公開する'

    # 非公開用のカスタムメソッド
    def no_app(self, request, queryset):
        queryset.update(app=False)
    no_app.short_description = '公開しない'
    

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)






        
# Register your models here.
admin.site.register(Todo)
admin.site.register(WebColor, WebColorAdmin)
admin.site.register(User, MyUserAdmin)
