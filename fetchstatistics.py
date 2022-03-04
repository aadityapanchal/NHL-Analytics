import requests
import re
import pandas as pd

season = ['2021-2022','2020-2021','2019-2020', '2018-2019', '2017-2018', '2016-2017', '2015-2016', '2014-2015', '2013-2014', '2012-2013', '2011-2012', '2010-2011']

team_data = pd.DataFrame()

for team in range(1, 31):
    if team == 11 or team == 27:
        pass

    else:        
        for year in season:
            req = requests.get('https://statsapi.web.nhl.com/api/v1/teams/' + str(team) +'/?expand=team.stats&season='+re.sub("[^0-9]", '',year))
            information = req.json()['teams'][0]['teamStats'][0]['splits'][0]['stat']
            information['Team'] = req.json()['teams'][0]['name']
            information['Year'] = re.sub("[^0-9]", '',year)[-4:]
            team_data = team_data.append(information, ignore_index = True)
        print('Fetched data for team', information['Team'])
print('FETCHED DATA FOR ALL THE TEAMS')
team_data.to_csv('./Data/fetchstatistics.csv')