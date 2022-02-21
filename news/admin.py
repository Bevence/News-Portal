from django.contrib import admin
from news.models import News, Category


# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "count", "created_at")


admin.site.register(Category)
