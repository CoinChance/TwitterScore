
# app.py

from flask import Flask, request, jsonify, current_app
from twitter_helper import TwitterHelper
from searchtweets import load_credentials
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()


log_file = os.path.join(os.path.dirname(__file__), 'logs', 'app.log')
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Load credentials once when the application starts
search_args = load_credentials("./twitter_keys_.yaml",
                                yaml_key="search_tweets_v2",
                                env_overwrite=False)


@app.route('/count_tweets', methods=['GET'])
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
