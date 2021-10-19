# Openclassrooms Project 7
# AlgoInvest&Trade

The project was designed for the specific needs of the project 7 on Openclassrooms' track "Python App Developper"

This program has been developped to offer an efficient solution to the following problem:
given a list of stocks with corresponding prices and profit and a limited budget, what is the optimal combination of stocks to buy to get the highest return on investment.

This program contains 2 main files "bruteforce.py" and "optimized.py" that offer 2 different algorithms to solve this problem.


## Installation

Download the repository on your computer.

Make sure that you're using the right requirements by running the following command:

```bash
pip install -r requirements.txt
```

## Syntax for bruteforce.py and optimized.py

Use the input csv file as a first argument
Enter the budget as a second argument

```bash
python bruteforce.py input_file.csv 500
python optimized.py input_file.csv 500
```

The bruteforce algorithm is much more time consuming than the optimized algorithm, therefore it takes too long to process the datasets:

- dataset1_Python+P7.csv
- dataset2_Python+P7.csv

## Outputs

- The bruteforce algorithm will generate a file output_options.csv showing all the combinations

- The optimized algorithm will display the cost, return on investment and stocks in the terminal

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
Name: Tom Gauthier
Github: https://github.com/tomgauth
