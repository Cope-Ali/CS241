import numpy as np
import pandas as pd


def main():
    census_data = pd.read_csv("census.csv")
    
    median = census_data.median(0)

    print("The median age is: {}".format(median))

if __name__ == "__main__":
    main()