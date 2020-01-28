import tweepy
import time

auth = tweepy.OAuthHandler('YOURAUTHKEY')
auth.set_access_token('ACCESS_TOKEN',
                      'TOKENISER2')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()


# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(100)


# Narcist bot
search_string ='frontend developer'
numberOfTweets = 5
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# Generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
#     if follower.name == 'nichu':
#         follower.follow()
#         break
