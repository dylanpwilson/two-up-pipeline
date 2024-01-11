import pandas as pd
import requests
import time
import json


# ----------------------------------------------------- API ----------------------------------------------------- #
def odds_api_request(sport, market_type):
    endpoint = f'https://api.the-odds-api.com/v4/sports/{sport}/odds'
    params = {
        'apiKey': 'ff72e22e942b668d9ef538e96f834ad5',
        'regions': 'uk',
        'markets': market_type
    }

    response = requests.get(url=endpoint, params=params)
    response = response.json()

    return response


def save_api_response(response, sport, market_type):

    ts = str(time.time())
    json_object = json.dumps(response, indent=4)

    with open(f'output/api_responses/{sport}-{market_type}-{ts}.json', 'w') as f:
       f.write(json_object)

    f.close()


def unpack_odds_response(response):

    results = []

    for el1 in response:
        for el2 in el1['bookmakers']:
            for el3 in el2['markets']:
                for el4 in el3['outcomes']:
                    
                    data = {}

                    if el3['key'] == 'h2h' and el4['name'] == el1['home_team']:

                        data['league'] = el1['sport_title']
                        data['date'] = el1['commence_time']
                        data['home_team'] = el1['home_team']
                        data['away_team'] = el1['away_team']
                        data['bookie'] = el2['title']
                        data['market'] = el3['key']
                        data['bet'] = 'home wins'
                        data['odds'] = el4['price']
                    
                    elif el3['key'] == 'h2h' and el4['name'] == el1['away_team']:
                        data['league'] = el1['sport_title']
                        data['date'] = el1['commence_time']
                        data['home_team'] = el1['home_team']
                        data['away_team'] = el1['away_team']
                        data['bookie'] = el2['title']
                        data['market'] = el3['key']
                        data['bet'] = 'away wins'
                        data['odds'] = el4['price']
                    
                    elif el3['key'] == 'h2h' and el4['name'] == 'Draw':
                        data['league'] = el1['sport_title']
                        data['date'] = el1['commence_time']
                        data['home_team'] = el1['home_team']
                        data['away_team'] = el1['away_team']
                        data['bookie'] = el2['title']
                        data['market'] = el3['key']
                        data['bet'] = 'draw'
                        data['odds'] = el4['price']
                    
                    elif el3['key'] == 'totals' and el4['name'] == 'Over' and el4['point'] == 2.5:
                        data['league'] = el1['sport_title']
                        data['date'] = el1['commence_time']
                        data['home_team'] = el1['home_team']
                        data['away_team'] = el1['away_team']
                        data['bookie'] = el2['title']
                        data['market'] = el3['key']
                        data['bet'] = 'over2.5'
                        data['odds'] = el4['price']
                    
                    elif el3['key'] == 'totals' and el4['name'] == 'Under' and el4['point'] == 2.5:
                        data['league'] = el1['sport_title']
                        data['date'] = el1['commence_time']
                        data['home_team'] = el1['home_team']
                        data['away_team'] = el1['away_team']
                        data['bookie'] = el2['title']
                        data['market'] = el3['key']
                        data['bet'] = 'under2.5'
                        data['odds'] = el4['price']

                    
                    results.append(data)

    
    return results

                        
# ----------------------------------------------------- API PROCESS ----------------------------------------------------- #
def pull_odds_process(sports, market_types):

    results = []
    for sport in sports:
        for market in market_types:
            response = odds_api_request(sport, market)
            save_api_response(response, sport, market)
            odds_lst = unpack_odds_response(response)
            results = results + odds_lst


    df_odds = pd.DataFrame(results)
    df_odds.dropna(inplace=True)
    ts = str(time.time())
    df_odds.to_csv(f'output/future_odds/future-odds-{ts}.csv', index=False)




