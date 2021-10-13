import sys
import pandas as pd
import time
from math import floor


# run script from command line with dataset as arg
# test

def main():
    # dataset = "stock_list.csv"
    dataset = sys.argv[1]

    W = int(sys.argv[2])
    # print(W)
    W = W*100
    # dataset = "dataset1_Python+P7.csv"
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
    df['profit'] = df['profit'].astype(int)

    df['2y value'] = df['price'] * df['profit'] / 100
    # df['2y value'] = df['2y value'].apply(floor)

    ids = df['name'].tolist()
    val = [i for i in df['2y value'].tolist()]
    wt = [i for i in df['price'].tolist()]

    n = len(val)

    best_stocks = []
    total_cost = 0

    K = [[0 for w in range(W + 1)]
         for i in range(n + 1)]

    # Creating a table of n*W
    # Fill each row (item) with the best value possible
    for i in range(n + 1):
        print(i, "rows out of ", n + 1, " done.")
        for w in range(W + 1):
            # print("col: ", w, " out of ", W + 1)
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                # print("i: ", i)
                # print("w: ", w)
                # print("[i - 1]: ", i-1)
                # print("wt[i - 1]: ", wt[i - 1])
                # print("type(wt[i - 1]): ", type(wt[i - 1]))
                # print("w - wt[i - 1]: ", w - wt[i - 1])
                # print("K[i - 1][w - wt[i - 1]: ",
                #       K[i - 1][round(w - wt[i - 1], 2)])
                K[i][w] = round(max(
                    val[i - 1] + K[i - 1][w - wt[i - 1]],
                    K[i - 1][w]), 2)
            else:
                K[i][w] = K[i - 1][w]

    # print(pd.DataFrame(K))
    # stores the result
    # The value of K[n][W] (last row last column) is the highest
    # res = round(K[n][W], 2)
    res = K[n][W]
    best_2y_roi = round(res / 100, 2)

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
            best_stocks.append(i - 1)
            # Since this weight is included
            # its value is deducted
            res = round(res - val[i - 1], 2)
            w = w - wt[i - 1]

    total_cost = sum(wt[i] for i in best_stocks)
    print("---------------")
    print("Best 2y ROI is: ", round(best_2y_roi/100, 2))
    print("Best stocks IDs: ", [ids[i] for i in best_stocks])
    print("total Cost :", round(total_cost/100, 2))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("The algorithm took %s seconds to complete" %
          (round((time.time() - start_time), 2)))
