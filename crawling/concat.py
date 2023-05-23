import pandas as pd
import os
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def concat(folder_name):
    origin_folder_path = f'../data/{folder_name}'
    search_folder_path = f'./{folder_name}_search'
    f = open(f'./{folder_name}.txt', 'r')
    file_names = f.readlines()
    f.close()
    for ind, file in enumerate(file_names):
        origin_file_path = os.path.join(origin_folder_path, file[:-1])
        search_file_path = os.path.join(search_folder_path, file[:-1])
        
        df2 = pd.read_csv(search_file_path, index_col=0)
        df2.index = pd.to_datetime(df2.index)
        df2.columns = ['Search']
        df2['Search'] = df2['Search'].replace('<1', 0)

        df2 = df2.resample(rule='D').mean()
        df2_interpolated = df2.interpolate(method='linear')

        # load csv file as dataframe
        df_origin = pd.read_csv(origin_file_path, index_col='Date')
        df_origin.index = pd.to_datetime(df_origin.index)

        df = pd.concat([df_origin, df2_interpolated], axis=1)
        df.dropna(inplace=True)
        df.to_csv(f'../data/{folder_name}_clean/{file[:-1]}')