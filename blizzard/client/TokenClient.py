# Function to obtain OAuth token
import os

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


def get_oauth_token():
    client_id = os.getenv("CLIENT_ID")
    oauth = OAuth2Session(client=BackendApplicationClient(client_id=client_id))
    token = oauth.fetch_token(token_url=os.getenv("TOKEN_URL"), client_id=client_id,
                              client_secret=os.getenv("CLIENT_SECRET"))
    
    return token["access_token"]
