from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

starturl="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser=webdriver.Chrome("chromedriver.exe")
browser.get(starturl)

scraped_list=[]

# scrapping function
def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    # to find <table>
    bright_star_table= soup.find("table",attrs={"class","wikitable"})
    #to find <tbody>
    table_body=bright_star_table.find('tbody')
    # to find <tr>
    table_rows=table_body.find_all('tr')

    #loop to get data from <tr>
    for rows in table_rows:
        table_cols=rows.find_all("td")
        #print(table_cols)

        temp_list=[]

        #loop for printing data in text using .text
        for col_data in table_cols:
            data=col_data.text.strip()
            #print(data)
            temp_list.append(data)
        
        #to append data in stars
        scraped_list.append(temp_list)

#running the above function
scrape()

stars_data=[]

for i in range(0,len(scraped_list)):

    Star_names = scraped_list[i][1]
    Distance = scraped_list[i][3]
    Mass = scraped_list[i][5]
    Radius = scraped_list[i][6]
    Lum = scraped_list[i][7]

    required_data=[Star_names,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)

print(stars_data)

#define headers
headers=["Star_names", 'Distance' ,' Mass' , 'Radius','Luminosity']
#creating a dataframe
stars_df1=pd.DataFrame(scraped_list,columns=headers)
#saving df
stars_df1.to_csv('scraped_data.csv',index=True,index_label="id")










