import pandas as pd
from math import floor

W = 500*100
# dataset = "dataset1_Python+P7.csv"
dataset = "dataset1_Python+P7.csv"
# dataset = "dataset2_Python+P7.csv"
df = pd.read_csv(dataset, index_col=False)
# cleaning up the dataset
# removing rows where price = 0
df = df[df.price >= 0]
# reverting negative values
df['price'] = df['price']*100
df['price'] = df['price'].astype(int)
# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
df['profit'] = df['profit']*100
# df['profit'] = df['profit'].astype(int)
# df['profit'] = df['profit'].apply(floor)
# df['2y value'] = df['price'] * df['profit'] / 10000
df['2y value'] = df['price'] * df['profit'] / 10000
df['2y value'] = df['2y value'].apply(floor)


# My Stocks from dataset 1

set1_correct = ['Share-KMTG', 'Share-GHIZ', 'Share-NHWA', 'Share-UEZB', 'Share-LPDM', 'Share-MTLR', 'Share-USSR', 'Share-GTQK', 'Share-FKJW', 'Share-MLGM', 'Share-QLMK', 'Share-WPLI', 'Share-LGWG', 'Share-ZSDE', 'Share-SKKC', 'Share-QQTU', 'Share-GIAJ', 'Share-XJMO', 'Share-LRBZ', 'Share-KZBL', 'Share-EMOV', 'Share-IFCP']

stocks_dataset1 = ['Share-KMTG', 'Share-GHIZ', 'Share-NHWA', 'Share-UEZB',
            'Share-LPDM', 'Share-MTLR', 'Share-USSR', 'Share-GTQK',
            'Share-FKJW',
            'Share-MLGM', 'Share-QLMK', 'Share-WPLI', 'Share-LGWG',
            'Share-ZSDE', 'Share-SKKC', 'Share-QQTU', 'Share-GIAJ',
            'Share-IHOT',
            'Share-GOEX', 'Share-GSDZ', 'Share-MIOT', 'Share-EWGU',
            'Share-DPMV', 'Share-ICKP', 'Share-RJIB', 'Share-BAPF',
            'Share-QOYO']

# Sienna stocks from dataset 2
sienna_stocks = ["Share-ECAQ",
                 "Share-IXCI",
                 "Share-FWBE",
                 "Share-ZOFA",
                 "Share-PLLK",
                 "Share-YFVZ",
                 "Share-ANFX",
                 "Share-PATS",
                 "Share-NDKR",
                 "Share-ALIY",
                 "Share-JWGF",
                 "Share-JGTW",
                 "Share-FAPS",
                 "Share-VCAX",
                 "Share-LFXB",
                 "Share-DWSK",
                 "Share-XQII",
                 "Share-ROOM"]


def check_2y_value(stock_list):
    total_price = 0
    total_twoyvalue = 0
    for stock_name in stock_list:
        print(stock_name)
        row = df.loc[df['name'] == stock_name]
        print("2y value: ", row['2y value'].values[0])
        total_twoyvalue += row['2y value'].values[0]
        print("price: ", row['price'].values[0])
        total_price += row['price'].values[0]
    print("total_twoyvalue: ", total_twoyvalue/100)
    print("total price: ", total_price/100)
