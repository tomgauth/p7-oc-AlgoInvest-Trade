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

    # Use a recursive approach to try all the combinations possible
    #
    def combinations(lst):
        # not [] returns True, if the list is not empty, returns False
        # print("lst: ", lst)
        if not lst:
            # Reached the bottom of the recursive tree
            return [[]]
        else:
            # Keep going down the recursive tree
            last_combo = combinations(lst[:-1])
            # print("last_combo: ", last_combo)
            # print("[lst[-1]: ", [lst[-1]])
            # print("r for r in combo: ", [r for r in last_combo])
            return last_combo + [r+[lst[-1]] for r in last_combo]

    def find_combinations(dataframe):
        # Convert the dataframe to an array of dictionnaries
        stocks_dict = dataframe.to_dict('records')
        # Instantiate an emplty array options to store the different
        # combinations of stocks
        options = []

        # Get the subset of combinations of stocks of length L
        for subset in combinations(stocks_dict)[1:]:
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
