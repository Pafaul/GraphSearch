MAIN_SEPARATOR = '->'
def get_cities_numbers(filename):
    cities_numbers = {}
    numbers_cities = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            city,number = line.strip().split(MAIN_SEPARATOR)
            cities_numbers[city] = number
            numbers_cities[number] = city
    return cities_numbers,numbers_cities

def get_cities_connections(filename, cities_numbers):
    connections = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            city,city_connections = line.strip().split(MAIN_SEPARATOR); city_number = cities_numbers[city]
            city_connections = city_connections.split(',')
            connections[city_number] = []
            for connection in city_connections:
                connections[city_number].append(cities_numbers[connection])
    return connections

def get_cities_sld(filename, cities_numbers):
    sld = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            city,cost=line.strip().split(MAIN_SEPARATOR)
            sld[cities_numbers[city]] = int(cost)
    return sld

def get_city_to_city_distance(filename, cities_numbers):
    dist = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            city1,city2,cost=line.strip().split(MAIN_SEPARATOR)
            city1N = cities_numbers[city1]
            city2N = cities_numbers[city2]
            dist[city1N + ' ' + city2N] = int(cost)
            dist[city2N + ' ' + city1N] = int(cost)
    return dist