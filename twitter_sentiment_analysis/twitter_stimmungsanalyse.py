import json
from textblob import TextBlob
import pandas as pd
import seaborn as sns

with open("data.json", "r") as file:
    twitter_data = file.read()
data = json.loads(twitter_data)
twitter_df = pd.DataFrame(data)

def get_sentiment(text):                   
    t_text = TextBlob(text)                 
    sentiment = t_text.sentiment.polarity   
    if sentiment < -0.2:                    
        return "negative"                   
    elif sentiment > 0.2:
        return "positive"
    else:
        return "neutral"
    
twitter_df["sentiment"] = twitter_df["tweet"].apply(get_sentiment)
obama_df = twitter_df[twitter_df['topic'] =='obama']
obama_df.to_json("obama_tweets_sentiment.json")

sns.set_theme()
sns_obama_theme = sns.histplot(data=obama_df, x='sentiment', color="blue")
sns_obama_theme.set(title="Obama Tweet Semtiment")
sns_obama_theme.get_figure().savefig("Obama_Tweets_Semtiment.png")
sns_obama_theme.figure.clf()
