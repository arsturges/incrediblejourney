import twitter

consumer_key = 'nzAYHwT3zpaTWh1YkcYrJvSDG'
consumer_secret = 'RhSMn5UjGRrporcB4pf6OpUfx0wDFJVAQ4KpCQ3ub2PrYoSCMd'
access_token_id = '281554638-lLqDYqrEmut8szHujhDiuVJwqKns6k72vN11knKw'
access_token_secret = '4rVEt3oJHddy6Gzi209GHrc5KpKk7YLngjOtOiMJYURcR'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_id,
                  access_token_secret=access_token_secret)

search_phrase = 'journey'
statuses = api.GetSearch(term=search_phrase)

for s in statuses:
    try:
        s.retweeted_status
    except AttributeError:
        # good, it's not a retweet
        print s.text
