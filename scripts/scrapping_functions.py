import selenium
from bs4 import BeautifulSoup
from configs import *
import requests
import regex
import time


def teams_url_maker(comp, start_year, end_year):
    url = f'https://www.worldfootball.net/players/{comp}-{start_year}-{end_year}/'
    return url


def match_url_maker(comp, year1, year2, team_pair):
    url = f'https://www.worldfootball.net/report/{comp}-{year1}-{year2}-{team_pair[0]}-{team_pair[1]}/'
    return url


def pull_html(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, "html.parser")

    return soup


def extract_teams(soup):
    css_selector = 'td[align] > a[href^="/teams/"] img'
    rows = soup.select(css_selector)
    teams = [row.get('title') for row in rows]

    return teams


def extract_goal_time(string):
    if regex.search('[0-9]+(?=\. /)', string) is not None:
        return  regex.search('[0-9]+(?=\. /)', string).group()
    elif regex.search('[0-9]+(?=\.\+[0-9]+)', string) is not None:
        return regex.search('[0-9]+(?=\.\+[0-9]+)', string).group()
    else:
        return None


def format_team_str(string, adj_map,):
    new_str = string.lower()
    new_str = new_str.replace('&', '')
    new_str = new_str.replace('.', '')

    for key in adj_map.keys():
        new_str = new_str.replace(key, adj_map[key])

    for key in adj_map.keys():
        new_str = new_str.replace(key, adj_map[key])

    new_str = new_str.replace('  ', ' ')
    new_str = new_str.strip().replace(' ', '-')

    return new_str


def matches(teams):
    teams = [format_team_str(team, url_adjustments_map) for team in teams]
    team_pairs = []
    for home in teams:
        for away in teams:
            if home != away:
                team_pairs.append((home, away))
    
    return team_pairs


def match_data(soup):

    results = {}
    css_selector = '.standard_tabelle'
    rows = soup.select(css_selector)
    text_list = [row.text.lower() for row in rows][:2]

    results['match_date'] = extract_str('[0-9]+\. (' + months_str + ') [0-9]{4}', text_list[0])
    results['match_time'] = extract_str('[0-9]{2}:[0-9]{2} clock', text_list[0]).replace(' clock', '')
    results['final_score'] = extract_str('[0-9]+:[0-9]+(?!.*clock)', text_list[0])


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


def match_data_scrapping(years, football_leagues):
    for year_pair in years:
        year1 = year_pair[0]
        year2 = year_pair[1]

        results = []
        fails = []

        for country in football_leagues['team'].keys():
            for comp in football_leagues['team'][country].keys():

                print(f'{year1}-{year2}-{country}-{comp}')

                team_comp_url = football_leagues['team'][country][comp]
                teams_url = teams_url_maker(team_comp_url, year1, year2)
                teams_soup = pull_html(teams_url)
                teams = extract_teams(teams_soup)
                matches_strs = matches(teams)

                results = []
                fails = []
        
                for index, match in enumerate(matches_strs):
                    match_comp_url = football_leagues['match'][country][comp]
                    match_url = match_url_maker(match_comp_url, year1, year2, match)
                    match_soup = pull_html(match_url)

                    try:
                        data = match_data(match_soup)
                        data['country'] = country
                        data['league'] = comp
                        data['season'] = str(year1) + '-' + str(year2)
                        data['home_team'] = match[0]
                        data['away_team'] = match[1]
                        results.append(data)
                    except:
                        fails.append({
                                    'match_date': year1,
                                    'match_time': year2,
                                    'country': country,
                                    'league': comp,
                                    'url': match_url
                                    })

                                
                    time.sleep(1)
                    
                    
                results_df = pd.DataFrame(results)
                fails_df = pd.DataFrame(fails)
                results_df.to_csv(f'output/scrapped_data/match_data/{country}-{comp}-{year1}-{year2}-goal-time.csv', index=False)
                fails_df.to_csv(f'output/scrapping_fails/{country}-{comp}-{year1}-{year2}-fails.csv', index=False)

                time.sleep(60)


