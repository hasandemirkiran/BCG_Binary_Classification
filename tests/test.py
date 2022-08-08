import pandas as pd
import numpy as np
import os
from datetime import datetime
import math 

# data={'Name':['Karan','Rohit','Sahil','Aryan'],'Age':[23,22,21,24],'Surnname':['demir', 'kiran', 'cayir', 'cimen']}
# df = pd.DataFrame(data)

# print(df)

# df2= df[['Name', 'Age']]

# print(df2)

# date_time_obj1 = datetime.strptime('31.12.2020', '%d.%m.%Y')
# date_time_obj2 = datetime.strptime('30.12.2025', '%d.%m.%Y')
# date_diff = date_time_obj2 - date_time_obj1
# print(type(date_diff.days))


# df_impact = pd.read_csv(f'../../data/evergy/evergy_impact_values.csv', sep=';')
# df_features = pd.read_csv(f'../../data/evergy/evergy_input_features.csv', sep=';')
# df_concat = pd.concat([df_impact, df_features], axis=1)

# # If plan impact is 0, take actual impact
# df_concat['A_IMPACT_PLAN'] = np.where(df_concat['A_IMPACT_PLAN'] == (0 or '0'), df_concat['A_IMPACT_ACTUAL'],  df_concat['A_IMPACT_PLAN'] )

# # Only get needed columns to calculate success (output) 
# df_concat_selected = df_concat[['A_FK_ROADMAP', 'A_IMPACT_PLAN', 'A_IMPACT_ACTUAL', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN', 'INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL']]

# # Remove NaN and change datetime objects
# df_output_features = df_concat_selected.dropna()
# df_output_features.info()
# df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN'] = pd.to_datetime(df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN'])
# df_output_features.info()
# # df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN'] = df_output_features.apply(lambda row : datetime.strptime(row['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_PLAN'], '%d.%m.%Y %H:%M'), axis=1)
# # df_output_features['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL'] = df_output_features.apply(lambda row : datetime.strptime(row['INITIATIVE_LAST_IMPACT_BEARING_MILESTONE_ACTUAL'], '%d.%m.%Y %H:%M'), axis=1)

# print(df_output_features)



x = '20.442'
y = '565,554'

print(math.floor(y))
# print(int(y))