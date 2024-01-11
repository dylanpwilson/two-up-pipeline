from configs import months_str
from utility_functions import extract_str
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests
import regex
import time


# ----------------------------------------------------- MATCH SCRAPING FUNCTIONS ----------------------------------------------------- #
def football_league_urls(seasons, leagues):
    from configs import league_urls
    from configs import league_rounds

    urls = {}
    for league in leagues:

        urls[league] = {}
        last_round = league_rounds[league]
        for years in seasons:

            rounds = [el for el in range(1, last_round+1)]
            output = []

            for r in rounds:
                old_url = league_urls[league]
                new_url = old_url.replace('year1', str(years[0])).replace('year2', str(years[1]))
                new_url = new_url + str(r) + '/'
                output.append(new_url)
            
         
            urls[league][str(years[0])+'-'+str(years[1])] = output

    return urls


def pull_html(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, "html.parser")

    return soup


def extract_match_url(soup):
    selector = 'a[title^="Match details"]'
    rows = soup.select(selector)
    match_urls = ['https://www.worldfootball.net' + row.get('href') for row in rows]

    return match_urls


def extract_goal_time(string):
    if regex.search('[0-9]+(?=\. /)', string) is not None:
        return  regex.search('[0-9]+(?=\. /)', string).group()
    elif regex.search('[0-9]+(?=\.\+[0-9]+)', string) is not None:
        return regex.search('[0-9]+(?=\.\+[0-9]+)', string).group()
    else:
        return None


def extract_teams(soup):
    selector = 'th a[href]'
    rows = soup.select(selector)
    teams = [row.get('title') for row in rows]
    return teams


def extract_match_data(soup):

    results = {}
    css_selector = '.standard_tabelle'
    rows = soup.select(css_selector)
    text_list = [row.text.lower() for row in rows][:2]

    results['match_date'] = extract_str('[0-9]+\. (' + months_str + ') [0-9]{4}', text_list[0])
    results['match_time'] = extract_str('[0-9]{2}:[0-9]{2} clock', text_list[0]).replace(' clock', '')
    results['final_score'] = extract_str('[0-9]+:[0-9]+(?!.*clock)', text_list[0])

    teams = extract_teams(soup)
    results['home_team'] = teams[0]
    results['away_team'] = teams[1]

    if results['final_score'] == '0:0':
        return results
    else:
        goals_list = regex.split('\n', text_list[1])
        goals_list = [text for text in goals_list if text != '']
        goals_list = [text for text in goals_list if text != 'goals']
        goals = {}
        home = 0
        score_index = [index for index, text in enumerate(goals_list) if 
                       regex.search('[0-9]+:[0-9]+', text.replace(' ', '')) is not None]
        for index in score_index:
            new_home_score = int(goals_list[index].replace(' ', '').split(':')[0])
            goal_time = extract_goal_time(goals_list[index+1])
            if new_home_score > home:
                goals[goal_time] = 'home'
                home += 1
            else:
                goals[goal_time] = 'away'
        
        results['goals'] = goals
        return results


# ----------------------------------------------------- MATCH SCRAPING PROCESS ----------------------------------------------------- #
def match_scraping_process(SEASONS, LEAGUES):
    
    urls = football_league_urls(seasons=SEASONS, leagues=LEAGUES)

    for league in urls.keys():

        for season in urls[league].keys():

            scraped_data = []
            scraped_data_fails = []
            for round_url in urls[league][season]:
                round_soup = pull_html(round_url)
                match_urls = extract_match_url(round_soup)

                for match_url in match_urls:
                    round_number = extract_str('/[0-9]+/', round_url).replace('/', '')
                    print('round: ' + round_number + ' url: ' + match_url)
                    match_soup = pull_html(url=match_url)
                    try:
                        match_data = extract_match_data(match_soup)
                        match_data['season'] = season
                        match_data['round'] = int(round_number)
                        scraped_data.append(match_data)
                    except:
                        fails = {}
                        fails['round'] = int(round_number)
                        fails['season'] = season
                        fails['match_url'] = match_url
                        scraped_data_fails.append(fails)

            df = pd.DataFrame(scraped_data)
            df.dropna(inplace=True)
            df_fails = pd.DataFrame(scraped_data_fails)
            df_fails.dropna(inplace=True)
            df.to_csv(f'output/scraped_data/success/{league.replace(" ", "-")}-{season}.csv', index=False)
            df_fails.to_csv(f'output/scraped_data/fail/{league.replace(" ", "-")}-{season}-scraping-fails.csv', index=False)


# ----------------------------------------------------- UPCOMING ODDS SCRAPING FUNCTIONS ----------------------------------------------------- #