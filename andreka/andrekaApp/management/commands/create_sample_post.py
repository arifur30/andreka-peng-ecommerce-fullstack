from django.core.management.base import BaseCommand
from andrekaApp.models import BlogPost, User
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create a sample blog post'

    def handle(self, *args, **options):
        # Get admin user
        admin_user = User.objects.get(username='admin')
        
        # Create sample blog post
        post = BlogPost.objects.create(
            title="Spring 2025 Fashion Trends: What to Wear This Season",
            excerpt="Discover the hottest fashion trends for spring 2025, from bold colors to sustainable fashion choices that will define your wardrobe.",
            content="""
            <h2>The Colors of Spring</h2>
            <p>Spring 2025 brings a refreshing palette of colors that speak to renewal and optimism. From soft pastels to vibrant neons, this season is all about expressing your personality through color.</p>
            
            <h3>Must-Have Colors:</h3>
            <ul>
                <li><strong>Lavender Mist</strong> - A soft, dreamy purple that works beautifully for both day and evening wear</li>
                <li><strong>Sunset Orange</strong> - A warm, energetic orange that adds instant vibrancy to any outfit</li>
                <li><strong>Mint Green</strong> - Fresh and clean, perfect for casual and professional settings</li>
                <li><strong>Blush Pink</strong> - Elegant and feminine, ideal for romantic occasions</li>
            </ul>
            
            <h2>Sustainable Fashion Takes Center Stage</h2>
            <p>This season, sustainability isn't just a trend—it's a movement. Designers are embracing eco-friendly materials and ethical production methods, proving that style and sustainability can coexist beautifully.</p>
            """,
            category='trends',
            tags='spring trends, fashion 2025, sustainable fashion, colors, style',
            author=admin_user,
            status='published',
            is_featured=True,
            published_at=timezone.now()
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created blog post: {post.title}'))
