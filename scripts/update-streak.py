#!/usr/bin/env python3
import requests
import json
from datetime import datetime

def update_streak():
    print("Updating streak counter...")
    # Your streak logic here
    streak_data = {"current_streak": 7, "last_updated": str(datetime.now())}
    
    with open('metrics/streak.json', 'w') as f:
        json.dump(streak_data, f)
    
    print(f"✅ Streak updated: {streak_data['current_streak']} days")

if __name__ == "__main__":
    update_streak()
