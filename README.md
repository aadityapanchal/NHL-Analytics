# NHL-Analytics

# CMPT733 - Big Data Project.

### Team Members: [Aditya Bhadreshkumar Panchal](https://github.com/aadityapanchal), [Divye Maheshwari](https://www.github.com/divyemaheshwari), [Hemang Bhanushali](https://www.github.com/ihemangb07), [Priyanka Manam](https://www.github.com/priman15), [Rohit Irvisetty](https://www.github.com/rohitirvisetty)

### Description
Sports statistics are the most important for team managers/coaches to prepare their team better.
Analyzing the optimal positions will help the team to make strategic decisions in choosing
players so as to maximize their winning chances. In addition, the players will be able to learn
about their gameplay from the analysis and make adjustments to improve their on-field
performance.

### Main Datasets
1) Game Stats for each game from season 2015-2016 to 2020-2021:
   https://www.naturalstattrick.com/games.php?fromseason={20152016}&thruseason={20202021}
2) Player position data:
   statsapi.web.nhl.com/api/v1
3) Twitter sentiment analysis:
   Twitter api
4) Fight Statistics from:
   https://www.hockeyfights.com/stats


### How to run:

**Prediction_Modeling.ipynb**: This notebook models and tests the accuracy of game prediction model.

**NHL-Shots-Data-Analysis.ipynb**: 

**Tweet_Sentiment_analysis.ipynb**: This notebook is for analysing fans' sentiments and opinions towards a team using tweets fetched from Twitter.

**fight-analysis.ipynb**: In this notebook, we have analyzed the relationship between game outcomes like goal scoring, puck possession, unblocked shot attempts, match-winning, etc., with fights between players of different teams. 

Further, we have also compared and performed a correlation analysis between teams' performance in the following two matches after they fought in their previous game to understand the psychological impact of a fistfight on the team.

### Dashboard Link
Tableau Dashboard:


### Acknowledgement:
We used a third party tool for feature selection. Since the tool is not a package, we had to import it to our repository.

Source: https://github.com/WillKoehrsen/feature-selector

Credits: Will koehrsen
