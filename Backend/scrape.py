# WORKED------------------------

# import instaloader
# import sys
# import re

# # Set encoding for standard output
# sys.stdout.reconfigure(encoding='utf-8')

# # Create an instance of Instaloader
# L = instaloader.Instaloader()

# # post_url = "https://www.instagram.com/p/DBsMV1psrRO/?igsh=YTBvOHE1NmlrNmxh"
# post_url = "https://www.instagram.com/p/DBsMV1psrRO/?utm_source=ig_web_button_native_share"

# # Extract the shortcode from the post URL
# shortcode = re.search(r"instagram\.com/p/([A-Za-z0-9_-]+)", post_url).group(1)

# # Load the post using the extracted shortcode
# post = instaloader.Post.from_shortcode(L.context, shortcode)

# # Print post details
# print(f"Post Caption: {post.caption}")
# print(f"Likes: {post.likes}")

# # Download the post image
# L.download_post(post, target="post_image")

# if post.caption:
#     print(f"Post Caption (utf-8): {post.caption.encode('utf-8', errors='ignore').decode('utf-8')}")
# else:
#     print("Post has no caption.")



# FOR REELS--------------------

# import instaloader
# import sys
# import re

# # Set encoding for standard output
# sys.stdout.reconfigure(encoding='utf-8')

# # Create an instance of Instaloader
# L = instaloader.Instaloader()

# # Define the Instagram post URL
# post_url = "https://www.instagram.com/reel/DBfFruENVfV/?igsh=MTR2MjRjcHRtM2xiZA=="

# # Extract the shortcode from the post URL
# # Updated regex to match both /p/ and /reel/ URLs
# match = re.search(r"instagram\.com/(?:p|reel)/([A-Za-z0-9_-]+)", post_url)

# if match:
#     shortcode = match.group(1)
    
#     # Load the post using the extracted shortcode
#     post = instaloader.Post.from_shortcode(L.context, shortcode)

#     # Print post details
#     print(f"Post Caption: {post.caption if post.caption else 'No caption available'}")
#     print(f"Likes: {post.likes}")

#     # Check if the post is a video and download accordingly
#     if post.is_video:
#         print("This post is a video. Downloading the video.")
#         # Download the video
#         L.download_post(post, target="downloaded_video")
#     else:
#         print("This post is an image. Downloading the image.")
#         # Download the image post
#         L.download_post(post, target="downloaded_post_image")

#     # Handle special characters in caption if necessary
#     if post.caption:
#         print(f"Post Caption (utf-8): {post.caption.encode('utf-8', errors='ignore').decode('utf-8')}")
#     else:
#         print("Post has no caption.")
# else:
#     print("No shortcode found in the provided URL.")








import instaloader
# import tweepy
import facebook
import re
import sys
import requests

# Set encoding for standard output
sys.stdout.reconfigure(encoding='utf-8')

# # Function to fetch Instagram post information
# def fetch_instagram_post(post_url):
#     L = instaloader.Instaloader()
    
#     # Extract the shortcode from the post URL
#     match = re.search(r"instagram\.com/(?:p|reel)/([A-Za-z0-9_-]+)", post_url)
    
#     if match:
#         shortcode = match.group(1)
#         post = instaloader.Post.from_shortcode(L.context, shortcode)
        
#         print(f"Instagram Post Caption: {post.caption if post.caption else 'No caption available'}")
#         print(f"Likes: {post.likes}")

#         # Check if the post is a video and download accordingly
#         if post.is_video:
#             print("This post is a video. Downloading the video.")
#             L.download_post(post, target="downloaded_video")
#         else:
#             print("This post is an image. Downloading the image.")
#             L.download_post(post, target="downloaded_post_image")
#     else:
#         print("No shortcode found in the provided Instagram URL.")









# def fetch_facebook_post(post_url):
#     # Use a long-lived access token with necessary permissions
#     # access_token = "EAAPRgw208KgBO8L3L0v2Xk74ScfVZB88Xi1mxvncJp8PSwjnHa2fx9MltRHVsTmOLQZBd2ygGGHwvwugK2RYORsQpuqqUTZB4NHZBzIZA64rTJ1UeJNHlZCqZBBbE60rlVk6jkZCo4PGFwZApPnCZAN5QnoSLUfZBpvIxVk321AIVp4eMYZC2imt2jdb1RC1"
#     access_token = "EAAPRgw208KgBO3Waq0LAawc2fQWMFkWVmpzZAUMy5HDuglER5vZBXhGrnKxcUCnOXGznqtj27WKRtMVn1ly4xZC2Jtd6nnGo8szuI73OZC0sURTl72rB7P1UBo11LiCSZC6jymfjUa8kpCW5d09lZBiCxYbR0Ot0Tmq09givASu5VGpdAVImBWXgjQoZCUZBLYgLJGpZCz5BgFT5PZBxWNUAu0ag06hSMZD"
    
#     graph = facebook.GraphAPI(access_token=access_token, version="2.8")

#     # Adjust the regex to extract post ID, which may include alphanumeric characters
#     match = re.search(r"facebook\.com/.+/(posts|videos)/([a-zA-Z0-9]+)", post_url)

#     if match:
#         post_id = match.group(2)
#     else:
#         print("Could not extract post ID from URL. Ensure the URL is in a standard format.")
#         return

#     try:
#         # Retrieve the post details via Graph API
#         post = graph.get_object(id=post_id, fields="message,likes.summary(true),full_picture")

#         # Print post details
#         print("Post Message:", post.get("message", "No message available"))
#         print("Likes Count:", post["likes"]["summary"]["total_count"])
        
#         # Check if the post has an image
#         if "full_picture" in post:
#             image_url = post["full_picture"]
#             print("Post Image URL:", image_url)

#             # Download the image
#             download_image(image_url, post_id)
#         else:
#             print("No image found in this post.")
        
#     except facebook.GraphAPIError as e:
#         # Error handling for Graph API issues
#         print(f"GraphAPIError: {e}")
#         print("Verify token permissions and post visibility settings.")

# def download_image(image_url, post_id):
#     # Send an HTTP GET request to download the image
#     try:
#         response = requests.get(image_url, stream=True)
#         if response.status_code == 200:
#             # Open the file and write the image data
#             with open(f"facebook_post_{post_id}.jpg", "wb") as file:
#                 for chunk in response.iter_content(1024):
#                     file.write(chunk)
#             print(f"Image downloaded successfully as facebook_post_{post_id}.jpg")
#         else:
#             print(f"Failed to download the image. Status code: {response.status_code}")
#     except Exception as e:
#         print(f"An error occurred while downloading the image: {e}")

# # Replace with the full post URL
# facebook_url = "https://www.facebook.com/IndianCricketTeam/posts/pfbid02xfAChod4KkcwtjNyPiJLRe3SpGwmdKoUAdZYmP1NM6S1Dk2YgydBZMG8iNzaPtB3l"
# fetch_facebook_post(facebook_url)

# ?THIS AGAIN=================

# import facebook
# import re
# import requests

# def fetch_facebook_post(post_url):
#     # Use a long-lived access token with necessary permissions
#     access_token = "AAPRgw208KgBO2oP2c0geRCZCqyR1ChEAO2V3sJ44DG8GtXHf5I58rQdsNZAQk4F4zvDHZCTbB3H9Nt8n0ADGqZAnfkZAe13AXRwzRuZC9VymNDrfZAtm5kH4gVBqbodKxFLru0evVp694bWObNsPtR67RtBCJodd37eo5peL6bqYgPKEpaJfLXhZC8ZC"
#     graph = facebook.GraphAPI(access_token=access_token, version= "16.0")  # Use v12.0 or latest version

#     # Adjust the regex to extract post ID, which may include alphanumeric characters
#     match = re.search(r"facebook\.com/.+/(posts|videos)/([a-zA-Z0-9]+)", post_url)

#     if match:
#         post_id = match.group(2)
#     else:
#         print("Could not extract post ID from URL. Ensure the URL is in a standard format.")
#         return

#     try:
#         # Retrieve the post details via the correct API endpoint
#         post = graph.get_object(id=post_id, fields="message,likes.summary(true),full_picture")

#         # Print post details
#         print("Post Message:", post.get("message", "No message available"))
#         print("Likes Count:", post["likes"]["summary"]["total_count"])
        
#         # Check if the post has an image
#         if "full_picture" in post:
#             image_url = post["full_picture"]
#             print("Post Image URL:", image_url)

#             # Download the image
#             download_image(image_url, post_id)
#         else:
#             print("No image found in this post.")
        
#     except facebook.GraphAPIError as e:
#         # Error handling for Graph API issues
#         print(f"GraphAPIError: {e}")
#         print("Verify token permissions and post visibility settings.")

# def download_image(image_url, post_id):
#     # Send an HTTP GET request to download the image
#     try:
#         response = requests.get(image_url, stream=True)
#         if response.status_code == 200:
#             # Open the file and write the image data
#             with open(f"facebook_post_{post_id}.jpg", "wb") as file:
#                 for chunk in response.iter_content(1024):
#                     file.write(chunk)
#             print(f"Image downloaded successfully as facebook_post_{post_id}.jpg")
#         else:
#             print(f"Failed to download the image. Status code: {response.status_code}")
#     except Exception as e:
#         print(f"An error occurred while downloading the image: {e}")

# # Replace with the full post URL
# facebook_url = "https://www.facebook.com/IndianCricketTeam/posts/pfbid02xfAChod4KkcwtjNyPiJLRe3SpGwmdKoUAdZYmP1NM6S1Dk2YgydBZMG8iNzaPtB3l"  # Example post URL
# fetch_facebook_post(facebook_url)


# AGAIN=============

import requests
import re
from urllib.parse import urljoin
import json

def fetch_facebook_post(post_url: str) -> None:
    """
    Fetch Facebook post details using the modern Graph API endpoint.
    
    Args:
        post_url (str): URL of the Facebook post
    """
    # Your access token - Get this from Facebook Graph API Explorer
    access_token = "EAAPRgw208KgBO3Waq0LAawc2fQWMFkWVmpzZAUMy5HDuglER5vZBXhGrnKxcUCnOXGznqtj27WKRtMVn1ly4xZC2Jtd6nnGo8szuI73OZC0sURTl72rB7P1UBo11LiCSZC6jymfjUa8kpCW5d09lZBiCxYbR0Ot0Tmq09givASu5VGpdAVImBWXgjQoZCUZBLYgLJGpZCz5BgFT5PZBxWNUAu0ag06hSMZD"  # Replace with your token
    
    try:
        # Extract page name and post ID
        match = re.search(r"facebook\.com/([^/]+)/(?:posts|videos)/([^/?]+)", post_url)
        if not match:
            print("Could not extract page and post ID from URL. Please check the URL format.")
            return
        
        page_name = match.group(1)
        post_id = match.group(2)
        
        # First, get the page ID
        base_url = "https://graph.facebook.com/v16.0/"
        page_endpoint = page_name
        page_params = {
            "access_token": access_token,
            "fields": "id"
        }
        
        page_response = requests.get(urljoin(base_url, page_endpoint), params=page_params)
        page_response.raise_for_status()
        page_data = page_response.json()
        page_id = page_data.get('id')
        
        # Now get the post using page_id and post_id
        post_endpoint = f"{page_id}_{post_id}"
        post_params = {
            "access_token": access_token,
            "fields": "message,reactions.summary(total_count).limit(0),attachments{media,type,url}"
        }
        
        # Make the request for post data
        post_response = requests.get(urljoin(base_url, post_endpoint), params=post_params)
        post_response.raise_for_status()
        post_data = post_response.json()
        
        # Print post details
        print("\nPost Details:")
        print("-" * 50)
        print("Message:", post_data.get("message", "No message available"))
        
        # Get reactions count (equivalent to likes in newer API)
        reactions = post_data.get("reactions", {}).get("summary", {}).get("total_count", 0)
        print("Reactions Count:", reactions)
        
        # Handle attachments (images, videos, etc.)
        attachments = post_data.get("attachments", {}).get("data", [])
        for attachment in attachments:
            if attachment.get("type") == "photo":
                image_data = attachment.get("media", {}).get("image", {})
                if image_data:
                    image_url = image_data.get("src")
                    if image_url:
                        print("Image URL:", image_url)
                        download_image(image_url, post_id)
            elif attachment.get("type") == "video":
                print("Video URL:", attachment.get("url", "No video URL available"))
                
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            try:
                error_data = json.loads(e.response.text)
                print("\nDetailed error message:")
                print(json.dumps(error_data, indent=2))
            except:
                print("Raw error response:", e.response.text)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def download_image(image_url: str, post_id: str) -> None:
    """Download image from URL and save it locally."""
    try:
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()
        
        filename = f"facebook_post_{post_id}.jpg"
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Image downloaded successfully as {filename}")
        
    except requests.RequestException as e:
        print(f"Failed to download image: {e}")
    except IOError as e:
        print(f"Failed to save image: {e}")

def get_page_access_token():
    """
    Instructions for getting a Page Access Token
    """
    print("\nTo get a working access token:")
    print("\n1. Go to: https://developers.facebook.com/tools/explorer/")
    print("2. Select your App from the dropdown menu")
    print("3. Click on 'Generate Access Token'")
    print("4. Select these permissions:")
    print("   - pages_read_engagement")
    print("   - pages_read_user_content")
    print("5. Click 'Generate Access Token'")
    print("6. Copy the generated token")
    print("\nReplace 'YOUR_ACCESS_TOKEN' in the code with your new token")

if __name__ == "__main__":
    # Example Facebook post URL
    facebook_url = "https://www.facebook.com/IndianCricketTeam/posts/pfbid02xfAChod4KkcwtjNyPiJLRe3SpGwmdKoUAdZYmP1NM6S1Dk2YgydBZMG8iNzaPtB3l"
    
    # First, show instructions for getting a token
    get_page_access_token()
    
    # Uncomment and run this after you have your token
    fetch_facebook_post(facebook_url)



















# def fetch_facebook_post(facebook_url):
#     # Extract the post ID from the URL
#     match = re.search(r"facebook\.com/.*/posts/([0-9]+)", facebook_url)
#     if not match:
#         print("Invalid Facebook URL.")
#         return
    
#     post_id = match.group(1)

#     # Setup Facebook API client (make sure to provide your own access token)
#     graph = facebook.GraphAPI(access_token='EAAPRgw208KgBO6M5tn6BdJlU03tIHqzQAfROhMfTkeRy20OWdabaLJ2tODGRAotyIfjZCamXNQkgki8pkArwWQHypL9SZAS8K4gnTHn0vZC6eUH13Y1CEB9n3Y0SCTqcRqTkyybaOHu6BZBnxbaFcdalIhGctZB1S0onS9Qd5EZAVXeUfRz58U53ia')

#     # Fetch the post data
#     post = graph.get_object(id=post_id, fields='message,likes.summary(true)')
#     print(f"Facebook Post: {post['message'] if 'message' in post else 'No message available'}")
#     print(f"Likes: {post['likes']['summary']['total_count'] if 'likes' in post else 0}")

# Main execution
# if __name__ == "__main__":
#     # Example URLs (replace with actual ones)
#     # instagram_url = "https://www.instagram.com/reel/DBfFruENVfV/?igsh=MTR2MjRjcHRtM2xiZA=="
#     # twitter_url = "https://twitter.com/elonmusk/status/1440678748958746624"
#     # facebook_url = "https://www.facebook.com/zuck/posts/10103495870489891"
#     facebook_url = "https://www.facebook.com/profile.php?id=100087058047259"
    

#     # print("Fetching Instagram post information...")
#     # fetch_instagram_post(instagram_url)

#     print("\nFetching Facebook post information...")
#     fetch_facebook_post(facebook_url)