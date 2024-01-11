from configs import month_map
import pandas as pd
import os
import regex


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


def extract_str(pattern, string):

    if regex.search(pattern, string) is not None:
        return regex.search(pattern, string).group()
    else:
        return None


def format_date_str(string):
    day = regex.search('[0-9]+(?=\.)', string).group()
    month = regex.search('[a-z]+', string).group()
    year = regex.search('2[0-9]{3}', string).group()

    month_num = str(month_map[month])

    date_str = year + '-' + month_num + '-' + day

    return date_str
