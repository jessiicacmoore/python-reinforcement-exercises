class Location:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Trip:
    def __init__(self):
        self.locations = []

    def __str__(self):
        return self.locations

    def add(self, location):
        if location not in self.locations:
            self.locations.append(location)

    def add_multiple(self, *locations):
        for location in locations:
            self.add(location)

    def make_trip(self):
        if len(self.locations) < 1:
            print("Add destinations to your trip before making a trip")
        else:
            print("Begin trip.")
            for num in range(0, len(self.locations) - 1):
                start_location = self.locations[num]
                end_location = self.locations[num + 1]

                print(f"Travelled from {start_location} to {end_location}")
            print("End trip.")


tor = Location(name="Toronto")
ott = Location(name="Ottawa")
mtl = Location(name="Montreal")
qc = Location(name="Quebec City")
hal = Location(name="Halifax")
sj = Location(name="St. John's")

road_trip = Trip()
road_trip.make_trip()
road_trip.add_multiple(tor, ott, mtl, qc, hal, sj)
road_trip.make_trip()

# Add destinations to your trip before making a trip
# Begin trip.
# Travelled from Toronto to Ottawa
# Travelled from Ottawa to Montreal
# Travelled from Montreal to Quebec City
# Travelled from Quebec City to Halifax
# Travelled from Halifax to St. John's
# End trip.
