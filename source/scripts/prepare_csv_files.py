from venv import create
import pandas as pd 
import numpy as np 
import pprint 
from pathlib import Path  
from enum import Enum
import argparse
from datetime import datetime
import seaborn
# import matplotlib.pyplot as plt

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

CUSTOMERS = ['nationwide', 'evergy']
PROGRAM_END_DATES = {'nationwide': '31.12.2023', 'evergy': '31.12.2025' }

def prepare_dataframes(customer):
    df_impact = pd.read_csv(f'../../data/{customer}/impact_values_pl.csv', sep=';')
    df_features = pd.read_csv(f'../../data/{customer}/input.csv', sep=';')

    # Drop Forecast column - not used
    df_impact = df_impact.drop(['A_IMPACT_FORECAST'], axis=1)
 
    # If plan impact is 0 or NULL, take actual impact
    df_impact['A_IMPACT_PLAN'] = np.where(df_impact['A_IMPACT_PLAN'] == (0 or '0'), df_impact['A_IMPACT_ACTUAL'],  df_impact['A_IMPACT_PLAN'] )
    
    # Remove NaN 
    df_impact_no_nan = df_impact.dropna()

    # Remove '.' and Remove after ','
    df_impact_no_nan['A_IMPACT_PLAN'] = df_impact_no_nan['A_IMPACT_PLAN'].str.replace(".","")
    df_impact_no_nan['A_IMPACT_ACTUAL'] = df_impact_no_nan['A_IMPACT_ACTUAL'].str.replace(".",'')
    df_impact_no_nan['A_IMPACT_PLAN'] = df_impact_no_nan['A_IMPACT_PLAN'].apply(lambda row : row.split(',')[0]) 
    df_impact_no_nan['A_IMPACT_ACTUAL'] = df_impact_no_nan['A_IMPACT_ACTUAL'].apply(lambda row : row.split(',')[0]) 

    # Cast to Int
    df_impact_no_nan[['A_IMPACT_PLAN','A_IMPACT_ACTUAL' ]] = df_impact_no_nan[['A_IMPACT_PLAN','A_IMPACT_ACTUAL' ]].astype(int)

    # Calculate Success Rate
    df_impact_no_nan['SUCCESS_RATE'] = np.where((df_impact_no_nan['A_IMPACT_PLAN'] < 0) & (df_impact_no_nan['A_IMPACT_ACTUAL'] > 0), 1, df_impact_no_nan['A_IMPACT_ACTUAL']/df_impact_no_nan['A_IMPACT_PLAN'])
    df_impact_no_nan['SUCCESS_RATE'] = np.where(df_impact_no_nan['SUCCESS_RATE'] > 0.8, 1, 0)

    return df_impact_no_nan


def create_customer_outputfile(customer, output_df):
    # Save the created output features file as csv
    filepath = Path(f'../../data/{customer}/output.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)
    output_df.to_csv(filepath)

def create_all_output_files():
    for customer in CUSTOMERS:
        output_df =  prepare_dataframes(customer)
        print(output_df)
        # create_customer_outputfile(customer, output_df)

def main():
    parser = argparse.ArgumentParser(description='Prepare your output files from your CSVs.')
    parser.add_argument("--create-features", action="store_true", help="To create the output features from your CSVs.")
    parser.add_argument("--show-plots", action="store_true", help="To show the data steps with seaborn.")
    args = parser.parse_args()

    if (args.create_features):
        create_all_output_files()


    
      
if __name__ == "__main__":
    main()