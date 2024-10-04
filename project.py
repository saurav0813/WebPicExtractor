import requests
from bs4 import BeautifulSoup
import os

# Create directory to save images
save_dir = "image/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Define search query
query = 'pwskill'
response = requests.get(f"https://www.google.com/search?q={query}&tbm=isch")  # Use tbm=isch for image search
soup = BeautifulSoup(response.content, 'html.parser')

# Find all image tags
images_tag = soup.find_all("img")

# Remove the first image which is typically a logo or irrelevant
if images_tag:
    del images_tag[0]

# Fetch images if available
for index, img_tag in enumerate(images_tag):
    try:
        img_url = img_tag.get('src')  # or get('data-src') depending on the site structure
        if img_url:
            print(f"Fetching image: {img_url}")
            image_data = requests.get(img_url).content
            with open(os.path.join(save_dir, f"{query.replace(' ', '')}{index}.jpg"), "wb") as f:
                f.write(image_data)
    except Exception as e:
        print(f"Could not fetch image {index}: {e}")

print(len(images_tag))
