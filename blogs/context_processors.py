from assignment.models import SocialLink
from blogs.models import Category


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)
# This context processor retrieves all categories from the database

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)