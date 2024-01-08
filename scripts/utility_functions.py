import pandas as pd
import os

def read_txt_by_line(file_path):
    '''
    Return list of lines from txt file.
    txt file location determined by file_path arg.

    '''
    
    lines = []
    f = open(file_path, 'r')
    for line in f:
        lines.append(line)
    f.close()
    return lines


def dir_files_list(dir_path):
    return os.listdir(dir_path)


def nullOrEmptyStr(el):
    if el is None:
        return True
    elif pd.isna(el) or pd.isnull(el):
        return True
    elif el == '':
        return True
    else:
        return False