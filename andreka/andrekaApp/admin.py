from django.contrib import admin
from .models import Product, UserProfile, Order, OrderItem, Cart, CartItem, Payment, BlogPost, BlogImage

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'original_price', 'category', 'stock', 'is_available', 'created_at')
    list_filter = ('category', 'is_available', 'created_at')
    search_fields = ('name', 'description', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'original_price', 'stock', 'is_available')
    ordering = ('-created_at',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'category')
        }),
        ('Pricing', {
            'fields': ('price', 'original_price')
        }),
        ('Inventory', {
            'fields': ('stock', 'is_available')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'city', 'created_at')
    list_filter = ('created_at', 'newsletter_subscription')
    search_fields = ('user__username', 'user__email', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_number', 'user__username', 'user__email')
    readonly_fields = ('order_number', 'created_at', 'updated_at')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'product_price', 'quantity')
    list_filter = ('order__status',)
    search_fields = ('product_name', 'order__order_number')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'total_items', 'total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'session_key')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__name', 'cart__user__username')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'order', 'payment_method', 'amount', 'status', 'created_at')
    list_filter = ('payment_method', 'status', 'created_at')
    search_fields = ('payment_id', 'order__order_number', 'order__user__username')
    readonly_fields = ('payment_id', 'created_at', 'updated_at')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'author', 'views', 'created_at')
    list_filter = ('category', 'status', 'is_featured', 'created_at')
    search_fields = ('title', 'excerpt', 'content', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status', 'is_featured')
    ordering = ('-created_at',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'category')
        }),
        ('Publishing', {
            'fields': ('status', 'is_featured', 'author', 'published_at')
        }),
        ('SEO & Organization', {
            'fields': ('tags',)
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Analytics', {
            'fields': ('views',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('views', 'created_at', 'updated_at')

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'caption', 'order', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('blog_post__title', 'caption', 'alt_text')
    ordering = ('blog_post', 'order', 'created_at')
