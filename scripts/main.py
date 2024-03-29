from scrapping_functions import *
from api_functions import *
from configs import *


SEASONS = [(2019, 2020), (2020, 2021), (2021, 2022), (2022, 2023), (2023, 2024)]
LEAGUES = [key for key in league_urls.keys()]
SPORTS = ['soccer_epl']
MARKET_TYPE = ['h2h', 'totals']
SCRAPE_MATCH_DATA = False
STORE_MATCH_DATA = True
PROCESS_MATCH_DATA = False
PULL_FUTURE_ODDS = False


if SCRAPE_MATCH_DATA:
    match_scraping_process(SEASONS=SEASONS, LEAGUES=LEAGUES)

if STORE_MATCH_DATA:
    pass


if PROCESS_MATCH_DATA:
    pass


if PULL_FUTURE_ODDS:

    pull_odds_process(SPORTS, MARKET_TYPE)



