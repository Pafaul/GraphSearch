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
