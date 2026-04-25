import json
import os

def update_players():
    file_path = 'players.json'
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try: players = json.load(f)
            except: players = []
    else: players = []

    print("--- CuePointe Player Entry ---")
    cp_id = input("CP-ID: ")
    name = input("Player Name: ")
    area = input("Area: ")
    events = input("Events Played: ")
    wins = input("Wins: ")
    score = input("Talent Score: ")
    traits = input("Traits: ")

    new_player = {
        "id": cp_id,
        "name": name,
        "area": area,
        "events": events,
        "wins": wins,
        "score": score,
        "traits": traits
    }

    players.append(new_player)

    with open(file_path, 'w') as f:
        json.dump(players, f, indent=4)
    
    print(f"Done! {name} added.")

if __name__ == "__main__":
    update_players()