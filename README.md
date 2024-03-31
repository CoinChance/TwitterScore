# TwitterScore
TwitterScore is a Python application that, given a Twitter URL, returns the number of tweets found with mentions of the specified Twitter account.

## Requirements

- Python 3.12.2
- VPN (as Twitter API was not accessible w/o it.)
- Maximum 5 Calls in 15 minutes (as per twitter basic plan). If plan is upgraded to enterprise, update RATE_LIMIT and RATE_LIMIT_DURATION variables in .env file

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
```bash
    python app.py  
```


### Endpoint
The application exposes an endpoint for counting tweets with mentions of a specified Twitter account.

- Endpoint: http://127.0.0.1:5000/count_tweets
- Parameter: twitter_link (Twitter URL)

For example, you can try the following link in your browser:

http://127.0.0.1:5000/count_tweets?twitter_link=https://twitter.com/SolSnap_
http://127.0.0.1:5000/count_tweets?twitter_link=https://x.com/MochiCat_sol


## Docker Deployment
You can also deploy TwitterScore using Docker.

### Build and Run Docker Container

```bash
    docker-compose up --build
```
   