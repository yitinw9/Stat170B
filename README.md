# Stat170B
Spring2022 Stat170B Project-Steam video game  recommendation system
## The "How To Use" Guide:
The whole project is divided into 3 phases:

1. Collecting and Processing Steam Raw Data via Web Crawler and API
2. Collecting and Processing Sentiment Raw Data
3. Implementing Steam Recommendations Algorithm

### 1. Collecting Steam Data via Web Crawler and API 
Under the Steam Crawling + Processing folder there are some Notebooks:

-Crawling Steam ID+Process Json.ipynb(by Michelle Sun):
The notebook consists of 3 parts which are Crawl User Id, Processing Gathered Raw User Data, and Retrieving and Processing Game Info From API.
1. Crawl User Id:
For the project we need to have SteamIDs in order to use the Steam API to gather users and games information, so we first crawl SteamIDs on 'https://steamcommunity.com/games/steam/members?p='. The code needs manually changing the range of the community pages, crawling 10-20 pages each time to avoid excceds request limit connection error. The gathered steamIDs were written into txt files 'steamid1.txt' and 'steamid2.txt' in the Sample Ouputs file for use in Steam API.
2.  Processing Gathered Raw User Data:
Reads 'submissions_v3.csv' and 'submissions_v2.csv'(results from Steam API inputing steamIDs done by Yiting Wang) and processing the raw user data into nice dataframe, outputing it as 'users.csv'.
3. Retrieving and Processing Game Info From API:
This part the games' names played by users in users.csv were gathered and used to get Game Information from Steam API, storing Json result of each game in list and processing the results into Game dataframe, outputing as 'game.csv'.


### 2. Collecting and Processing Sentiment Raw Data
Under the Reddit Comment Getting & Processing folder there are several files:

-Getting Reddit comment corresponding to the list of game craw from Steam Data Collecting Reddit Comment Data.ipynb(by Kaixuan Zhang/yiting wang ):
The notebook consists of 2 parts.
1. Getting the Reddit comment by specific game list:
Read the 'game.csv' as a dataframe by numpy, get the related comment from Reddit API through pmaw import PushshiftAPI. Storing the data into the total4800-5012.csv (one example of small part of the total 5012 games).
2. Cleaning and Mining the dataset:
Generating two row of sentimental analysis by the textblob import TextBlob tool, only keep the useful columns as final dataframe: game, polarity, 
subjectivity. Storing the new dataframe as the new total comment dataset.

-SteamIdInfo.ipynb(by yiting wang)
The notebook consists of 1 parts.
1. Access the UserInfo from SteamAPI
Connecting to the SteamAPi first, then read and open the "steamid2.txt" file to use each steam user id as function input, and access the get_owned_games and get_recently_played_games functions in order to acquire related user information from Steam. Finally store the data as 'submissions_v2.csv'.


### 3. Implementing Steam Recommendations Algorithm
-Under the Algorithm folder we use Algorithm.ipynb(by Michelle Sun) to implement the Steam Recommendations System using KNN method of collaborative-filering algorithm. The notebook consists of 3 parts: Data Preprocessing and Scaling, Implementing KNN, and Applying Evaluation Metrics.
1. Data Preprocessing and Scaling:
Read 'users.csv' as pandas dataframe and applying log transformation to some columns where needed to be prepared to use in the algorithm. Read 'game_changed.csv', 'new_sentiment.csv', 'sentiment_4800.csv' and 'rating.csv' as pandas dataframes and applying log transformation and other processing techniques to make the features ready for the algorithm. Combining all the dataframes into one final dataframe called users_combined and output it as 'processed_data.csv'. Splitting the dataset into test and training subdatasets for algorithm.
2. Implementing KNN:
This part of the notebook fits the knn model and outputs the Full Recommendations List for a random user, Final Recommendations List Top 5 for a random user, and a sample of Game-Based Result that outputs 5 recommendations when inputting a random game. The results are shown under parts 1.3, 1.4, and 1.5.
3. Applying Evaluation Metrics:
Here we use three methods: Item-Based Collaborative Filtering, Random Recommendation Algorithm and Popular Games Algorithm and compare the average precison and recall of all the recommendations to users using the test subdataset. The notebook's n_neighbors value can be changed manually to show different results with different k, as well as the Top K variable that controls the number of games in the final result.

-The Demo.ipynb needs 'finalized_model.sav', 'test.csv' to run. The 'finalized_model.sav' saved the model that had already trained to shorten the running time. The result changes everytime you rerun the file for showing different results.



