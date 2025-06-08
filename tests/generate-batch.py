import requests

from tests.secret import cookies, headers

json_data = {
    'affiliate_short_link': True,
    'list': [
        {
            'item_id': '15727063885',
            'item_name': 'Paket 4 PC 100RB Kaos Mix Brand Matahari Kaos Pria 4 Pcs 100 Ribu | Kaos Pria Branded 100 Ribu 4 Pcs | Kaos Pria | Kaos Distro Pria | Baju Pria | Fashion Pria | Clothes Pria | Atasan Pria Wanita | T-shirt Pria | kaos distro 100 dapat 4 | Dunia Fashion 99',
            'shop_name': 'Dunia_Fashion 99',
            'long_link': 'https://shopee.co.id/universal-link/product/595321248/15727063885?utm_source=an_11304720468&utm_medium=affiliates&utm_campaign=-&utm_content=----',
            'commission_rate': '6%',
            'price': 5140000000,
            'sales': 55796,
            'product_link': 'https://shopee.co.id/product/595321248/15727063885',
            'from_shop_id': '595321248',
        },
    ],
    'sub_ids': [
        '',
        '',
        '',
        '',
        '',
    ],
}

response = requests.post(
    'https://affiliate.shopee.co.id/api/v3/offer/batch_product_links',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.json())
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"affiliate_short_link":true,"list":[{"item_id":"24679921252","item_name":"I13 Pro TWS Headset Bluetooth Bass 9D HiFi Stereo Sound Earphone Wireless Waterproof Headphone Henset Bloetooth with Microphone Sport- bergaransi","shop_name":"Hoki Time","long_link":"https://shopee.co.id/universal-link/product/1171516114/24679921252?utm_source=an_11304720468&utm_medium=affiliates&utm_campaign=-&utm_content=----","commission_rate":"25%","price":2580000000,"sales":5672,"product_link":"https://shopee.co.id/product/1171516114/24679921252","from_shop_id":"1171516114","trace":"{\\"trace_id\\":\\"0.LoOw6wXJ94.100\\",\\"list_type\\":100,\\"exp_group_ids\\":[472643,447777,515643,470135,442993,509408,435409,472595,447311,357113,447104,502629,470152],\\"root_trace_id\\":\\"0.LoOw6wXJ94.100\\",\\"root_list_type\\":100}"},{"item_id":"15727063885","item_name":"Paket 4 PC 100RB Kaos Mix Brand Matahari Kaos Pria 4 Pcs 100 Ribu | Kaos Pria Branded 100 Ribu 4 Pcs | Kaos Pria | Kaos Distro Pria | Baju Pria | Fashion Pria | Clothes Pria | Atasan Pria Wanita | T-shirt Pria | kaos distro 100 dapat 4 | Dunia Fashion 99","shop_name":"Dunia_Fashion 99","long_link":"https://shopee.co.id/universal-link/product/595321248/15727063885?utm_source=an_11304720468&utm_medium=affiliates&utm_campaign=-&utm_content=----","commission_rate":"6%","price":5140000000,"sales":55796,"product_link":"https://shopee.co.id/product/595321248/15727063885","from_shop_id":"595321248","trace":"{\\"trace_id\\":\\"0.yeNkgLwg1G.100\\",\\"list_type\\":100,\\"exp_group_ids\\":[472643,447777,515643,470135,442993,509408,435409,472595,447311,357113,447104,502629,470152],\\"root_trace_id\\":\\"0.yeNkgLwg1G.100\\",\\"root_list_type\\":100}"}],"sub_ids":["","","","",""]}'
#response = requests.post(
#    'https://affiliate.shopee.co.id/api/v3/offer/batch_product_links',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)