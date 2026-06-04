#!/usr/bin/env python3
"""
GitHub Streak Counter
Calculates and updates current contribution streak
"""

import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict

def get_contributions(username: str) -> List[Dict]:
    """Fetch contribution data (simplified version)"""
    
    # Note: For real data, use GitHub GraphQL API with token
    # This is a mock version for demonstration
    
    url = f"https://api.github.com/users/{username}/events"
    headers = {'Accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        events = response.json()
        
        # Count push events
        push_events = [e for e in events if e['type'] == 'PushEvent']
        return push_events
    except:
        return []

def calculate_streak(events: List[Dict]) -> int:
    """Calculate current streak based on events"""
    
    if not events:
        return 0
    
    # Get unique dates
    dates = set()
    for event in events:
        date = event['created_at'][:10]  # YYYY-MM-DD
        dates.add(date)
    
    # Sort dates
    sorted_dates = sorted(dates, reverse=True)
    
    # Calculate streak
    streak = 0
    today = datetime.now().date()
    
    for date_str in sorted_dates:
        event_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        if (today - event_date).days <= streak + 1:
            streak += 1
        else:
            break
    
    return streak

def update_streak_file(streak: int):
    """Update streak data in JSON file"""
    
    streak_data = {
        'current_streak': streak,
        'last_updated': datetime.now().isoformat(),
        'best_streak': max(streak, get_best_streak())
    }
    
    with open('metrics/streak.json', 'w') as f:
        json.dump(streak_data, f, indent=2)
    
    print(f"🔥 Current streak: {streak} days")

def get_best_streak() -> int:
    """Get best streak from stored data"""
    try:
        with open('metrics/streak.json', 'r') as f:
            data = json.load(f)
            return data.get('best_streak', 0)
    except:
        return 0

if __name__ == "__main__":
    username = 'tauhid-topu-007'
    events = get_contributions(username)
    streak = calculate_streak(events)
    update_streak_file(streak)