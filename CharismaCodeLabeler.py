"""
formula to calculate IBS is ==> IBS = (buy_i_volume * sell_counti)/(sell_i_volume * sell_counti)
"""

import requests
from datetime import datetime
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


# from matplotlib import pyplot as plt


# fill the dataframe with asset names
# it gets a code and returns industry and name of the asset
def get_asset_name(asset_code):
    url = "http://www.tsetmc.com/loader.aspx?ParTree=15131M&i=" + str(asset_code)
    asset_attributes = BeautifulSoup(requests.get(url).text, 'html.parser').find('table', {"class": "table1"}).find_all('tr')
    clean_asset_attributes = {attrib.get_text()[1:-1].split("\n")[0]: attrib.get_text()[1:-1].split("\n")[1] for attrib in asset_attributes}
    asset_industry = re.sub('^\u200c', '', str(clean_asset_attributes["گروه صنعت"]).strip())
    asset_name = str(clean_asset_attributes["نماد فارسی"]).strip()
    # print((asset_industry, asset_name))
    return asset_industry, asset_name


all_assets_url = "http://www.tsetmc.com/tsev2/data/ClientTypeAll.aspx"
assets_data = requests.get(all_assets_url).content
# print(assets_data)

temp_raw_data = str(assets_data)[2:-1].split(';')
# print(temp_raw_data[0])

raw_data = [item.split(",") for item in temp_raw_data]
# print(raw_data)

int_data = [[int(i) for i in item] for item in raw_data]
# print(int_data)

headers = ["InsCode", "Buy_Countl", "Buy_CountN", "Buy_I_Volume", "Buy_N_Volume", "Sell_Countl", "Sell_CountN", "Sell_I_Volume", "Sell_N_Volume"]
df = pd.DataFrame(int_data, columns=headers)
# print(df.loc[1, :])

df = df.drop(columns=["Buy_Countl", "Buy_CountN", "Buy_I_Volume", "Buy_N_Volume", "Sell_Countl", "Sell_CountN", "Sell_I_Volume", "Sell_N_Volume"])
# print(df.loc[1, :])


# add name and industry columns
df.insert(1, 'Industry', "null")
df.insert(1, 'Asset_Name', "null")
# print(df.loc[1, :])

# add assets name
for index, row in df.iterrows():
    temp = get_asset_name(row['InsCode'])
    df.loc[index, "Industry"] = temp[0]
    df.loc[index, "Asset_Name"] = temp[1]
print(df.loc[1, :])


df.to_csv("code-name-industry.csv", index=False)
print("All done")
