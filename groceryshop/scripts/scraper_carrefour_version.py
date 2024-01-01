import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
import json

no_pages = 10

def get_data(pageNo):  
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    # grocery-egyption url
    r = requests.get(f"https://www.carrefouregypt.com/mafegy/ar/c/grocery-egyptian?currentPage={pageNo}&filter=&pageSize=60&sortBy=relevance", headers=headers)
    # dairy-products
    #r = requests.get(f"https://www.carrefouregypt.com/mafegy/ar/c/dairy-egyptian?currentPage={pageNo}&filter=&pageSize=60&sortBy=relevance", headers=headers)
    #fruits-veg-egyptian
    #r = requests.get(f"https://www.carrefouregypt.com/mafegy/ar/c/fruits-veg-egyptian?currentPage={pageNo}&filter=&pageSize=60&sortBy=relevance", headers=headers)
    #beverages-egyptian
    #r = requests.get(f"https://www.carrefouregypt.com/mafegy/ar/c/beverages-egyptian?currentPage={pageNo}&filter=&pageSize=60&sortBy=relevance", headers=headers)
    #delicatessen-egyptian
    #r = requests.get(f"https://www.carrefouregypt.com/mafegy/ar/c/delicatessen-egyptian?currentPage={pageNo}&filter=&pageSize=60&sortBy=relevance", headers=headers)
    #frozen-egyptian
    #r = requests.get(f"https://www.carrefouregypt.com/mafegy/ar/c/frozen-egyptian?currentPage={pageNo}&filter=&pageSize=60&sortBy=relevance", headers=headers)
    content = r.content
    soup = BeautifulSoup(content, features="html.parser")
    json_file = soup.find('script', attrs={'id':'__NEXT_DATA__'}).text
    json_file = json.loads(json_file)
    products = json_file['props']['initialState']['search']['products']
    #print(products)
    alls = []
    for p in products:
        #print(p)
        photo = p['image']
        #print(p['src'])
        desc = p['name']
        price = p['applicablePrice']
        brand = p['brand']

        
        #print(brand.text)
        
        all1=[]

        if desc is not None:
            #print(author.text)
            all1.append(desc)
        else:    
            all1.append('Unknown')
        
        if brand is not None:
            #print(author.text)
            all1.append(brand)
        else:    
            all1.append('Unknown')
        
          

        if price is not None:
            #print(price.text)
            all1.append(price+" EGP")
        else:
            all1.append('0')
            
        if photo is not None:
            #print(n[0]['alt'])
            all1.append(photo['href'])
        else:
            all1.append("unknown-product")
        alls.append(all1)    
        
    return alls

results = []
for i in range(no_pages+1):
    results.append(get_data(i))
#print(results[:10])
# get_data(2)
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Description','Brand', 'Price','Img url'])
print(df.head())
df.to_csv('products.csv', index=False, encoding='utf-8')

# df = pd.read_csv("products.csv")
# print(len(df))
