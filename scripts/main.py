from utility_functions import *
from sql_functions import *
from configs import *
import pandas as pd


STORE_SCRAPPED_DATA = True
SCRAPPED_DATA_PATH = 'input/scrapped_data/'
DATABASE_NAME = 'football'
TABLE_NAME = 'matches_scrapped_data'


if STORE_SCRAPPED_DATA:
    files = dir_files_list(SCRAPPED_DATA_PATH)
    for file in files:
        df = pd.read_csv(f'input/scrapped_data/{file}')
        df.rename(columns={'date': 'match_date',
                           'time': 'match_time',
                           'home': 'home_team',
                           'away': 'away_team'
                           }, inplace=True)

        for index, row in df.iterrows():
            row_dct = row.to_dict()
            sql_cnx = sql_connection(sql_configs['host'], sql_configs['user'], 
                                     sql_configs['password'], DATABASE_NAME)
            sql_insert_data_pt(sql_cnx, TABLE_NAME, row_dct)
            
            

