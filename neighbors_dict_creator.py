import random
import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *
from dijkstra import *
from os import listdir
from os.path import isfile, join
import pickle




def graph_creator(adjacency_matrix, number_of_kingdoms):
    edge_list = []
    for i in range(number_of_kingdoms):
        for j in range(i):
            weight = adjacency_matrix[i][j]
            if weight == "x":
                continue
            edge_list.append((i,j, weight))
    G = nx.Graph()
    nodelist = range(number_of_kingdoms)
    G.add_weighted_edges_from(edge_list, nodelist=nodelist)
    return G




input_file_path = "./inputs"

# all_input_files = [f for f in listdir(input_file_path) if isfile(join(input_file_path, f))]

all_input_files = []
for i in range(726,753):
    all_input_files.append(str(i) + ".in")
neigbhors_dict_name = "neighbors_dict.p"
neighbors_cost_name = "neighbors_cost.p"

for file_name in all_input_files:
    file_num = file_name.split(".")[0]
    input_data = utils.read_file(input_file_path + "/" + file_name)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
    source_index = list_of_kingdom_names.index(starting_kingdom)
    G = graph_creator(adjacency_matrix, number_of_kingdoms)



    # neighbors_dict_file_name = "./neighbors_dict/" + file_num + "_" + neigbhors_dict_name
    neighbors_cost_file_name = "./neighbors_cost/" + file_num + "_" + neighbors_cost_name

    neighbor_dict = dict()
    neighbor_cost_dict = dict()
    for i in range(number_of_kingdoms):
        neighbor_dict[i] = list(G.neighbors(i))
        total = 0
        for j in neighbor_dict[i]:
            total += adjacency_matrix[j][j]
        neighbor_cost_dict[i] = total

    # pickle.dump( neighbor_dict, open( neighbors_dict_file_name, "wb" ), protocol = 2 )
    pickle.dump( neighbor_cost_dict, open( neighbors_cost_file_name, "wb" ) )
    print(file_num, " done")