# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
    url = backend_url + endpoint
    print("GET:", url, "PARAMS:", kwargs)

    try:
        response = requests.get(url, params=kwargs)

        print("STATUS:", response.status_code)
        print("RAW RESPONSE TEXT:", response.text)

        # Try to parse JSON
        try:
            parsed = response.json()
            print("PARSED JSON:", parsed)
            return parsed
        except Exception as exc:  # noqa: BLE001 - intentional catch for JSON errors
            print("JSON PARSE ERROR:", exc)
            return None

    except Exception as exc:
        print("NETWORK ERROR:", exc)
        return None


# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/+text
# Add code for retrieving sentiments


def analyze_review_sentiments(text):
    url = sentiment_analyzer_url + "analyze/"
    try:
        response = requests.get(url, params={"text": text})
        print("SENTIMENT RAW TEXT:", response.text)

        try:
            return response.json()
        except Exception as exc:  # noqa: BLE001
            print("JSON PARSE ERROR:", exc)
            return None

    except Exception as exc:
        print(f"Network exception: {exc}")
        return None


# def post_review(data_dict):
# Add code for posting review


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as exc:
        print("Network exception occurred:", exc)
        return None
