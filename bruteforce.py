from itertools import combinations, product
import pandas as pd
# Create a table with the actions

# Actions, Coût par action (en euros), Bénéfice (après 2 ans)
column_names = ['action id', 'action cost', '2y benefit (%)']
df = pd.DataFrame([
    [1,  20,  5],
    [2,  30,  10],
    [3,  50,  15],
    [4,  70,  20],
    [5,  60,  17],
    [6,  80,  25],
    [7,  22,  7],
    [8,  26,  11],
    [9,  48,  13],
    [10, 34,  27],
    [11, 42,  17],
    [12, 110,  9],
    [13, 38,  23],
    [14, 14,  1],
    [15, 18,  3],
    [16, 8,  8],
    [17, 4,  12],
    [18,   10,  14],
    [19, 24,  21],
    [20, 114, 18]], columns=column_names)

# Define the ROI of each action and add it to the table
# Create a column with the value of each action after 2 years
df['value after 2y'] = df['action cost'] * ((df['2y benefit (%)']*0.01)+1)
print(df)


# Go through the actions one by one
# While budget is < 500€
# add the next action
#

# all I want is all the combinaitions of action cost under 500€

numbers = df['action cost'].tolist()

# result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) <= 500]
result = []

my_dict = df['action cost'].to_dict()

for i in range(len(my_dict)):
    print("i: ", i)
    for index, value in list(combinations(df.index, 2)):
        print(index)
        print(value)
        # print(df.loc[index]['action cost'])
        # print(df.loc[index, :])
        # print(sum(df.loc[index, :]))
        # print('\n')

    for key, value in combinations(values, i):
        # for seq in combinations(df['action cost'], i):
        # print(seq)
        # if sum(seq) <= 50:
        # result.append(seq)
        dict(zip(keys, value))


my_dict = {'A': ['D', 'E'], 'B': ['F', 'G', 'H'], 'C': ['I', 'J']}
my_dict = {'1': 20, '2': 30, '3': 50, '4': 70}
keys, values = zip(*my_dict.items())
permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]

# https://realpython.com/lessons/how-use-itertools-dictionaries/
# https://www.geeksforgeeks.org/group-list-of-dictionary-data-by-particular-key-in-python/
rows = df.to_dict('records') # list of dicts

def key_func(k):
    return k['action cost']


for key, value in combinations(rows, key_func)




