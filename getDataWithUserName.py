import time
import os
import tweepy
from tweepy import OAuthHandler
import json

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

if __name__ == '__main__':
    # the number of tweet that we want for a specific user
    numberOfTweet = 3000

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    pathForSaveTweets = ""
    listOfNameUser = [] #id or user_id or screen_name

    for item in listOfNameUser:
        if os.path.exists(pathForSaveTweets + "\\" + fileName.split(".")[0]):
            print("file " + fileName + " existed " + str(Counter))
            continue

        tweets = tweepy.Cursor(api.user_timeline, tweet_mode="extended", id=item).items()

        if not (os.path.exists(pathForSaveTweets + "\\" + str(item))):
            os.makedirs(pathForSaveTweets + "\\" + str(item))

        i = 0
        while i < numberOfTweet:
            i = i + 1
            try:
                tweet = tweets.next()

                with open(pathForSaveTweets + "\\" + str(item) + "\\" + str(tweet.id_str) + ".json","w") as tweetFile:
                    json.dump(json.loads(json.dumps(tweet._json)), tweetFile)
            except tweepy.TweepError as e:
                if str(e.reason).find("401") > 0:
                    print("breaked because the user is protected! :" + e.reason)
                    break
                else:
                    print(e.reason)
                    print("sleep for 16 minute... :|")
                    time.sleep(60 * 16)
            except StopIteration:
                print(str(i) + " = StopIteration")
                break


