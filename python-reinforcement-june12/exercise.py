import json
import requests

ottawa_wards_response = requests.get(
    "https://represent.opennorth.ca/boundaries/?sets=ottawa-wards"
)

wards = ottawa_wards_response.json()

for ward in wards["objects"]:
    print(ward["name"])

# Barrhaven
# West Carleton-March
# Somerset
# Rideau-Goulbourn
# Cumberland
# Orléans
# Innes
# Rideau-Rockcliffe
# Rideau-Vanier
# Stittsville
# Alta Vista
# Gloucester-Southgate
# Kitchissippi
# Capital
# River
# Knoxdale-Merivale
# Kanata North
# Gloucester-South Nepean
# College
# Beacon Hill-Cyrville

rep_response = requests.get(
    "https://represent.opennorth.ca/representatives/house-of-commons/"
)
reps = rep_response.json()

print(reps["objects"][0].keys())
# dict_keys(
#     [
#         "gender",
#         "party_name",
#         "first_name",
#         "offices",
#         "representative_set_name",
#         "extra",
#         "related",
#         "source_url",
#         "photo_url",
#         "url",
#         "personal_url",
#         "elected_office",
#         "district_name",
#         "name",
#         "last_name",
#         "email",
#     ]
# )

for rep in reps["objects"]:
    print(f"{rep['first_name']} {rep['last_name']} - {rep['party_name']}")

# James Maloney - Liberal
# Blaine Calkins - Conservative
# Andy Fillmore - Liberal
# Bob Benzen - Conservative
# Jean-Claude Poissant - Liberal
# Francis Drouin - Liberal
# Ron McKinnon - Liberal
# Jonathan Wilkinson - Liberal
# Mark Gerretsen - Liberal
# Gary Anandasangaree - Liberal
# Deepak Obhrai - Conservative
# Erin Weir - Co-operative Commonwealth Federation
# Harjit S. Sajjan - Liberal
# David Sweet - Conservative
# Arnold Viersen - Conservative
# Francesco Sorbara - Liberal
# Andrew Leslie - Liberal
# Kelly Block - Conservative
# Richard Cannings - NDP
# Kim Rudd - Liberal
