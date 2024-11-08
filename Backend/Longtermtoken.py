import requests

# Replace these values with your app's details and the short-lived access token
app_id = "1074785731014824"
app_secret = "a92e2d308901e069da2f0166560a45be"
short_lived_token = "EAAPRgw208KgBO3Waq0LAawc2fQWMFkWVmpzZAUMy5HDuglER5vZBXhGrnKxcUCnOXGznqtj27WKRtMVn1ly4xZC2Jtd6nnGo8szuI73OZC0sURTl72rB7P1UBo11LiCSZC6jymfjUa8kpCW5d09lZBiCxYbR0Ot0Tmq09givASu5VGpdAVImBWXgjQoZCUZBLYgLJGpZCz5BgFT5PZBxWNUAu0ag06hSMZD"

# Construct the request URL
url = (
    f"https://graph.facebook.com/v12.0/oauth/access_token?"
    f"grant_type=fb_exchange_token&"
    f"client_id={app_id}&"
    f"client_secret={app_secret}&"
    f"fb_exchange_token={short_lived_token}"
)

# Make the request
response = requests.get(url)
long_lived_token = response.json().get("access_token")
print(f"Long-Lived Access Token: {long_lived_token}")


# Long-Lived Access Token: EAAPRgw208KgBOzAJy3SuPeD99Vu4yG2xhvrUm8eHVtb3ZC4m8NdY3MGbcOsR1HOi1Q186ZCv97hgrzE0CGgcRbOl0JnGldCvsGOZAk5XmgVoqcRstsWmYmMRBZCSbZAUa2q2wlYFnczwJQLZANAHkeeIltPUfaZByHTrZB8jInSvAKb16zpXhRf8PZBMF