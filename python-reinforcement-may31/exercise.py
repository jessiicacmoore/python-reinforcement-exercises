ballots = [
    {"gold": "Smudge", "silver": "Tigger", "bronze": "Simba"},
    {"gold": "Bella", "silver": "Lucky", "bronze": "Tigger"},
    {"gold": "Bella", "silver": "Boots", "bronze": "Smudge"},
    {"gold": "Boots", "silver": "Felix", "bronze": "Bella"},
    {"gold": "Lucky", "silver": "Felix", "bronze": "Bella"},
    {"gold": "Smudge", "silver": "Simba", "bronze": "Felix"},
]

# Make an empty list to contain participants
participants = []

# Loop through ballots and list participants
for ballot in ballots:
    participants.extend(list(ballot.values()))

# Make a dictionary of participant points and set default of 0 - this also cleans list of duplicate values
participant_points = dict.fromkeys(participants, 0)
# {'Smudge': 0, 'Tigger': 0, 'Simba': 0, 'Bella': 0, 'Lucky': 0, 'Boots': 0, 'Felix': 0}

# Loop through ballots and add points to participant
for ballot in ballots:
    for medal, participant in ballot.items():
        if medal == "gold":
            participant_points[participant] += 3
        if medal == "silver":
            participant_points[participant] += 2
        if medal == "bronze":
            participant_points[participant] += 1
# {"Smudge": 7, "Tigger": 3, "Simba": 3, "Bella": 8, "Lucky": 5, "Boots": 5, "Felix": 5}

# Get key of participant from participant points dictionary with highest value
winner = max(participant_points, key=participant_points.get)
print(winner)
# Bella
