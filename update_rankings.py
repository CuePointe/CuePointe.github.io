import json
import os

def update_players():
    file_path = 'players.json'
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try: players = json.load(f)
            except: players = []
    else: players = []

    print("--- CuePointe Player Update ---")
    name = input("Player Name: ")
    location = input("Location (e.g., Buziga): ")
    membership = input("Membership (e.g., K.O): ")
    points = float(input("Total Points: "))
    played = int(input("Matches Played: "))

    new_player = {
        "name": name,
        "location": location,
        "membership": membership,
        "points": points,
        "played": played
    }

    players.append(new_player)

    with open(file_path, 'w') as f:
        json.dump(players, f, indent=4)
    
    print(f"Successfully added {name}!")

if __name__ == "__main__":
    update_players()