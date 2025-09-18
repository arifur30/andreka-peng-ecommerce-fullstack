# Example: Adding a blog post programmatically
from andrekaApp.models import BlogPost
from django.contrib.auth.models import User
from django.utils import timezone

# Get admin user
admin_user = User.objects.get(username='admin')

# Create new blog post
new_post = BlogPost.objects.create(
    title="Your New Blog Post Title",
    excerpt="Short description of your post",
    content="""
    <h2>Your Content Here</h2>
    <p>Write your blog post content here. You can use HTML tags for formatting.</p>
    <ul>
        <li>Bullet points</li>
        <li>More content</li>
    </ul>
    """,
    category='fashion',  # or 'trends', 'lifestyle', 'beauty', 'events', 'designer', 'sustainability'
    tags='fashion, style, trends',
    author=admin_user,
    status='published',
    is_featured=False
)

print(f"Created blog post: {new_post.title}")

