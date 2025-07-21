from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Category, 
    PricingPlan, 
    AITool, 
    ToolImage, 
    ToolVideo, 
    Feature,
    Review,
    Comparison,
    Article,
    NewsletterSubscriber,
    ContactSubmission,
    ToolSubmission,
    SiteStat
)

class ToolImageInline(admin.TabularInline):
    model = ToolImage
    extra = 1
    readonly_fields = ['preview_image']
    
    def preview_image(self, obj):
        return format_html('<img src="{}" height="100" />', obj.image.url) if obj.image else '-'
    preview_image.short_description = 'Preview'

class ToolVideoInline(admin.TabularInline):
    model = ToolVideo
    extra = 1

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1

class PricingPlanInline(admin.TabularInline):
    model = AITool.pricing_plans.through
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_free')
    list_filter = ('is_free',)
    search_fields = ('name', 'description')
    list_per_page = 20

@admin.register(AITool)
class AIToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_logo', 'short_description', 'website_link', 
                   'pricing_type', 'is_verified', 'featured', 'views', 'created_at')
    list_filter = ('pricing_type', 'is_verified', 'featured', 'categories', 'created_at')
    search_fields = ('name', 'short_description', 'long_description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ToolImageInline, ToolVideoInline, FeatureInline, PricingPlanInline]
    filter_horizontal = ('categories',)
    readonly_fields = ('views', 'created_at', 'updated_at')
    list_per_page = 20
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'short_description', 'long_description', 'website_url')
        }),
        ('Media', {
            'fields': ('logo', 'logo_url')
        }),
        ('Metadata', {
            'fields': ('categories', 'pricing_type', 'pricing_plans', 'launch_date')
        }),
        ('Status', {
            'fields': ('featured', 'is_verified', 'views')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def website_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.website_url, obj.website_url)
    website_link.short_description = 'Website'

    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" height="30" />', obj.logo.url)
        elif obj.logo_url:
            return format_html('<img src="{}" height="30" />', obj.logo_url)
        return '-'
    display_logo.short_description = 'Logo'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('tool', 'user', 'rating', 'title', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved', 'created_at')
    search_fields = ('title', 'content', 'tool__name')
    list_editable = ('is_approved',)
    list_per_page = 20
    actions = ['approve_reviews', 'disapprove_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
    approve_reviews.short_description = "Approve selected reviews"

    def disapprove_reviews(self, request, queryset):
        queryset.update(is_approved=False)
    disapprove_reviews.short_description = "Disapprove selected reviews"

@admin.register(Comparison)
class ComparisonAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tools',)
    list_per_page = 20
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'views', 'created_at')
    list_filter = ('is_published', 'categories', 'created_at')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories', 'related_tools')
    list_per_page = 20
    readonly_fields = ('views', 'created_at', 'updated_at')
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'excerpt')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Relationships', {
            'fields': ('categories', 'related_tools')
        }),
        ('Metadata', {
            'fields': ('author', 'is_published', 'views')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subscribed_at', 'is_active')
    list_filter = ('is_active', 'subscribed_at')
    search_fields = ('email', 'name')
    readonly_fields = ('subscribed_at', 'unsubscribe_token')
    list_per_page = 20

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_processed')
    list_filter = ('is_processed', 'submitted_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('submitted_at',)
    list_per_page = 20
    actions = ['mark_as_processed', 'mark_as_unprocessed']

    def mark_as_processed(self, request, queryset):
        queryset.update(is_processed=True)
    mark_as_processed.short_description = "Mark selected submissions as processed"

    def mark_as_unprocessed(self, request, queryset):
        queryset.update(is_processed=False)
    mark_as_unprocessed.short_description = "Mark selected submissions as unprocessed"

@admin.register(ToolSubmission)
class ToolSubmissionAdmin(admin.ModelAdmin):
    list_display = ('tool_name', 'tool_url', 'submitted_by', 'submitted_at', 'is_processed')
    list_filter = ('is_processed', 'submitted_at')
    search_fields = ('tool_name', 'tool_url', 'description')
    readonly_fields = ('submitted_at',)
    list_per_page = 20
    actions = ['mark_as_processed', 'mark_as_unprocessed']

    def mark_as_processed(self, request, queryset):
        queryset.update(is_processed=True)
    mark_as_processed.short_description = "Mark selected submissions as processed"

    def mark_as_unprocessed(self, request, queryset):
        queryset.update(is_processed=False)
    mark_as_unprocessed.short_description = "Mark selected submissions as unprocessed"

@admin.register(SiteStat)
class SiteStatAdmin(admin.ModelAdmin):
    list_display = ('stat_name', 'stat_value', 'icon', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('stat_name', 'stat_value')
    list_editable = ('stat_value', 'icon', 'is_active')
    list_per_page = 20