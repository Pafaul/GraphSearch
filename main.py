from tree_lib.parse_input_data import *
from tree_lib.node import *

c_n,n_c = get_cities_numbers('cities_to_numbers.txt')
conn = get_cities_connections('map_of_Romania.txt', c_n)
sld = get_cities_sld('sld.txt',c_n)
dist = get_city_to_city_distance('cities_distances.txt', c_n)


root = build_tree_from_info(0, conn, dist)
res = width_search(root, 12)
cities_visited = res.action.split(' ')
res_string = ''
for c in cities_visited:
    res_string += n_c[c] + ' '

print('Route: ', res_string)

res = a_star_search(root, 12, sld)

cities_visited = res.action.split(' ')
res_string = ''
for c in cities_visited:
    res_string += n_c[c] + ' '

print('Route: ', res_string, '; path_cost: ', res.path_cost)