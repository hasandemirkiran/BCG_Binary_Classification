from venv import create
import pandas as pd 
import numpy as np 
from pathlib import Path  
from datetime import datetime


df_impact = pd.read_csv(f'../../data/evergy/evergy_impact_values_rr.csv', sep=';')
df_features = pd.read_csv(f'../../data/evergy/evergy_input_features.csv', sep=';')
df_concat = pd.concat([df_impact, df_features], axis=1)

# If plan impact is 0, take actual impact
df_concat['A_IMPACT_PLAN'] = np.where(df_concat['A_IMPACT_PLAN'] == (0 or '0'), df_concat['A_IMPACT_ACTUAL'],  df_concat['A_IMPACT_PLAN'] )

# Only get needed columns to calculate success (output) 
df_concat_selected = df_concat[['A_FK_ROADMAP', 'A_IMPACT_PLAN', 'A_IMPACT_ACTUAL', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL']]

# Remove NaN and change datetime objects
df_output_features = df_concat_selected.dropna()
df_output_features[['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL']] = df_output_features[['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL']].apply(pd.to_datetime)
print(df_output_features)
df_output_features['deneme'] = (df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL'] - df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN']).dt.days
print(df_output_features)

# program_end_dto = datetime.strptime('31.12.2025', '%d.%m.%Y')
# df_output_features['success'] = np.where(
#     ((program_end_dto - df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL'])*df_output_features['A_IMPACT_ACTUAL'])
#     /(
#     ((program_end_dto - df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE'])*df_output_features['A_IMPACT_PLAN'])
#     ), 1, 0)