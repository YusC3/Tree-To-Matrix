from argparse import ArgumentParser
from ete3 import Tree
import dendropy
import pandas as pd
import numpy as np
from numpy.random import randint

"""
This is a code meant to be used to obtain pairwise distance from all species in
the tree. The code will return a Nxn Matrix output file, which can be uploaded to
a code to run a certian test, and a file titled 'Distance Matrix',
 which contains a taxon labeled matrix (so the viewer can understand the data visually).
"""

def make_user_interface():
    #defining help string
    help_string = \
    """
    This code will take a some phylogeny tree as it's input and calculate pairwise
    distance between all of its species and out put it in a NxN matrix and a file
    called 'Distance Matrix'.
    """
    parser = ArgumentParser(description = help_string)

    parser.add_argument('-p', '--phylogenetic_tree', help=\
    "input path to phylogenetic tree file")
    parser.add_argument('-t', '--type', help=\
    "input type of format the tree is in ex: NEWICK (or nwk) should be typed in as 'newick'")
    parser.add_argument('-q', '--question', help=\
    "Please type 'y' or 'n'. If yes (y), the data will output as a CSV file")
    return parser

def main():
    """Create Nxn Matrix"""
    parser = make_user_interface()
    #Interpret user interface arguments
    args = parser.parse_args()
    tree_file = args.phylogenetic_tree
    type_t = args.type
    answer = args.question

    # import tree based
    tree = dendropy.Tree.get(
        path = tree_file,
        schema= type_t)

    #conduct pairwaise distance
    pdc = tree.phylogenetic_distance_matrix()

    def create_df_columns_list(pdc):
        #create column list of all species
        column_list = []
        for i, t1 in enumerate(tree.taxon_namespace):
            taxa_label = [str(tree.taxon_namespace[i])]
            column_list += taxa_label
        return column_list

    def rough_matrix(column_list, tree, pdc):
        #Create list for data to make data dict
        lists = []
        #Calculate all pdc for one species
        j = 0
        final_n = len(column_list)
        while j < final_n:
            test_list =[]
            t1 = tree.taxon_namespace[j]
            for i in range(len(column_list)):
                t2= tree.taxon_namespace[i]
                n1 = [pdc(t1, t2)]
                test_list += n1
            lists.append(test_list)
            j += 1
        return (lists)

    def create_dict_with_taxa(column_list, lists):
        #merges list of species with each list of pairwise distance
        dict_of_pdc = dict(zip(column_list, lists))
        return dict_of_pdc

    def answer_to_q(answer, distance_matrix, pdc_dict, column_list):
        #If yes, output file will be create
        if answer == 'y':
            # based on arg -q, it will print answers on scree or create a csv file
            #creates a df that will be turned into a csv file
            output = pd.DataFrame(pdc_dict, index = column_list)
            #create a file named distance_matrix
            output.to_csv('Distance_matrix')
            print(output)
        else:
            print(output)


    column_list = create_df_columns_list(pdc)
    lists = rough_matrix(column_list, tree, pdc)
    distance_matrix =  np.asmatrix(lists)
    # CREATE NXN MATRIX OUTPUT_____
    pdc_dict = create_dict_with_taxa(column_list, lists)

    output = output_format(distance_matrix, pdc_dict, column_list)
    show_data = answer_to_q(answer, output)

    return distance_matrix

if __name__== "__main__":
    main()
