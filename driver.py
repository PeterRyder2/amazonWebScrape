#%%
# 
import pandas as pd
import datetime as datetime
import os
import selenium 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time 
import selenium
from selenium import webdriver
import pprint


def GetDatafromWebsite(url, xpath):
    chromedriver = r"ChromeDriver\chromedriver.exe"
    
    driver = webdriver.Chrome(executable_path=chromedriver)
    driver.get(url)
    time.sleep(5)


    
    price = driver.find_element_by_xpath(xpath)
    
    print(price.text)
    #driver.quit()
    return price.text


def CheckBookPrice(df, pricePoint = None):
    '''

    -open the excel in pandas 
    -iterate through the rows one by one
    - compare todays price with yesterdays
    - if there is price change
            do something interesting 
        else:
            do nothing 
    '''
    for i in df.itterrows():
        pass


    # now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    # excelpath = r"C:\Users\ryderp\Documents\projects\amazonWebScrape\excels"
    # path = r"C:\Users\ryderp\Documents\projects\amazonWebScrape\excels\books.xlsx"
    # df = pd.read_excel(path)
    # df["checked"] = None
    
    # for index,row in df.iterrows():
    #     print(f"Current price is {row['price_USD']}")
    #     if row["price_USD"] < pricePoint:
    #         print(f"Price is below price point \n\n {row}")
    #         df.loc[index, 'checked']  = pricePoint + row["price_USD"]
    #         newFileName = f"new_book_{now}.xlsx"

    #         neFilePath = os.path.join(excelpath,newFileName )
    #         df.to_excel(neFilePath, index = False )

    #         return row.to_dict() 
    # return None




#driver
path = r'excels\books.xlsx'

df = pd.read_excel(path)
dict1 = {}
for index,row in df.iterrows():
    print(row)
    url = row["url"]
    xpath =row["xpath"]
    returnedValue  = GetDatafromWebsite(url, xpath)
    print(returnedValue)

    dict1[url] = returnedValue


    pprint.pprint(dict1)


now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
df[now] = ""
for count, i in enumerate(dict1):
    df.loc[df['url'] == i, [now]] = str(dict1[i]).replace("$", "")

Newpath = os.path.join(r"C:\Users\ryderp\Documents\projects\amazonWebScrape\excels", f"books_{now}.xlsx")

print(df)
df.to_excel(Newpath, index=False)
    



