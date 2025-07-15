import requests

# Step 1: App credentials (must be registered in Fyers Developer Console under API v3)
APP_ID = "519Z1LNOLC-100"
APP_SECRET = "30KC8NSD9L"
REDIRECT_URI = "https://127.0.0.1"  # Must match exactly in Fyers portal

# Step 2: Generate auth URL
def get_auth_code_url():
    return f"https://api.fyers.in/api/v3/generate-authcode?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&response_type=code&state=sample_state&scope=read+write"

print("🔗 Visit this URL in your browser and login:")
print(get_auth_code_url())

# Step 3: After login, you'll be redirected to a URL with ?auth_code=xxxx
auth_code = input("\n📥 Paste the `auth_code` from the URL here: ")

# Step 4: Exchange auth_code for access token
def get_access_token(auth_code):
    url = "https://api.fyers.in/api/v3/token"
    payload = {
        "grant_type": "authorization_code",
        "client_id": APP_ID,
        "secret_key": APP_SECRET,
        "code": auth_code,
        "redirect_uri": REDIRECT_URI
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

token_response = get_access_token(auth_code)
print("\n✅ Access Token Response:")
print(token_response)
