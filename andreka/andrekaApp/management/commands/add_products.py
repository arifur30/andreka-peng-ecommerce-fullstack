from django.core.management.base import BaseCommand
from andrekaApp.models import Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Add initial products to the database'

    def handle(self, *args, **kwargs):
        products_data = [
            {
                'name': 'The Urban Nomad Trench',
                'slug': 'womens-trench-coat',
                'description': 'A classic, longline trench coat perfect for adding a sophisticated layer to any outfit. Its versatile design and neutral tone make it a timeless piece for both daily wear and travel.',
                'price': Decimal('189.99'),
                'stock': 12,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/product1.png'
            },
            {
                'name': 'Metropolitan Chic Blazer',
                'slug': 'womens-camel-blazer',
                'description': 'A single-breasted blazer in a warm camel tone, ideal for creating a polished and professional look. It can be paired with matching trousers or worn as a standout piece over a simple dress.',
                'price': Decimal('115.50'),
                'stock': 25,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/product2.png'
            },
            {
                'name': 'Desert Voyager Suit',
                'slug': 'womens-orange-blazer-suit',
                'description': 'A bold and vibrant suit in a striking orange hue. This set, featuring a structured blazer and tailored trousers, is designed to make a confident statement.',
                'price': Decimal('245.00'),
                'stock': 8,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/Product3.png'
            },
            {
                'name': 'The Boho Denim Vest',
                'slug': 'womens-denim-vest',
                'description': 'A relaxed-fit denim vest with a unique, textured collar. This versatile piece is perfect for layering over knitwear or a dress to add a casual, bohemian flair to your look.',
                'price': Decimal('75.25'),
                'stock': 31,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/Product4.png'
            },
            {
                'name': 'The Linen Luxe Set',
                'slug': 'womens-beige-suit',
                'description': 'A full-length, wide-leg suit in a light, neutral shade. The relaxed silhouette and soft fabric offer both elegance and comfort, making it a perfect choice for warmer weather.',
                'price': Decimal('210.75'),
                'stock': 15,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/product5.png'
            },
            {
                'name': 'Forest Haze Blazer',
                'slug': 'womens-dark-green-blazer',
                'description': 'An elegant, dark green blazer with a structured fit. Its deep color provides a sophisticated alternative to traditional black and can be styled for both professional and casual occasions.',
                'price': Decimal('130.00'),
                'stock': 19,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/product6.png'
            },
            {
                'name': 'Ivory Elegance Suit',
                'slug': 'womens-white-linen-suit',
                'description': 'A crisp and clean all-white suit, exuding a sense of refined style. The lightweight material and classic tailoring make this a powerful and fashionable choice for any event.',
                'price': Decimal('265.00'),
                'stock': 10,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/product7.png'
            },
            {
                'name': 'Terracotta Muse Set',
                'slug': 'womens-oversized-blazer-and-shorts',
                'description': 'A modern and chic two-piece set featuring an oversized blazer and matching shorts in a warm terracotta color. It offers a contemporary twist on classic tailoring.',
                'price': Decimal('195.50'),
                'stock': 14,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/product8.png'
            },
            {
                'name': 'The Rustic Weave Cardigan',
                'slug': 'mens-brown-cardigan',
                'description': 'A ribbed, button-down cardigan in a rich brown tone. Its comfortable knit and classic design make it a versatile layering piece for a relaxed yet stylish look.',
                'price': Decimal('85.00'),
                'stock': 40,
                'category': 'mens-fashion',
                'is_available': True,
                'image': 'products/product9.png'
            },
            {
                'name': 'The Oatmeal Layer Dress',
                'slug': 'womens-layered-dress-and-sweater',
                'description': 'A seamless combination of a light-colored dress and a layered knit sweater. This outfit highlights effortless, comfortable layering and a minimalist aesthetic.',
                'price': Decimal('160.00'),
                'stock': 22,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/product10.png'
            },
            {
                'name': 'The Olive Drape Shirt',
                'slug': 'womens-olive-green-shirt',
                'description': 'A relaxed-fit button-down shirt in a classic olive green. Its soft drape and simple design make it a perfect, easy-to-style staple for any wardrobe.',
                'price': Decimal('55.00'),
                'stock': 55,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/product11.png'
            },
            {
                'name': 'Mocha Minimalist Blazer',
                'slug': 'brown-and-white-blazer',
                'description': 'A unique blazer featuring a split design with one side in a solid brown and the other in a neutral white. This striking contrast creates a modern and artistic statement.',
                'price': Decimal('140.00'),
                'stock': 7,
                'category': 'womens-fashion',
                'is_available': True,
                'image': 'products/product12.png'
            },
            {
                'name': 'Canvas Comfort Trousers',
                'slug': 'gray-and-brown-trousers',
                'description': 'A pair of structured trousers available in both a light gray and a warm brown. Their clean lines and versatile colors make them a foundational piece for professional or casual outfits.',
                'price': Decimal('99.00'),
                'stock': 38,
                'category': 'mens-fashion',
                'is_available': True,
                'image': 'products/product13.png'
            },
            {
                'name': 'The Luxe Lounger Shirt',
                'slug': 'mens-cream-linen-shirt',
                'description': 'A relaxed-fit, lightweight button-down shirt in a soft cream color. The airy fabric and easy-going style are perfect for a comfortable yet elevated look.',
                'price': Decimal('65.00'),
                'stock': 45,
                'category': 'mens-fashion',
                'is_available': True,
                'image': 'products/product14.png'
            },
            {
                'name': 'The Denim Heritage Jacket',
                'slug': 'mens-denim-jacket',
                'description': 'A timeless classic, this dark denim jacket features a standard fit and traditional styling. It\'s a durable and versatile outerwear piece that complements a variety of casual looks.',
                'price': Decimal('120.00'),
                'stock': 28,
                'category': 'mens-fashion',
                'is_available': True,
                'image': 'products/product15.png'
            },
            {
                'name': 'Shearling Soft Jacket',
                'slug': 'mens-green-sherpa-jacket',
                'description': 'A cozy and warm jacket with a plush shearling lining. The relaxed fit and soft texture in a pleasant green shade make it the perfect outerwear for chilly days.',
                'price': Decimal('155.00'),
                'stock': 20,
                'category': 'mens-fashion',
                'is_available': True,
                'image': 'products/product16.png'
            }
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))