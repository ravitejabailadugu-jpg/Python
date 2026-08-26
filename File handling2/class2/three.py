import requests,json,csv

product_resp=requests.get('https://dummyjson.com/products')
product_data=product_resp.json()
print(type(product_data))
products=product_data['products']
print(type(products))




beauty_product