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

        # Coba parse JSON
        try:
            parsed = response.json()
            print("PARSED JSON:", parsed)
            return parsed
        except Exception as e:
            print("JSON PARSE ERROR:", e)
            return None   # biar caller bisa cek

    except Exception as e:
        print("NETWORK ERROR:", e)
        return None

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments

def analyze_review_sentiments(text):
    url = sentiment_analyzer_url + "analyze/"
    try:
        response = requests.get(url, params={"text": text})
        print("SENTIMENT RAW TEXT:", response.text)

        try:
            return response.json()
        except Exception as e:
            print("JSON PARSE ERROR:", e)
            return None

    except Exception as err:
        print(f"Network exception: {err}")
        return None


# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")