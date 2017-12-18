#from django.conf import settings
import settings
import facebook
import requests


class FacebookFeed:
    token_url = 'https://graph.facebook.com/oauth/access_token'
    params = dict(client_id=settings.SOCIAL_AUTH_FACEBOOK_KEY, client_secret=settings.SOCIAL_AUTH_FACEBOOK_SECRET,
                  grant_type='client_credentials')

    #params = dict(client_id=123, client_secret=1212, grant_type='client_credentials')


#grant_type = 'client_credentials')

    @classmethod
    def get_posts(cls, user, count=6):
        try:
            token_response = requests.get(url=cls.token_url, params=cls.params)
            print('we are here ', token_response.text)
            access_token = token_response.text.split('=')[1]
            graph = facebook.GraphAPI(access_token)
            profile = graph.get_object(user)
            query_string = 'posts?limit={0}'.format(count)
            posts = graph.get_connections(profile['id'], query_string)
            print("Profile: {}, query_string: {}, posts: {}".format(profile, query_string, posts) )
            return posts
        except facebook.GraphAPIError:
            return None


f = FacebookFeed()
print(f.get_posts(1234567))