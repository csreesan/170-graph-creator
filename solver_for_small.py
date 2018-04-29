import random
import os
import sys
from heapq import heappush, heappop
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *
import numpy as np
import pickle
from rutgers_tsp import solve_for_cycle
import operator
import itertools





def cost(input_file, output_file, dist_dict, adjacency_matrix):
    input_data = utils.read_file(input_file)
    output_data = utils.read_file(output_file)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    kingdom_tour = output_data[0]
    conquered_kingdoms = output_data[1]

    kingdom_tour = [list_of_kingdom_names.index(name) for name in kingdom_tour]
    conquered_kingdoms = [list_of_kingdom_names.index(name) for name in conquered_kingdoms]

    return cylce_val(dist_dict, kingdom_tour) + dominating_set_value(adjacency_matrix, conquered_kingdoms)

def output_cost(file_num, dist_dict, adjacency_matrix):
    input_file, output_file = "./inputs/" + file_num + ".in", "./outputs/" + file_num + ".out"
    return cost(input_file, output_file, dist_dict, adjacency_matrix)


############### DOM SET #############################

def get_dominating_set(neighbor_dict, order, number_of_kingdoms):
    con = set()
    sur = set()
    for chosen in order:
        con.add(chosen)
        sur.add(chosen)
        sur.update(neighbor_dict[chosen])
        if len(sur) >= number_of_kingdoms:
            break
    return frozenset(con)

# def get_dom_prob(neighbor_dict, neighbor_cost, adjacency_matrix, number_of_kingdoms):
#     return [(neighbor_cost[i])/(adjacency_matrix[i][i]) for i in range(number_of_kingdoms)]

def softmax(x, temp):
    """Compute softmax values for each sets of scores in x."""
    e_x = (np.exp(x - np.max(x))) / temp
    return e_x / e_x.sum(axis=0) # only difference


def dominating_set_value(adjacency_matrix, dom_set):
    val = 0
    for node in dom_set:
        val += adjacency_matrix[node][node]
    return val




def best_dominating_set(neighbor_dict, neighbor_cost, source_index, number_of_kingdoms, adjacency_matrix, temp, curr_best):

    all_dom = []
    rep_check = set()
    # for i in range(10000):
    #     dom_set = random_dominating_set1(neighbor_dict, neighbor_cost, adjacency_matrix, source_index, number_of_kingdoms)
    #     val = dominating_set_value(adjacency_matrix, dom_set)
    #     if dom_set not in rep_check:
    #         rep_check.add(dom_set)
    #         heappush(all_dom, (val, dom_set))
    # for i in range(10000):
    #     dom_set = random_dominating_set2(neighbor_dict, neighbor_cost, adjacency_matrix, source_index, number_of_kingdoms)
    #     val = dominating_set_value(adjacency_matrix, dom_set)
    #     if dom_set not in rep_check:
    #         rep_check.add(dom_set)
    #         heappush(all_dom, (val, dom_set))


    for i in range(50000):
        dom_set = random_dominating_set2(neighbor_dict, neighbor_cost, adjacency_matrix, source_index, number_of_kingdoms)
        val = dominating_set_value(adjacency_matrix, dom_set)
        if dom_set not in rep_check:
            rep_check.add(dom_set)
            if val < curr_best:
                all_dom.append((val, dom_set))

        if len(all_dom) >= 200:
            break
        

    # for i in range(10000):
    #     dom_set = random_dominating_set3(neighbor_dict, neighbor_cost, adjacency_matrix, source_index, number_of_kingdoms)
    #     val = dominating_set_value(adjacency_matrix, dom_set)
    #     if dom_set not in rep_check:
    #         rep_check.add(dom_set)
    #         heappush(all_dom, (val, dom_set))
    # top10 = []
    # for i in range(20):
    #     if len(all_dom) == 0:
    #         break
    #     top10.append(heappop(all_dom))
    # print("TOP10: ", top10)
    print(len(all_dom))
    return all_dom




######################################### Cycle ##############


def best_cycle(dist_dict, dom_set, source_index):

    has_source = True
    dom_set = set(dom_set)
    if source_index not in dom_set:
        dom_set.add(source_index)
        has_source = False

    best_cycle = None
    for i in range(3):
        cycle = solve_for_cycle(dom_set, dist_dict, source_index)
        val = cylce_val(dist_dict, cycle)
        print("VAL", i, ":", val)
        if best_cycle is None or best_cycle[0] > val:
            print("BEAT: ", i)
            best_cycle = (val, cycle)

    if not has_source:
        dom_set.remove(source_index)

    return best_cycle


def cylce_val(dist_dict, cycle):
    total_cost = 0
    for i in range(len(cycle) - 1):
        total_cost += dist_dict[cycle[i]][cycle[i + 1]]
    return total_cost


def get_path(cycle_order, path_dict):
    path = []
    order_len = len(cycle_order)
    for i in range(order_len - 2):
        path += path_dict[cycle_order[i]][cycle_order[i + 1]]
        path.pop()

    path += path_dict[cycle_order[order_len - 2]][cycle_order[order_len - 1]]
    return path



################# write solutions ##################

def write_output(file_num, solution, list_of_kingdom_names, path_dict, write_to):
    file = open(write_to + file_num + ".out", "w")
    cycle_order = solution[1]
    conquer_set = solution[2]
    path = get_path(cycle_order, path_dict)
    # print(path)
    for i in path:
        file.write(list_of_kingdom_names[i])
        file.write(" ")
    file.write("\n")
    for j in conquer_set:
        file.write(list_of_kingdom_names[j])
        file.write(" ")
    file.close()


######################################## SOLVER ##################
def solver(curr_file, iter_file, beaten_file, write_to, poly2, file_list):

    file_names = []
    for i in file_list:
        file_names.append(str(i) + ".in")

    for file_name in file_names:
        print("#########################")
        print(file_name)
        print("#########################")
        input_data = utils.read_file("./inputs/" + file_name)
        number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
        source_index = list_of_kingdom_names.index(starting_kingdom)

        temp = 1
        file_num = file_name.split(".")[0]
        with open(curr_file, "a") as file_curr:
            file_curr.write(file_num + "\n")  

        poly_path = "./"
        if poly2:
            poly_path = "./dict_poly2/"

        neighbor_dict = pickle.Unpickler(open( poly_path + "neighbors_dict/" + file_num + "_neighbors_dict.p", "rb" )).load()
        neighbor_cost = pickle.Unpickler(open( poly_path + "neighbors_cost/" + file_num + "_neighbors_cost.p", "rb" )).load()

        dist_dict = pickle.Unpickler( open( poly_path + "shortest_dist_dict/" + file_num + "_dist_dict.p", "rb" ) ).load()
        path_dict = pickle.Unpickler( open( poly_path + "shortest_path_dict/" + file_num + "_path_dict.p", "rb" ) ).load()
        curr_best = output_cost(file_num, dist_dict, adjacency_matrix)
        print("CUR BEST:", curr_best)

        all_nodes = list(range(number_of_kingdoms))
        rep = set()
        j = 0
        for order in itertools.permutations(all_nodes):
            j += 1
            with open(iter_file, "w") as file_iter:
                file_iter.write(str(j) + "\n")  
            dom_set = get_dominating_set(neighbor_dict, order, number_of_kingdoms)
            dom_cost = dominating_set_value(adjacency_matrix, dom_set)
            if dom_cost >= curr_best or dom_set in rep:
                continue
            rep.add(dom_set)
            if len(dom_set) > 14:
                continue
            perm = itertools.permutations(list(dom_set))
            cycle_tup=None
            for p in perm:
                cycle = [source_index] + list(p) + [source_index]
                val = cylce_val(dist_dict, cycle)
                if cycle_tup is None or cycle_tup[0] > val:
                    cycle_tup = (val, cycle)


            cycle_cost = cycle_tup[0]
            cycle_path = cycle_tup[1]
            val = dom_cost + cycle_cost
            if curr_best > val:
                with open(beaten_file, "a") as file_beat:
                    file_beat.write(file_num + "\n")
                    file_beat.write("curr_best: " + str(curr_best) + "\n")
                    file_beat.write("new_best: "+ str(val) + "\n" + "\n")
                    print("write")
                best_solution = (dom_cost+cycle_cost, cycle_path, dom_set)
                curr_best = val
                write_output(file_num, best_solution, list_of_kingdom_names, path_dict, write_to)
                

  