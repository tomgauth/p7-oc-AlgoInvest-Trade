import sys
import pandas as pd
import time


def main():

    dataset = sys.argv[1]
    budget = int(sys.argv[2]) * 100

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

    def find_best_stocks(ids, values, prices, budget):
        n = len(values)
        best_stocks = []
        total_cost = 0

        # Create a 2D array of size budget+1 * n+1
        K = [[0 for w in range(budget + 1)]
             for i in range(n + 1)]

        # Go through each row
        for i in range(n + 1):
            print(i, "rows out of ", n + 1, " done.")
            # Fill each row (item) with the best value possible
            for w in range(budget + 1):
                # first row and first column are filled with 0's
                if i == 0 or w == 0:
                    K[i][w] = 0
                    """ If the price of the cell above is less than the budget
                    Remove the current budget w to the current price (column)
                    Add to it the value of the currentcombination
                    unless the value of the previous cell is higher
                    """
                elif prices[i - 1] <= w:
                    K[i][w] = round(max(
                        values[i - 1] + K[i - 1][w - prices[i - 1]],
                        K[i - 1][w]), 2)
                else:
                    # otherwise get the same value as the previous cell
                    K[i][w] = K[i - 1][w]
        # stores the result
        # The value of K[n][budget] (last row last column) is the highest
        res = K[n][budget]
        best_2y_roi = round(res / 100, 2)

        # Now lets got through the table to find which items
        # compose the highest value
        w = budget

        for i in range(n, 0, -1):  # Starting at the bottom
            # if res is 0, there are no more items possible
            if res <= 0:
                break
            """ Checks the cell on the top, if the value is the same as
            the current cell, move up
            otherwise add the current item (row), remove the value
            of the item, find the next best item with this value available
            in the table
            """
            if res == K[i - 1][w]:
                continue
            else:
                # This item is included.
                best_stocks.append(i - 1)
                # Since this weight is included
                # its value is deducted
                res = round(res - values[i - 1], 2)
                w = w - prices[i - 1]

        total_cost = sum(prices[i] for i in best_stocks)
        print("---------------")
        print("Best 2y ROI is: ", round(best_2y_roi/100, 2))
        print("Best stocks IDs: ", [ids[i] for i in best_stocks])
        print("total Cost :", round(total_cost/100, 2))

    df = create_df(dataset)
    ids = df['name'].tolist()
    values = [i for i in df['2y value'].tolist()]
    prices = [i for i in df['price'].tolist()]
    find_best_stocks(ids, values, prices, budget)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("The algorithm took %s seconds to complete" %
          (round((time.time() - start_time), 2)))
