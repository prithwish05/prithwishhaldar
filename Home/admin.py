from django.contrib import admin
from .models import Skills


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
	list_display = ("name", "percentage", "color_start", "color_end")
	readonly_fields = ("color_start", "color_end")
	fields = ("name", "percentage", "color_start", "color_end")

