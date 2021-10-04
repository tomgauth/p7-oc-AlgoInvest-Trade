from itertools import combinations
import pandas as pd
import time


def main():

    column_names = ['action id', 'action cost', '2y benefit (%)']

    # Import the data from a csv file as a pandas dataframe
    # Name the columns
    df = pd.read_csv("stock_list.csv", index_col=False, names=column_names)

    # create a column for the value of the action after 2 years
    df['2y value'] = df['action cost'] + \
        (df['action cost'] * df['2y benefit (%)']/100)

    # Create a column showing the Return On Investment (ROI) for each action
    df['2y ROI'] = df['2y value'] - df['action cost']

    # Instantiate an emplty array options to store the different combinations
    # of stocks
    options = []

    # Convert the dataframe to an array of dictionnaries
    stocks_dict = df.to_dict('records')

    # For each length L in the total number of stocks:
    # O(n^2) + 3n
    for L in range(0, len(stocks_dict)+1):
        # Get the subset of combinations of stocks of length L
        for subset in combinations(stocks_dict, L):
            # Convert the returned tuple to an a list
            stocks = list(subset)
            # for each subset of stocks, calculate the sum of costs and ROI
            cost = sum(stock['action cost'] for stock in stocks)
            roi = sum(stock['2y ROI'] for stock in stocks)
            # Create a list of the stocks ids
            stocks_ids = [stock['action id'] for stock in stocks]
            # Create a dict called option with the cost, roi and stocks IDs
            # An option is a combination of stocks
            option = {'totalcost': cost,
                      '2 Year ROI': roi,
                      'Stocks IDs': stocks_ids}
            # If the total cost of the option is less than 500, add it to the
            # options list
            if cost < 500:
                options.append(option)
    # Convert the options list to a pandas dataframe
    df_options = pd.DataFrame(
        options, columns=['totalcost', '2 Year ROI', 'Stocks IDs'])

    # Sort the dataframe to show the best combinations at the top
    df_sorted_options = df_options.sort_values(
        by=['2 Year ROI'], ascending=False)

    # Export the table of sorted options to a csv file
    df_sorted_options.to_csv('output_options.csv')


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
