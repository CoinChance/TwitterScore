# twitter_helper.py

import re
import os
import pytz
import logging
from datetime import datetime, timedelta
from searchtweets import gen_request_parameters, collect_results
from searchtweets import gen_request_parameters, collect_results

class TwitterHelper:
    @staticmethod
    def extract_account(url):
        # Extract the account from the URL
        pattern = r'https?://(?:www\.)?(?:twitter|x)\.com/(?:#!/)?([A-Za-z0-9_]+)'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            return None

    @staticmethod
    def count_tweets_with_string(twitter_link, search_args, logging):
        
        # Get the value of the TZ environment variable
        tz_env = os.environ.get('TZ', 'UTC')        # default UTC
         # Set the desired timezone based on the TZ environment variable
        desired_timezone = pytz.timezone(tz_env)

        current_datetime = datetime.now(desired_timezone)
        today = current_datetime.strftime("%Y-%m-%d %H:%M")
        yesterday = (current_datetime - timedelta(hours=24)).strftime("%Y-%m-%d %H:%M")
        
        search_string = TwitterHelper.extract_account(twitter_link)
        if search_string is None:
            logging.error("Invalid Twitter link")
            return {"error": "Invalid Twitter link"}
        
        query = gen_request_parameters(f"{search_string} has:mentions -is:retweet",
                                       start_time=yesterday,
                                       end_time=today,
                                       granularity="day",
                                       results_per_call=50)
        logging.info(query)

        try:
            tweets = collect_results(query, result_stream_args=search_args)
            total_tweets = sum(chunk['meta']['total_tweet_count'] for chunk in tweets)
            logging.info(total_tweets)
            return {"total_tweets": total_tweets, "status": 200}
        except Exception as e:
            logging.error(str(e))
            return {"error": str(e), "status": 500}



if __name__ == '__main__':
    twitter_link = "https://twitter.com/SolSnap_"

    from searchtweets import load_credentials

    search_args = load_credentials("./twitter_keys.yaml",
                                    yaml_key="search_tweets_v2",
                                    env_overwrite=False)

    #result = count_tweets_with_string(twitter_link)
    result = TwitterHelper.count_tweets_with_string(twitter_link, search_args)
    print(result)