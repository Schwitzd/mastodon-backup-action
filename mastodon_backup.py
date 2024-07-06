import os
import json
import requests
import datetime
from typing import List, Dict
from datetime import datetime
from bs4 import BeautifulSoup

# Environment variables
#MASTODON_ACCESS_TOKEN = os.getenv('MASTODON_ACCESS_TOKEN')
#MASTODON_BASE_URL = os.getenv('MASTODON_BASE_URL')
MASTODON_ACCESS_TOKEN = input("api:")
MASTODON_BASE_URL = 'https://infosec.exchange'

# Fetch posts (toots)

def fetch_posts():
    try:
        headers = {
            'Authorization': f'Bearer {MASTODON_ACCESS_TOKEN}'
        }

        # Verify credentials
        account_response = requests.get(f'{MASTODON_BASE_URL}/api/v1/accounts/verify_credentials', headers=headers)
        account_response.raise_for_status()
        user_id = account_response.json()['id']

        # Fetch posts
        url = f'{MASTODON_BASE_URL}/api/v1/accounts/{user_id}/statuses?exclude_replies=true&exclude_reblogs=true&limit=1000'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def process_posts(posts: List[Dict]) -> List[Dict]:
    posts_json = []

    for post in posts:
        raw_content = BeautifulSoup(post['content'], 'html.parser').text
        created_at = datetime.strptime(post['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%dT%H:%M")
        posts_json.append({
            'created_at': created_at,
            'content': raw_content
        })

    return posts_json


def save_posts(posts_json: List[Dict]) -> None:
    current_year = datetime.now().year
    filename = f'mastodon_posts_{current_year}.json'
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(posts_json, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    posts_list = fetch_posts()

    if posts_list:
        processed_posts = process_posts(posts_list)
        save_posts(processed_posts)
