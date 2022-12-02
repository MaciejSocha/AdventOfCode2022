import string
import pandas as pd


def read_data_to_df(file_location: string):
    data = pd.read_table(file_location, header=None)
    return data
