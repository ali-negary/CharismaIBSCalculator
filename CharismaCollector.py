"""
formula to calculate IBS is ==> IBS = (buy_i_volume * sell_counti)/(sell_i_volume * sell_counti)
"""

import pandas as pd
import numpy as np
import requests
from datetime import datetime
from pytz import timezone


def averageOfAll():
    all_assets_url = "http://www.tsetmc.com/tsev2/data/ClientTypeAll.aspx"
    assets_data_request = requests.get(all_assets_url)
    assets_data = assets_data_request.content
    download_time = datetime.strptime(assets_data_request.headers["Date"], '%a, %d %b %Y %H:%M:%S %Z')
    temp_raw_data = str(assets_data)[2:-1].split(';')
    raw_data = [item.split(",") for item in temp_raw_data]
    int_data = [[int(i) for i in item] for item in raw_data]
    headers = ["InsCode", "Buy_Countl", "Buy_CountN", "Buy_I_Volume", "Buy_N_Volume", "Sell_Countl", "Sell_CountN", "Sell_I_Volume", "Sell_N_Volume"]
    df = pd.DataFrame(int_data, columns=headers)
    df.insert(0, 'TimeStamp', pd.Timestamp(datetime.now(), tz="Iran").replace(microsecond=0))
    df["IBS"] = (df["Buy_I_Volume"] * df["Sell_Countl"]) / (df["Sell_I_Volume"] * df["Buy_Countl"])
    df = df.replace([np.inf, -np.inf], np.nan)
    average_ibs = df.loc[:, "IBS"].astype(float).mean()
    return download_time, round(average_ibs, 5)


def averageOfIndustry(name_of_industry):
    all_assets_url = "http://www.tsetmc.com/tsev2/data/ClientTypeAll.aspx"
    assets_data_request = requests.get(all_assets_url)
    assets_data = assets_data_request.content
    download_time = datetime.strptime(assets_data_request.headers["Date"], '%a, %d %b %Y %H:%M:%S %Z')
    temp_raw_data = str(assets_data)[2:-1].split(';')
    raw_data = [item.split(",") for item in temp_raw_data]
    int_data = [[int(i) for i in item] for item in raw_data]
    headers = ["InsCode", "Buy_Countl", "Buy_CountN", "Buy_I_Volume", "Buy_N_Volume", "Sell_Countl", "Sell_CountN", "Sell_I_Volume", "Sell_N_Volume"]
    df = pd.DataFrame(int_data, columns=headers)
    df.insert(0, 'TimeStamp', pd.Timestamp(datetime.now(), tz="Iran").replace(microsecond=0))
    df["IBS"] = (df["Buy_I_Volume"] * df["Sell_Countl"]) / (df["Sell_I_Volume"] * df["Buy_Countl"])
    # ger rid of the rubbish
    df = df.drop(columns=["Buy_Countl", "Buy_CountN", "Buy_I_Volume", "Buy_N_Volume", "Sell_Countl", "Sell_CountN", "Sell_I_Volume", "Sell_N_Volume"])
    detail_csv = pd.read_csv('code-name-industry.csv')
    # create the time-code-name-industry-IBS dataframe
    result_df = pd.merge(df, detail_csv, on="InsCode")
    result_df.columns = ['TimeStamp', 'InsCode', 'IBS', 'Asset_Name', 'Industry']
    # filter the results by the industry name
    industry_df = result_df.loc[result_df['Industry'] == name_of_industry]
    industry_df = industry_df.replace([np.inf, -np.inf], np.nan)
    average_ibs = industry_df["IBS"].mean()
    return download_time, round(average_ibs, 5)


def oneAsset(asset_name):
    all_assets_url = "http://www.tsetmc.com/tsev2/data/ClientTypeAll.aspx"
    assets_data_request = requests.get(all_assets_url)
    assets_data = assets_data_request.content
    download_time = datetime.strptime(assets_data_request.headers["Date"], '%a, %d %b %Y %H:%M:%S %Z')
    temp_raw_data = str(assets_data)[2:-1].split(';')
    raw_data = [item.split(",") for item in temp_raw_data]
    int_data = [[int(i) for i in item] for item in raw_data]
    headers = ["InsCode", "Buy_Countl", "Buy_CountN", "Buy_I_Volume", "Buy_N_Volume", "Sell_Countl", "Sell_CountN", "Sell_I_Volume", "Sell_N_Volume"]
    df = pd.DataFrame(int_data, columns=headers)
    df["IBS"] = (df["Buy_I_Volume"] * df["Sell_Countl"]) / (df["Sell_I_Volume"] * df["Buy_Countl"])
    # ger rid of the rubbish
    df = df.drop(columns=["Buy_Countl", "Buy_CountN", "Buy_I_Volume", "Buy_N_Volume", "Sell_Countl", "Sell_CountN", "Sell_I_Volume", "Sell_N_Volume"])
    detail_csv = pd.read_csv('code-name-industry.csv')
    # create the time-code-name-industry-IBS dataframe
    result_df = pd.merge(df, detail_csv, on="InsCode")
    result_df.columns = ['InsCode', 'IBS', 'Asset_Name', 'Industry']
    # filter the results by the industry name
    industry_df = result_df.loc[result_df['Asset_Name'] == asset_name]
    average_ibs = industry_df["IBS"].mean()
    return download_time, round(average_ibs, 5)


# print(oneAsset('وبملت'))
# print(averageOfIndustry('محصولات شيميايي'))
# print(averageOfAll())


def collector(choice='all', name='وبملت'):  # choice is one of all, industry, or single. ||| name will be name of industry or asset
    all_assets_url = "http://www.tsetmc.com/tsev2/data/ClientTypeAll.aspx"
    assets_data_request = requests.get(all_assets_url)
    assets_data = assets_data_request.content
    download_time = timezone('UTC').localize(datetime.strptime(assets_data_request.headers["Date"], '%a, %d %b %Y %H:%M:%S %Z'))
    download_time_iran = download_time.astimezone(timezone("Asia/Tehran"))
    temp_raw_data = str(assets_data)[2:-1].split(';')
    raw_data = [item.split(",") for item in temp_raw_data]
    int_data = [[int(i) for i in item] for item in raw_data]
    headers = ["InsCode", "Buy_Countl", "Buy_CountN", "Buy_I_Volume", "Buy_N_Volume", "Sell_Countl", "Sell_CountN", "Sell_I_Volume", "Sell_N_Volume"]
    df = pd.DataFrame(int_data, columns=headers)
    df.insert(0, 'TimeStamp', pd.Timestamp(datetime.now(), tz="Iran").replace(microsecond=0))
    df["IBS"] = (df["Buy_I_Volume"] * df["Sell_Countl"]) / (df["Sell_I_Volume"] * df["Buy_Countl"])
    # ger rid of the rubbish
    df = df.drop(columns=["Buy_Countl", "Buy_CountN", "Buy_I_Volume", "Buy_N_Volume", "Sell_Countl", "Sell_CountN", "Sell_I_Volume", "Sell_N_Volume"])
    if choice == 'asset':
        detail_csv = pd.read_csv('code-name-industry.csv')
        # create the time-code-name-industry-IBS dataframe
        result_df = pd.merge(df, detail_csv, on="InsCode")
        # filter the results by the industry name
        industry_df = result_df.loc[result_df['Asset_Name'] == name]
        average_ibs = industry_df["IBS"].mean()
        print('asset')

    elif choice == 'industry':
        detail_csv = pd.read_csv('code-name-industry.csv')
        # create the time-code-name-industry-IBS dataframe
        result_df = pd.merge(df, detail_csv, on="InsCode")
        result_df.columns = ['TimeStamp', 'InsCode', 'IBS', 'Asset_Name', 'Industry']
        # filter the results by the industry name
        industry_df = result_df.loc[result_df['Industry'] == name]
        industry_df = industry_df.replace([np.inf, -np.inf], np.nan)
        average_ibs = industry_df["IBS"].mean()
        print('industry')

    else:
        df = df.replace([np.inf, -np.inf], np.nan)
        average_ibs = df.loc[:, "IBS"].astype(float).mean()
        print('all')

    return download_time_iran, round(average_ibs, 5)

# print(collector('all'))
