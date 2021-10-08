import pandas as pd
import time


def main():

    def n_length_combo(lst, n):
        # print("n: ", n)
        if n == 0:
            return [[]]
        l = []
        for i in range(0, len(lst)):  # 0,1,2,3
            # print("   lst[i]: ", lst[i])
            m = lst[i]  # A
            remLst = lst[i + 1:]  # ['B', 'C', 'D']
            # print("   remLst: ", remLst)
            for p in n_length_combo(remLst, n-1):
                # print("     p: ", p)
                l.append([m]+p)
                # print("     l: ", l)
        return l

    column_names = ['action id', 'action cost', '2y benefit (%)']

    # Import the data from a csv file as a pandas dataframe
    # Name the columns
    df = pd.read_csv("stock_list.csv", index_col=False, names=column_names)

    # create a column for the value of the action after 2 years
    df['2y value'] = df['action cost'] * df['2y benefit (%)']/100

    # Instantiate an emplty array options to store the different combinations
    # of stocks
    options = []

    # Convert the dataframe to an array of dictionnaries
    stocks_dict = df.to_dict('records')

    # For each length L in the total number of stocks:
    # O(n^2) + 3n

    for L in range(0, len(stocks_dict)+1):
        # Get the subset of combinations of stocks of length L

        for subset in n_length_combo(stocks_dict, L):
            # Convert the returned tuple to an a list
            stocks = list(subset)
            # for each subset of stocks, calculate the sum of costs and ROI
            cost = sum(stock['action cost'] for stock in stocks)
            value = sum(stock['2y value'] for stock in stocks)
            # Create a list of the stocks ids
            stocks_ids = [stock['action id'] for stock in stocks]
            # Create a dict called option with the cost, roi and stocks IDs
            # An option is a combination of stocks
            option = {'totalcost': cost,
                      '2Y value': value,
                      'Stocks IDs': stocks_ids}
            # If the total cost of the option is less than 500, add it to the
            # options list
            if cost < 500:
                options.append(option)
    # Convert the options list to a pandas dataframe
    df_options = pd.DataFrame(
        options, columns=['totalcost', '2Y value', 'Stocks IDs'])

    # Sort the dataframe to show the best combinations at the top
    df_sorted_options = df_options.sort_values(
        by=['2Y value'], ascending=False)

    # Export the table of sorted options to a csv file
    df_sorted_options.to_csv('output_options.csv')


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
