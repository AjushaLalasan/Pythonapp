from django.contrib import admin
from .models import Service, ProjectCategory, Project, Testimonial, QuoteRequest, ContactMessage, CompanyStat


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_featured', 'created_at')
    list_editable = ('order', 'is_featured')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client_name', 'location', 'completion_year', 'is_featured', 'order')
    list_filter = ('category', 'is_featured', 'completion_year')
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'client_name', 'location', 'short_summary')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company_or_role', 'rating', 'is_active', 'created_at')
    list_filter = ('rating', 'is_active')
    list_editable = ('is_active', 'rating')
    search_fields = ('client_name', 'company_or_role', 'quote')


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'project_type', 'estimated_budget', 'status', 'created_at')
    list_filter = ('status', 'project_type', 'estimated_budget', 'timeframe')
    list_editable = ('status',)
    search_fields = ('full_name', 'email', 'phone', 'message', 'site_location')
    readonly_fields = ('created_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_resolved', 'created_at')
    list_filter = ('is_resolved', 'created_at')
    list_editable = ('is_resolved',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)


@admin.register(CompanyStat)
class CompanyStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'number_value', 'icon', 'order')
    list_editable = ('number_value', 'order')
