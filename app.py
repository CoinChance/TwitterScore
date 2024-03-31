
# app.py
import os
import logging
from functools import wraps
from dotenv import load_dotenv
from datetime import datetime, timedelta
from twitter_helper import TwitterHelper
from searchtweets import load_credentials
from flask import Flask, request, jsonify, current_app


# Load environment variables from .env file
load_dotenv()


log_file = os.path.join(os.path.dirname(__file__), 'logs', 'app.log')
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Load credentials once when the application starts
search_args = load_credentials("./twitter_keys_.yaml",
                                yaml_key="search_tweets_v2",
                                env_overwrite=False)


 # Get the value of the RATE_LIMIT and RATE_LIMIT_DURATION environment variables
RATE_LIMIT = int(os.environ.get('RATE_LIMIT', '5'))        # default 5
RATE_LIMIT_DURATION = int(os.environ.get('RATE_LIMIT_DURATION', '15'))        # default 15

WINDOW_DURATION = timedelta(minutes=RATE_LIMIT_DURATION)
request_log = []

def rate_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global request_log
        current_time = datetime.now()

        # Remove old entries from request log
        request_log = [r for r in request_log if current_time - r <= WINDOW_DURATION]

        if len(request_log) >= RATE_LIMIT:
            logging.error({"error": "Rate limit exceeded. Please try again later."})
            return jsonify({"error": "Rate limit exceeded. Please try again later."}), 429

        request_log.append(current_time)
        return func(*args, **kwargs)

    return wrapper

@app.route('/count_tweets', methods=['GET'])
@rate_limit
def count_tweets_route():
    print()
    twitter_link = request.args.get('twitter_link')
    print(twitter_link)
    logging.info(twitter_link)

    if twitter_link:
        result = TwitterHelper.count_tweets_with_string(twitter_link, search_args, logging)
        logging.info(result)
        return jsonify(result), result.get("status", 200)
    else:
        logging.error("Twitter link parameter missing")
        return jsonify({"error": "Twitter link parameter missing"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
