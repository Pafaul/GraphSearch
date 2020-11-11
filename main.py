from tree_lib.parse_input_data import *
from tree_lib.node import *

c_n,n_c = get_cities_numbers('cities_to_numbers.txt')
conn = get_cities_connections('map_of_Romania.txt', c_n)

root = build_tree_from_info(0, conn)
res = width_search(root, 12)
cities_visited = res.action.split(' ')
res_string = ''
for c in cities_visited:
    res_string += n_c[c] + ' '

print('Route: ', res_string)