from utility_functions import *


# ---------------------------------------- SQL CONFIGS ---------------------------------------- #
sql_configs_path = 'C:/Users/dylan/Documents/projects/sql_configs.txt'
sql_configs = {el.split(':')[0]: el.split(':')[1].strip() for el in read_txt_by_line(sql_configs_path)}


# ---------------------------------------- REGEX CONFIGS ---------------------------------------- #
months_str = 'january|february|march|april|may|june|july|august|september|october|november|december'
days_str = 'monday|tuesday|wednesday|thursday|friday|saturday|sunday'


# ---------------------------------------- SCRAPPING CONFIGS ---------------------------------------- #
league_urls = {

        # 'england premier league': 'https://www.worldfootball.net/schedule/eng-premier-league-year1-year2-spieltag/',
        # 'england championship': 'https://www.worldfootball.net/schedule/eng-championship-year1-year2-spieltag/',
        # 'england league one': 'https://www.worldfootball.net/schedule/eng-league-one-year1-year2-spieltag/',
        # 'england league two': 'https://www.worldfootball.net/schedule/eng-league-two-year1-year2-spieltag/',
        'spain laliga': 'https://www.worldfootball.net/schedule/esp-primera-division-year1-year2-spieltag/',
        'spain laliga 2': 'https://www.worldfootball.net/schedule/esp-segunda-division-year1-year2-spieltag/',
        'italy serie a': 'https://www.worldfootball.net/schedule/ita-serie-a-year1-year2-spieltag/',
        'italy serie b': 'https://www.worldfootball.net/schedule/ita-serie-b-year1-year2-spieltag/',
        'germany bundesliga': 'https://www.worldfootball.net/schedule/bundesliga-year1-year2-spieltag/',
        'france ligue 1': 'https://www.worldfootball.net/schedule/fra-ligue-1-year1-year2-spieltag/'

}

league_rounds = {

        'england premier league': 38,
        'england championship': 46,
        'england league one': 46,
        'england league two': 46,
        'spain laliga': 38,
        'spain laliga 2': 42,
        'italy serie a': 38,
        'italy serie b': 38,
        'germany bundesliga': 34,
        'france ligue 1': 38 

}

