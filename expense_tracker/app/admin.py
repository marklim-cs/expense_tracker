from django.contrib import admin
from .models import AddMoneyInfo, UserProfile

# Register your models here.
class AddMoneyInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "quantity", "date", "category", "expense_type")

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "profession", "savings", "income", "expenses")

admin.site.register(AddMoneyInfo, AddMoneyInfoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)