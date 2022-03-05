import requests
import pandas as pd
import numpy as np
import json
import time
!pip install hockey_scraper
import hockey_scraper
import pickle
season_dates=json.loads(requests.get("https://statsapi.web.nhl.com/api/v1/seasons").content)
season_dates_output=[x for x in season_dates["seasons"] if x['regularSeasonStartDate'][0:4]>='2000']
season_results={}
for i in range(len(season_dates_output)):
  dummy_list21=[]
  season_iteration=hockey_scraper.scrape_schedule(season_dates_output[i]["regularSeasonStartDate"],season_dates_output[i]["seasonEndDate"])
  season_results[season_dates_output[i]["regularSeasonStartDate"][0:4]+"_"+season_dates_output[i]["seasonEndDate"][0:4]]=season_iteration

with open('hockey_scrapper.p', 'wb') as i:
    pickle.dump(season_results, i)