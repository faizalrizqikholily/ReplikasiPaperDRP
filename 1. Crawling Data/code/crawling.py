import snscrape.modules.twitter as sntwitter
import pandas as pd

pd.options.display.max_colwidth = 500

query1="penundaan pemilihan umum since:2022-01-01 until:2022-02-23"
query2="penundaan pemilihan umum since:2022-02-24 until:2022-05-27"

tweets=[]
limit=500
# %time
try:
    print("crawl start")
    for tweet in sntwitter.TwitterSearchScraper(query=query1).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content])


    df1 = pd.DataFrame(tweets, columns=['datetime','username','content'])
    df1['datetime'] = df1['datetime'].apply(lambda a: pd.to_datetime(a).date()) 

    tweets=[]    

    for tweet in sntwitter.TwitterSearchScraper(query=query2).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content])


    df2 = pd.DataFrame(tweets, columns=['datetime','username','content'])
    df2['datetime'] = df2['datetime'].apply(lambda a: pd.to_datetime(a).date()) 


    with pd.ExcelWriter("crawl1.xlsx") as writer:
        df1.to_excel(writer, sheet_name="before", index=True)
        df2.to_excel(writer, sheet_name="after", index=True)
except Exception as e:
    print(e)

print("done")