hotel = {
    "data": {
        "rooms": [
            {"id": 1, "room_number": "201", "capacity": 50},
            {"id": 2, "room_number": "301", "capacity": 200},
            {"id": 3, "room_number": "1B", "capacity": 100},
        ],
        "events": [
            {"id": 1, "room_id": 2, "start_time": 18, "end_time": 20, "attendees": 75},
            {"id": 2, "room_id": 1, "start_time": 10, "end_time": 18, "attendees": 25},
            {"id": 3, "room_id": 2, "start_time": 10, "end_time": 18, "attendees": 20},
            {"id": 4, "room_id": 3, "start_time": 18, "end_time": 21, "attendees": 56},
        ],
    }
}


def retrieve_room_capacity(room_number_input):
    for room in hotel["data"]["rooms"]:
        if room["room_number"] == str(room_number_input):
            return room["capacity"]


# Retrieve the capacity of room 201 and store it in a variable.
rm_201_capacity = retrieve_room_capacity(201)

# Find all the events taking place in room 201. Iterate through them and print "ok" if the number of planned attendees will fit in the room.
def check_capacity():

    for event in hotel["data"]["events"]:
        if event["attendees"] <= rm_201_capacity:
            print(f"Event{event['id']}: ok")


check_capacity()
