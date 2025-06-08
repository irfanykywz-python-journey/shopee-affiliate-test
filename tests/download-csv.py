import os.path
import requests

from tests.secret import cookies, headers

url = 'https://affiliate.shopee.co.id/api/v3/offer/csv/3d/affiliate_batch_get_offer_link/LinkProdukSekaligus20250608034349-6db6775409034eef8998b23c1502d22b.csv'

# Send a GET request to the URL
response = requests.get(url, headers=headers, cookies=cookies)
# Check if the request was successful
if response.status_code == 200:
    # Open a local file in binary write mode
    with open(os.path.basename(url), 'wb') as file:
        file.write(response.content)  # Write the content to the file
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")