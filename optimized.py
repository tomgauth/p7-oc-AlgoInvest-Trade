from itertools import combinations
import pandas as pd
import time


def main():
    column_names = ['action id', 'action cost', '2y benefit (%)']
    df = pd.read_csv("stock_list.csv", index_col=False, names=column_names)

    df['2y value'] = df['action cost'] + \
        (df['action cost'] * df['2y benefit (%)']/100)
    df['2y ROI'] = df['2y value'] - df['action cost']
    options = []
    stocks_dict = df.to_dict('records')
    # quadratic complexity O(n^2)
    for L in range(0, len(stocks_dict)+1):
        for subset in combinations(stocks_dict, L):
            stocks = list(subset)
            # O(n)
            cost = sum(stock['action cost'] for stock in stocks)
            # O(n)
            value = sum(stock['2y value'] for stock in stocks)
            # O(n)
            roi = sum(stock['2y ROI'] for stock in stocks)
            # O(n)
            stocks_ids = [stock['action id'] for stock in stocks]
            # O(n)
            option = {'totalcost': cost,
                      '2 Year ROI': roi,
                      'Stocks IDs': stocks_ids}
            if cost < 500:
                options.append(option)
    df_options = pd.DataFrame(
        options, columns=['totalcost', '2 Year ROI', 'Stocks IDs'])
    print(df_options.sort_values(by=['2 Year ROI'], ascending=False))
    df_options.to_csv('output_options.csv')


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
