from django.core.management.base import BaseCommand
from andrekaApp.models import Product
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Add sample products to the database'

    def handle(self, *args, **options):
        products_data = [
            {
                'name': 'The Urban Nomad Trench',
                'slug': 'womens-trench-coat',
                'description': 'A classic, longline trench coat perfect for adding a sophisticated layer to any outfit. Its versatile design and neutral tone make it a timeless piece for both daily wear and travel.',
                'price': 189.99,
                'original_price': 249.99,
                'stock': 12,
                'category': 'womens-fashion',
                'is_available': True,
            },
            {
                'name': 'Metropolitan Chic Blazer',
                'slug': 'womens-camel-blazer',
                'description': 'A single-breasted blazer in a warm camel tone, ideal for creating a polished and professional look. It can be paired with matching trousers or worn as a standout piece over a simple dress.',
                'price': 115.50,
                'original_price': 150.00,
                'stock': 25,
                'category': 'womens-fashion',
                'is_available': True,
            },
            {
                'name': 'Classic Denim Jacket',
                'slug': 'mens-denim-jacket',
                'description': 'A timeless denim jacket crafted from premium cotton denim. Features a classic fit with button closure and chest pockets. Perfect for layering over t-shirts or sweaters.',
                'price': 89.99,
                'original_price': 120.00,
                'stock': 18,
                'category': 'mens-fashion',
                'is_available': True,
            },
            {
                'name': 'Premium Leather Sneakers',
                'slug': 'mens-leather-sneakers',
                'description': 'Handcrafted leather sneakers with superior comfort and style. Features a cushioned insole and durable rubber sole for all-day wear. Available in multiple colors.',
                'price': 149.99,
                'original_price': 199.99,
                'stock': 30,
                'category': 'sneakers',
                'is_available': True,
            },
            {
                'name': 'Elegant Evening Dress',
                'slug': 'womens-evening-dress',
                'description': 'A stunning evening dress perfect for special occasions. Features elegant draping, a flattering silhouette, and premium fabric that moves beautifully.',
                'price': 299.99,
                'original_price': 399.99,
                'stock': 8,
                'category': 'womens-fashion',
                'is_available': True,
            },
            {
                'name': 'Casual Cotton T-Shirt',
                'slug': 'mens-cotton-tshirt',
                'description': 'Soft, comfortable cotton t-shirt with a relaxed fit. Made from 100% organic cotton, perfect for everyday wear. Available in various colors.',
                'price': 24.99,
                'original_price': 35.00,
                'stock': 50,
                'category': 'mens-fashion',
                'is_available': True,
            },
            {
                'name': 'Running Performance Sneakers',
                'slug': 'womens-running-sneakers',
                'description': 'High-performance running sneakers designed for comfort and speed. Features advanced cushioning technology and breathable mesh upper.',
                'price': 129.99,
                'original_price': 169.99,
                'stock': 22,
                'category': 'sneakers',
                'is_available': True,
            },
            {
                'name': 'Designer Handbag',
                'slug': 'womens-designer-handbag',
                'description': 'Luxury handbag crafted from genuine leather with elegant hardware. Features multiple compartments and adjustable strap. Perfect for both casual and formal occasions.',
                'price': 199.99,
                'original_price': 279.99,
                'stock': 15,
                'category': 'accessories',
                'is_available': True,
            },
        ]

        created_count = 0
        for product_data in products_data:
            # Check if product already exists
            if not Product.objects.filter(slug=product_data['slug']).exists():
                # Create a placeholder image path (you'll need to add actual images)
                product_data['image'] = 'products/placeholder.jpg'
                Product.objects.create(**product_data)
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created product: {product_data["name"]}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product_data["name"]}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new products!')
        )
