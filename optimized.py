import pandas as pd
import time


def main():

    column_names = ['action id', 'action cost', '2y benefit (%)']
    df = pd.read_csv("stock_list.csv", index_col=False, names=column_names)

    # This is the memoization approach of
    # 0 / 1 Knapsack in Python in simple
    df['2y value'] = round(df['action cost'] * df['2y benefit (%)']/100, 2)
    # driver code
    val = df['2y value'].tolist()
    wt = df['action cost'].tolist()
    W = 500
    n = len(val)

    best_stocks = []

    K = [[0 for w in range(W + 1)]
         for i in range(n + 1)]

    # Creating a table of n*W
    # Fill each row (item) with the best value possible
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = round(max(val[i - 1]
                                    + K[i - 1][w - wt[i - 1]],
                                    K[i - 1][w]), 2)
            else:
                K[i][w] = K[i - 1][w]

    # stores the result
    # The value of K[n][W] (last row last column) is the highest
    res = round(K[n][W], 2)
    print("Best 2y ROI is: ", res)

    # Now lets got through the table to find which items
    # compose the highest value
    w = W
    for i in range(n, 0, -1):  # Starting at the bottom
        # if res is 0, there are no more items possible
        if res <= 0:
            break
        # Checks the cell on the top, if the value is the same as
        # the current cell, move up
        # otherwise add the current item (row), remove the value
        # of the item, find the next best item with this value available
        # in the table
        if res == K[i - 1][w]:
            continue
        else:

            # This item is included.
            best_stocks.append(i)

            # Since this weight is included
            # its value is deducted
            res = round(res - val[i - 1], 2)
            w = w - wt[i - 1]

    print("Best stocks IDs: ", best_stocks)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
