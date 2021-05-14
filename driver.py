#%%
import pandas as pd
import datetime as datetime
import os


def CheckBookPrice(pricePoint = None):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    excelpath = r"C:\Users\ryderp\Documents\projects\amazonWebScrape\excels"
    path = r"C:\Users\ryderp\Documents\projects\amazonWebScrape\excels\books.xlsx"
    df = pd.read_excel(path)
    df["checked"] = None
    
    for index,row in df.iterrows():
        print(f"Current price is {row['price_USD']}")
        if row["price_USD"] < pricePoint:
            print(f"Price is below price point \n\n {row}")
            df.loc[index, 'checked']  = pricePoint + row["price_USD"]
            newFileName = f"new_book_{now}.xlsx"

            neFilePath = os.path.join(excelpath,newFileName )
            df.to_excel(neFilePath, index = False )

            return row.to_dict() 
    return None


pricePoint =  50.40
bookCheck = CheckBookPrice(pricePoint=pricePoint)
if bookCheck == None:
    print("no books of interest")
else:
    print(f" There is a book of interest \n\n\n {bookCheck}")
exit()

 # %%
