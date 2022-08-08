from venv import create
import pandas as pd 
import numpy as np 
import pprint 
from pathlib import Path  
from enum import Enum
import argparse
from datetime import datetime

CUSTOMERS = ['nationwide', 'evergy']
PROGRAM_END_DATES = {'nationwide': '31.12.2023', 'evergy': '31.12.2025' }

def create_customer_outputfile(customer):
    df_impact = pd.read_csv(f'../../data/{customer}/{customer}_impact_values_pl.csv', sep=';')
    df_features = pd.read_csv(f'../../data/{customer}/{customer}_input_features.csv', sep=';')
    # df_concat = pd.concat([df_impact, df_features], axis=1

    # If plan impact is 0, take actual impact
    df_impact['A_IMPACT_PLAN'] = np.where(df_impact['A_IMPACT_PLAN'] == (0 or '0'), df_impact['A_IMPACT_ACTUAL'],  df_impact['A_IMPACT_PLAN'] )

    # # Only get needed columns to calculate success (output) 
    # df_concat_selected = df_concat[['A_FK_ROADMAP', 'A_IMPACT_PLAN', 'A_IMPACT_ACTUAL', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL']]

    # Remove NaN and change datetime objects
    df_impact = df_impact.dropna()
    # df_output_features[['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL']] = df_output_features[['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL']].apply(pd.to_datetime)
    # df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN'] = df_output_features.apply(lambda row : datetime.strptime(row['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN'], '%d.%m.%Y %H:%M'), axis=1)  An alternative way to upper ones
    # df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL'] = df_output_features.apply(lambda row : datetime.strptime(row['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL'], '%d.%m.%Y %H:%M'), axis=1) An alternative way to upper ones    
    
    # Old Calculate Success
    # program_end_dto = datetime.strptime(PROGRAM_END_DATES[customer], '%d.%m.%Y')
    # df_output_features['success'] = np.where(
    #     ((program_end_dto - df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL'])*df_output_features['A_IMPACT_ACTUAL'])
    #     /(
    #     ((program_end_dto - df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE'])*df_output_features['A_IMPACT_PLAN'])
    #     ), 1, 0)

    

    # print(df_output_features)

    # # Save the created output features file as csv
    # filepath = Path(f'../../data/{customer}/{customer}_output_features.csv')  
    # filepath.parent.mkdir(parents=True, exist_ok=True)
    # df_output_features.to_csv(filepath)

def create_all_output_files():
    for customer in CUSTOMERS:
       create_customer_outputfile(customer)

def main():
    parser = argparse.ArgumentParser(description='Prepare your output files from your CSVs.')
    parser.add_argument("--create-features", action="store_true", help="To create the output features from your CSVs.")
    args = parser.parse_args()

    if (args.create_features):
        create_all_output_files()
    
      
if __name__ == "__main__":
    main()