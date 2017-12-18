from django.http import HttpResponse
from app.services.social_networks.facebook import FacebookFeed
import json

def get_facebook_posts(request, user):
    posts = FacebookFeed.get_posts(user=user)
    if not posts:
        return HttpResponse(status=500, content="Can't fetch posts for desired user", content_type="application/json")
    return HttpResponse(json.dumps(posts), content_type="application/json")