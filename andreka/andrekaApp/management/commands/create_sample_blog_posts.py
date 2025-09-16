from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from andrekaApp.models import BlogPost, BlogImage
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create sample blog posts for the fashion blog'

    def handle(self, *args, **options):
        # Get or create admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@andreka.com',
                'first_name': 'Andreka',
                'last_name': 'Admin',
                'is_staff': True,
                'is_superuser': True
            }
        )
        
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created admin user'))
        
        # Sample blog posts
        blog_posts_data = [
            {
                'title': 'Spring 2025 Fashion Trends: What to Wear This Season',
                'excerpt': 'Discover the hottest fashion trends for spring 2025, from bold colors to sustainable fashion choices that will define your wardrobe.',
                'content': '''
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
                    
                    <blockquote>
                        "Fashion should be a force for good, not just a means of self-expression. This season, we're seeing a beautiful marriage of style and sustainability." - Fashion Editor, Vogue Bangladesh
                    </blockquote>
                    
                    <h2>Key Silhouettes</h2>
                    <p>The spring 2025 silhouette is all about balance—structured yet flowing, modern yet timeless. Think oversized blazers paired with fluid skirts, or fitted tops with wide-leg trousers.</p>
                    
                    <h3>Trending Styles:</h3>
                    <ul>
                        <li>Oversized blazers with structured shoulders</li>
                        <li>High-waisted wide-leg trousers</li>
                        <li>Midi-length dresses with defined waists</li>
                        <li>Layered textures and mixed materials</li>
                    </ul>
                    
                    <p>As we embrace the new season, remember that the best fashion trend is confidence. Wear what makes you feel beautiful, powerful, and authentically yourself.</p>
                ''',
                'category': 'trends',
                'tags': 'spring trends, fashion 2025, sustainable fashion, colors, style',
                'is_featured': True,
                'status': 'published'
            },
            {
                'title': 'Sustainable Fashion: Building an Eco-Friendly Wardrobe',
                'excerpt': 'Learn how to create a sustainable wardrobe that's both stylish and environmentally conscious. Tips for ethical fashion choices.',
                'content': '''
                    <h2>The Impact of Fast Fashion</h2>
                    <p>Fast fashion has revolutionized how we shop, but at what cost? The environmental impact of the fashion industry is staggering, with textile waste and carbon emissions reaching alarming levels.</p>
                    
                    <h3>Why Sustainable Fashion Matters:</h3>
                    <ul>
                        <li>Reduces environmental pollution and waste</li>
                        <li>Supports ethical labor practices</li>
                        <li>Creates timeless pieces that last longer</li>
                        <li>Encourages mindful consumption</li>
                    </ul>
                    
                    <h2>Building Your Sustainable Wardrobe</h2>
                    <p>Creating an eco-friendly wardrobe doesn't mean sacrificing style. It's about making conscious choices that benefit both you and the planet.</p>
                    
                    <h3>Essential Steps:</h3>
                    <ol>
                        <li><strong>Audit Your Current Wardrobe</strong> - Take inventory of what you own and identify gaps</li>
                        <li><strong>Invest in Quality Basics</strong> - Choose well-made pieces that will last for years</li>
                        <li><strong>Support Ethical Brands</strong> - Research brands that prioritize sustainability</li>
                        <li><strong>Embrace Second-Hand Shopping</strong> - Thrift stores and vintage shops offer unique finds</li>
                        <li><strong>Care for Your Clothes</strong> - Proper maintenance extends garment life</li>
                    </ol>
                    
                    <h2>Sustainable Materials to Look For</h2>
                    <p>When shopping for new pieces, look for these eco-friendly materials:</p>
                    
                    <ul>
                        <li><strong>Organic Cotton</strong> - Grown without harmful pesticides</li>
                        <li><strong>Hemp</strong> - Requires minimal water and pesticides</li>
                        <li><strong>Linen</strong> - Made from flax, a renewable resource</li>
                        <li><strong>Tencel</strong> - Made from sustainably sourced wood pulp</li>
                        <li><strong>Recycled Polyester</strong> - Made from plastic bottles and other waste</li>
                    </ul>
                    
                    <p>Remember, sustainable fashion is a journey, not a destination. Every small step towards conscious consumption makes a difference.</p>
                ''',
                'category': 'sustainability',
                'tags': 'sustainable fashion, eco-friendly, ethical fashion, green wardrobe',
                'is_featured': True,
                'status': 'published'
            },
            {
                'title': 'Designer Spotlight: Local Bangladeshi Fashion Innovators',
                'excerpt': 'Meet the talented Bangladeshi designers who are putting our country on the global fashion map with their innovative designs.',
                'content': '''
                    <h2>Celebrating Local Talent</h2>
                    <p>Bangladesh's fashion scene is experiencing a renaissance, with talented designers creating innovative pieces that honor traditional craftsmanship while embracing modern aesthetics.</p>
                    
                    <h2>Featured Designers</h2>
                    
                    <h3>Rashida Begum - Textile Artisan</h3>
                    <p>Rashida Begum has been revolutionizing traditional jamdani weaving techniques, creating contemporary pieces that tell the story of Bangladesh's rich textile heritage. Her work has been featured in international fashion weeks.</p>
                    
                    <h3>Ahmed Hassan - Sustainable Fashion Pioneer</h3>
                    <p>Ahmed Hassan is leading the charge in sustainable fashion, using recycled materials and traditional techniques to create stunning contemporary pieces. His commitment to environmental responsibility has earned him recognition worldwide.</p>
                    
                    <h3>Fatima Rahman - Modern Minimalist</h3>
                    <p>Fatima Rahman's clean, minimalist designs have captured the attention of fashion enthusiasts globally. Her work proves that simplicity and elegance go hand in hand.</p>
                    
                    <h2>The Future of Bangladeshi Fashion</h2>
                    <p>These designers represent just a fraction of the incredible talent emerging from Bangladesh. With their innovative approaches and commitment to quality, they're shaping the future of global fashion.</p>
                    
                    <blockquote>
                        "Bangladesh has always been a land of creativity and craftsmanship. Now, our designers are bringing that heritage to the world stage." - Fashion Industry Expert
                    </blockquote>
                    
                    <h2>Supporting Local Designers</h2>
                    <p>By choosing pieces from local designers, you're not just buying clothes—you're supporting artists, preserving cultural heritage, and contributing to the growth of Bangladesh's creative economy.</p>
                    
                    <p>Look for local designer collections at Andreka, where we're proud to showcase the best of Bangladeshi fashion talent.</p>
                ''',
                'category': 'designer',
                'tags': 'Bangladeshi designers, local fashion, textile art, cultural heritage',
                'is_featured': False,
                'status': 'published'
            },
            {
                'title': 'Fashion Week Highlights: What We Learned from the Runways',
                'excerpt': 'A comprehensive look at the most exciting trends and moments from this season\'s fashion weeks around the world.',
                'content': '''
                    <h2>Fashion Week Recap</h2>
                    <p>This season's fashion weeks have delivered some of the most exciting and innovative collections we've seen in years. From bold statements to subtle elegance, designers have pushed boundaries and redefined modern style.</p>
                    
                    <h2>Standout Collections</h2>
                    
                    <h3>Paris Fashion Week</h3>
                    <p>Paris Fashion Week showcased a perfect blend of classic French elegance and contemporary innovation. Designers experimented with proportions, creating oversized silhouettes that felt both dramatic and wearable.</p>
                    
                    <h3>Milan Fashion Week</h3>
                    <p>Italian designers brought their signature luxury and craftsmanship to the forefront, with intricate details and rich textures dominating the runways. The focus was on timeless pieces that transcend seasonal trends.</p>
                    
                    <h3>New York Fashion Week</h3>
                    <p>American designers embraced diversity and inclusivity, with collections that celebrated different body types, cultures, and perspectives. The energy was electric and inspiring.</p>
                    
                    <h2>Key Trends from the Runways</h2>
                    
                    <h3>Color Trends</h3>
                    <ul>
                        <li>Bold primary colors making a comeback</li>
                        <li>Metallic accents for evening wear</li>
                        <li>Earth tones for sustainable collections</li>
                        <li>Neon highlights for statement pieces</li>
                    </ul>
                    
                    <h3>Silhouette Trends</h3>
                    <ul>
                        <li>Oversized outerwear</li>
                        <li>High-waisted everything</li>
                        <li>Asymmetric hemlines</li>
                        <li>Layered textures</li>
                    </ul>
                    
                    <h2>What This Means for Your Wardrobe</h2>
                    <p>While runway trends can seem overwhelming, the key is to adapt them to your personal style. Look for pieces that speak to you and can be integrated into your existing wardrobe.</p>
                    
                    <p>Remember, fashion is about self-expression. Use these trends as inspiration, but always stay true to your personal aesthetic.</p>
                ''',
                'category': 'events',
                'tags': 'fashion week, runway trends, designer collections, style inspiration',
                'is_featured': False,
                'status': 'published'
            },
            {
                'title': 'Beauty and Fashion: Creating the Perfect Look',
                'excerpt': 'Discover how to coordinate your beauty routine with your fashion choices to create cohesive, stunning looks for any occasion.',
                'content': '''
                    <h2>The Art of Coordination</h2>
                    <p>Fashion and beauty are two sides of the same coin. When coordinated properly, they create a powerful, cohesive look that enhances your natural beauty and expresses your personal style.</p>
                    
                    <h2>Color Coordination</h2>
                    <p>The key to a polished look is understanding how colors work together. Your makeup should complement your outfit, not compete with it.</p>
                    
                    <h3>Basic Rules:</h3>
                    <ul>
                        <li>For bold clothing, keep makeup subtle</li>
                        <li>For neutral outfits, add a pop of color with makeup</li>
                        <li>Match undertones - warm clothing with warm makeup</li>
                        <li>Use complementary colors for dramatic effect</li>
                    </ul>
                    
                    <h2>Occasion-Based Looks</h2>
                    
                    <h3>Professional Settings</h3>
                    <p>For work environments, opt for clean, polished looks. Think neutral eyeshadows, defined brows, and a classic red or nude lip. Keep jewelry minimal and elegant.</p>
                    
                    <h3>Evening Events</h3>
                    <p>Evening looks allow for more creativity. Smoky eyes, bold lips, and statement jewelry can create stunning, memorable looks. Just remember to balance bold makeup with simpler clothing, or vice versa.</p>
                    
                    <h3>Casual Outings</h3>
                    <p>Casual looks should feel effortless and natural. Fresh, dewy skin, subtle eye makeup, and a tinted lip balm create a beautiful, low-maintenance look.</p>
                    
                    <h2>Seasonal Considerations</h2>
                    <p>Your beauty routine should adapt to the seasons, just like your wardrobe.</p>
                    
                    <h3>Spring/Summer</h3>
                    <ul>
                        <li>Light, breathable foundations</li>
                        <li>Bright, fresh lip colors</li>
                        <li>Waterproof mascara for humid weather</li>
                        <li>SPF protection in all products</li>
                    </ul>
                    
                    <h3>Fall/Winter</h3>
                    <ul>
                        <li>Rich, moisturizing foundations</li>
                        <li>Deeper lip colors</li>
                        <li>Hydrating skincare routines</li>
                        <li>Layered textures in both fashion and beauty</li>
                    </ul>
                    
                    <h2>Building Your Beauty Wardrobe</h2>
                    <p>Just like fashion, beauty requires investment in quality basics. Start with a good foundation, mascara, and lipstick, then build your collection based on your lifestyle and preferences.</p>
                    
                    <p>Remember, the goal is to enhance your natural beauty and express your personal style. Experiment, have fun, and don't be afraid to try new things!</p>
                ''',
                'category': 'beauty',
                'tags': 'beauty tips, makeup, fashion coordination, style guide',
                'is_featured': False,
                'status': 'published'
            }
        ]
        
        created_posts = []
        
        for post_data in blog_posts_data:
            post, created = BlogPost.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'excerpt': post_data['excerpt'],
                    'content': post_data['content'],
                    'category': post_data['category'],
                    'tags': post_data['tags'],
                    'is_featured': post_data['is_featured'],
                    'status': post_data['status'],
                    'author': admin_user,
                    'published_at': timezone.now()
                }
            )
            
            if created:
                created_posts.append(post.title)
                self.stdout.write(self.style.SUCCESS(f'Created blog post: {post.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Blog post already exists: {post.title}'))
        
        if created_posts:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created {len(created_posts)} blog posts!')
            )
        else:
            self.stdout.write(
                self.style.WARNING('No new blog posts were created. All posts already exist.')
            )
