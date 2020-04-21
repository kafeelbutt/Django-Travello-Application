from urllib.request import urlopen
from bs4 import BeautifulSoup

products=[]
prices=[]
ratings=[]
descriptions=[]
images_url=[]

pages_for_scrap = ['https://webscraper.io/test-sites/e-commerce/ajax',
                   'https://webscraper.io/test-sites/e-commerce/ajax/computers']

for quote_page in pages_for_scrap:
    
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')
    
    
    for a in soup.findAll('div',attrs={'class':'col-sm-4 col-lg-4 col-md-4'}):
        name=a.find('a', attrs={'class':'title'})
        price=a.find('h4',attrs={'class':'pull-right price'})
        description=a.find('p',attrs={'class':'description'})
        rating=a.find('p',attrs={'class':'pull-right'})
        image=a.find('img',attrs={'class':'img-responsive'})
        
        products.append(name.text.strip())
        prices.append(price.text.strip())
        descriptions.append(description.text.strip())
        ratings.append(rating.text.strip())
        images_url.append(image['src']+'\n')

import psycopg2
try:
    
    connection = psycopg2.connect(user = "postgres",
                                  password = "1234",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "telusko")

    cursor = connection.cursor()
    
    for (product,price,description,rating,image) in zip(products,prices,descriptions,ratings,images_url):
        cursor.execute("INSERT into table_data_products_scrape(description, price, name, rating, image) VALUES (%s, %s, %s, %s, %s)", (description,float(price.split('$')[1]),product,int(rating.split('reviews')[0]),image))
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into products_scrape table")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")