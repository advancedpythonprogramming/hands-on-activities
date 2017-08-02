from subway_stations import Direction, Map, Station

# Returns True if there is a path from the origin station to the destination
# station, otherwise False.
# You only can control the variables related to the origin_station, and ready
# station.

def path(origin_station, destination_station):
    global exist_path, route
    exist_path = False
    if search_rec(origin_station, destination_station):
        print("Route: ", end=" ")
        for station in route:
            print(station, end=" ")
        return True
    return False


def search_rec(origin_station, destination_station, past_stations=[]):
    global exist_path, route
    for d in Direction:
        if not exist_path:
            actual_station = origin_station.directions[d]
            past_stations_temp = list(past_stations)
            if actual_station == destination_station:
                past_stations_temp.append(actual_station)
                route = list(past_stations_temp)
                exist_path = True
            elif actual_station not in past_stations_temp and actual_station:
                past_stations_temp.append(actual_station)
                search_rec(actual_station,
                           destination_station,
                           past_stations_temp)
    return exist_path


if __name__ == "__main__":
    map = Map.example_map()
    print(path(map.first_station, map.stations[10]))
    print(path(map.stations[1], map.first_station))
    print(path(map.stations[9], map.stations[14]))
    print(path(map.first_station, map.first_station))
    print(path(map.first_station, map.last_station))
