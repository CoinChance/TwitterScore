# TwitterScore
TwitterScore is a Python application that, given a Twitter URL, returns the number of tweets found with mentions of the specified Twitter account.

## Requirements

- Python 3.12.2

## Local Deployment

### Setup

1. Create a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Run the Application

    ```
    python app.py
    ```
    

### Endpoint
The application exposes an endpoint for counting tweets with mentions of a specified Twitter account.

Endpoint: http://127.0.0.1:5000/count_tweets
Parameter: twitter_link (Twitter URL)
For example, you can try the following link in your browser:

http://127.0.0.1:5000/count_tweets?twitter_link=https://twitter.com/SolSnap_


## Docker Deployment
You can also deploy TwitterScore using Docker.

### Build and Run Docker Container

    ```
    docker-compose up --build
    ```
   