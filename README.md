# CMPT733 - Big Data Lab 2 Project
## NHL Ice Hockey Analytics
Sports analytics and prediction is one of the renowned fields where data science is being adopted at a fast pace. Sports analytics and prediction allow team management to stay updated on a team's performance. Our project is aimed at providing a one stop solution to the Team Management by providing solution to following four problems
- What is the outcome of the upcoming matches?
- How to optimally position the players to create more Goal-Scoring opportunities and have a stronger defence?
- Find the impact of in-game fights on the team's performance in the current and upcoming two matches?
- What is the fans' sentiment towards teams' performance, team and management updates?

### Team Members: 
- [Aditya Panchal](https://github.com/aadityapanchal)
- [Divye Maheshwari](https://www.github.com/divyemaheshwari)
- [Hemang Bhanushali](https://www.github.com/ihemangb07)
- [Priyanka Manam](https://www.github.com/priman15)
- [Rohit Irvisetty](https://www.github.com/rohitirvisetty)

### Datasets:
- [Game Stats for each game](https://www.naturalstattrick.com/games.php?fromseason={20152016}&thruseason={20202021})
- [Player position data](statsapi.web.nhl.com/api/v1)
- [Twitter sentiment analysis](https://developer.twitter.com/en/docs/twitter-api)
- [Fight Statistics](https://www.hockeyfights.com/stats)

### Evnironment Setup:
Our project requires a few Python modules to be installed. Use `pip install -r requirements.txt` to setup the dependencies locally.

### Code Structure:
- **Prediction_Modeling.ipynb**: Python notebook to develop ML models and tests their accuracy by predicting upcoming games 

- **NHL-Shots-Data-Analysis.ipynb**: Python notebook to analyze the optimal position of players for both attack and defence strategy

- **Tweet_Sentiment_analysis.ipynb**: Python notebook is for analysing fans' sentiments towards a team using tweets fetched from Twitter

- **fight-analysis.ipynb**: Python notebook to anaylze the impact of in-game physical fights between player on various game statistics such as game results, goals scored, puck possession. Additionally, it also evaluates the impact of the fight on the team's performance in their next two matches

### Dashboard Link:
- [Top 4 Player Goal scoring region](https://public.tableau.com/app/profile/hemang6825/viz/Top_player_shots/Top4players?publish=yes)

- [Attacking Strategy for Toronto Maple Leafs against Vancouver Canucks](https://public.tableau.com/app/profile/hemang6825/viz/Shot_analysis/AttackingpositionforTorontoMapleLeafs?publish=yes)

- [Defensive Strategy For Toronto Maple Leafs against Vancouver Canucks](https://public.tableau.com/app/profile/hemang6825/viz/Shot_analysis/DefensivePositionforTorontoMapleLeafs?publish=yes)

- [Home Goal Away Goal Analysis](https://public.tableau.com/app/profile/hemang6825/viz/Team_statistics/GoalsScoredAnalysis?publish=yes)

- [Match_Prediction](https://public.tableau.com/app/profile/hemang6825/viz/Match_Prediction/Dropdown-Prediction#1)

- [Impact of in-game fights on game outcomes](https://public.tableau.com/app/profile/hemang6825/viz/Final_Notebook-Copy2/Plotsforcorrelationbetweenfightsandgameoutcomes?publish=yes)


- [Impact of in-game fights on outcomes of two successive matches](https://public.tableau.com/app/profile/hemang6825/viz/Final_Notebook-Copy2/Plotsforcorrelationbetweenfightsandgameoutcomesintwosuccessivematches?publish=yes)


- [Fan's Sentiment towards Toronto Maple Leafs on Twitter](https://public.tableau.com/app/profile/hemang6825/viz/Final_Notebook-Copy2/PublicOpiniontowardsTorontoMapleLeafsonTwitter?publish=yes)

- [Team wise Fan's on Twitter](https://public.tableau.com/app/profile/hemang6825/viz/Final_Notebook-Copy2/FansSentimentsonTwitter?publish=yes)

### Acknowledgement:
For Feature Selection, we used an externally developed third party tool [Feature_Selector](https://github.com/WillKoehrsen/feature-selector) by `Will koehrsen`. Since it is currenlty not developed as a python package, we have added the required files to our code base. 
