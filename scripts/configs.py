from utility_functions import *


# ---------------------------------------- SQL CONFIGS ---------------------------------------- #
sql_configs_path = 'C:/Users/dylan/Documents/projects/sql_configs.txt'
sql_configs = {el.split(':')[0]: el.split(':')[1].strip() for el in read_txt_by_line(sql_configs_path)}



# ---------------------------------------- REGEX CONFIGS ---------------------------------------- #
months_str = 'january|february|march|april|may|june|july|august|september|october|november|december'
days_str = 'monday|tuesday|wednesday|thursday|friday|saturday|sunday'


# ---------------------------------------- SCRAPPING CONFIGS ---------------------------------------- #
league_urls = {

        'english premier league': 'https://www.worldfootball.net/schedule/eng-premier-league-year1-year2-spieltag/'

}

league_rounds = {

        'english premier league': 38

}




months_str = 'january|february|march|april|may|june|july|august|september|october|november|december'
days_str = 'monday|tuesday|wednesday|thursday|friday|saturday|sunday'
# url_adjustments_map = {

#     'é': 'e',
#     'á': 'a',
#     'ö': 'o',
#     'ü': 'u',
#     'í': 'i',
#     'koln': 'koeln',
#     'munchen': 'muenchen',
#     'monchengladbach': 'moenchengladbach',
#     'furth': 'fuerth',
#     'clermont foot 63': 'clermont foot',
#     'brestois': 'brest',
#     'rennais': 'rennes'

# }

# football_leagues = {
#     'team': {
#         'england': {
#             'premier league': 'eng-premier-league'
#         }

#     },

#     'match': {
#         'england': {
#             'premier league': 'premier-league'
#         },
#     }

# }