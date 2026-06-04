#!/usr/bin/env python3
"""
GitHub Stats Generator
Generates custom statistics for GitHub profile
"""

import json
import requests
from datetime import datetime
from typing import Dict, Any

def fetch_user_stats(username: str) -> Dict[str, Any]:
    """Fetch user statistics from GitHub API"""
    
    url = f"https://api.github.com/users/{username}"
    headers = {'Accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

def generate_stats_json(username: str = 'tauhid-topu-007'):
    """Generate JSON file with user statistics"""
    
    stats = fetch_user_stats(username)
    
    if stats:
        stats_data = {
            'username': stats.get('login'),
            'name': stats.get('name'),
            'followers': stats.get('followers'),
            'following': stats.get('following'),
            'public_repos': stats.get('public_repos'),
            'created_at': stats.get('created_at'),
            'updated_at': datetime.now().isoformat()
        }
        
        # Save to JSON file
        with open('metrics/stats.json', 'w') as f:
            json.dump(stats_data, f, indent=2)
        
        print(f"✅ Stats saved for {username}")
        print(f"📊 Followers: {stats_data['followers']}")
        print(f"📁 Repositories: {stats_data['public_repos']}")
    else:
        print("❌ Failed to fetch statistics")

if __name__ == "__main__":
    generate_stats_json()