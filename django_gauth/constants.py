GOOGLE_CLIENT_ID = "<GOOGLE CLIENT ID>"
GOOGLE_CLIENT_SECRET = "<GOOGLE CLIENT SECRET>"
BASE_URI = 'http://localhost:8000'

GOOGLE_REDIRECT_URI = f"{BASE_URI}/admin/google/callback"
GOOGLE_SCOPES = "https://www.googleapis.com/auth/userinfo.email"
GOOGLE_LOGIN_REDIRECT_URI = (f"https://accounts.google.com/o/oauth2/v2/auth?"
                             f"response_type={'code'}"
                             f"&scope={GOOGLE_SCOPES}"
                             f"&access_type={'offline'}"
                             f"&include_grant_scopes={'true'}"
                             f"&state={'admin'}"
                             f"&client_id={GOOGLE_CLIENT_ID}"
                             f"&redirect_uri={GOOGLE_REDIRECT_URI}")
