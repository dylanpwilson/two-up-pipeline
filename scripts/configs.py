from utility_functions import *


# ---------------------------------------- SQL CONFIGS ---------------------------------------- #
sql_configs_path = 'C:/Users/dylan/Documents/projects/sql_configs.txt'
sql_configs = {el.split(':')[0]: el.split(':')[1].strip() for el in read_txt_by_line(sql_configs_path)}
