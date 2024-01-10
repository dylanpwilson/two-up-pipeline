from scrapping_functions import *

SEASONS = [(2019, 2020), (2020, 2021), (2021, 2022), (2022, 2023), (2023, 2024)]
LEAGUES = ['english premier league']

scraping_process(SEASONS=SEASONS, LEAGUES=LEAGUES)

# test = football_league_urls(SEASONS, LEAGUES)
# print(test.keys())

