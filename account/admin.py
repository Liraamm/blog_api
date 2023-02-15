from django.contrib.auth import get_user_model
from django.contrib import admin

User = get_user_model()

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_staff')
    list_filter =(
        ('is_staff', admin.BooleanFieldListFilter),
    )