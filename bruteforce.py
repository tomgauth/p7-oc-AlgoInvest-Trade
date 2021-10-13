import sys
import pandas as pd
import time


def main():

    # pass the dataset csv file and the budget as argument
    # ex: python3 dataset.csv 500
    dataset = sys.argv[1]
    W = int(sys.argv[2]) * 100

    def create_df(dataset_csv):
        # Import the data from a csv file as a pandas dataframe
        df = pd.read_csv(dataset, index_col=False)
        # clean up the data set from negative or values equal to 0
        df = df[df['price'] >= 0]
        df['price'] = (df['price']*100).astype(int)
        df['profit'] = (df['profit']*100).astype(int)
        # create a column for the value of the action after 2 years
        df['2y value'] = df['price'] * df['profit']/100

        return df

    # n_length_combo(stocks_dict, L) returns an array of all
    # possible combinations of length n
    def n_length_combo(lst, n):

        # no (more) combinations possible, returns empty array
        if n == 0:
            return [[]]
        l = []
        # for each item in the given length
        for i in range(0, len(lst)):  # 0,1,2,3
            # take the first item
            m = lst[i]  # A
            # define the rest of the list
            remLst = lst[i + 1:]  # ['B', 'C', 'D']
            # recursively apply the same method for the
            # possible lengths on the remaining list
            for p in n_length_combo(remLst, n-1):
                l.append([m]+p)
        # l will contain an array of arrays of possible combinations
        return l

    # For each length L in the total number of stocks:
    # O(n^2) + 3n

    def find_combinations(dataframe):
        # Convert the dataframe to an array of dictionnaries
        stocks_dict = dataframe.to_dict('records')
        # Instantiate an emplty array options to store the different
        # combinations of stocks
        options = []
        # get all the lengths of combinaitions possible
        # (0 to total num of stocks)
        for L in range(0, len(stocks_dict)+1):
            print(L, "/", len(stocks_dict)+1)
            # Get the subset of combinations of stocks of length L
            for subset in n_length_combo(stocks_dict, L):
                # Convert the returned tuple to an a list
                stocks = list(subset)
                # for each subset of stocks, calculate the sum of costs and ROI
                cost = sum(stock['price'] for stock in stocks)
                value = sum(stock['2y value'] for stock in stocks)
                # Create a list of the stocks ids
                stocks_ids = [stock['name'] for stock in stocks]
                # Create a dict called option with the cost, roi and stocks IDs
                # An option is a combination of stocks
                option = {'totalcost': cost / 100,
                          '2Y value': value / 10000,
                          'Stocks IDs': stocks_ids}
                # If the total cost of the option is less than 500,
                # add it to the options list
                if cost < W:
                    options.append(option)
        return options

    # Export the sorted combinations of options into a csv file
    def generate_export_csv(options, output_csv='output_options.csv'):
        # Convert the options list to a pandas dataframe
        df_options = pd.DataFrame(
            options, columns=['totalcost', '2Y value', 'Stocks IDs'])

        # Sort the dataframe to show the best combinations at the top
        df_sorted_options = df_options.sort_values(
            by=['2Y value'], ascending=False)

        # Export the table of sorted options to a csv file
        df_sorted_options.to_csv(output_csv)

    dataframe = create_df(dataset)
    options = find_combinations(dataframe)
    generate_export_csv(options)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
