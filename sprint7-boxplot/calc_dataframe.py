"""
Author: Bruno Silva
Date: June 2th of 2020
"""

from openpyxl import load_workbook
import seaborn as sns
import pandas as pd
import os
import matplotlib.pyplot as plt

# calc the dictionary wich will be used to generate the data frame

def calc_dataframe():
    """
                            | miRNA 1 | miRNA 2 | miRNA 3 ...
    -----------------------------------------------------
    Plasmodium Falciparum   |         |         |
    -----------------------------------------------------
    Plasmodium Vivax        |         |         |
    -----------------------------------------------------
    Plasmodium Ovale        |         |         |
            .
            .
            .
    """

    # TODO: iterate over predictions
    path = os.path.join(os.getcwd(), 'input', 'miRDB_prediction_files')
    list_files = os.listdir(path)
    print(list_files)

    """
    Collums of prediction file
    [ ] - Collums to check
    
    [A] - Organismo
     B  - Gene
     C  - #miRNA (Humans)
     D  - Size
    [E] - miRNA 100
    [F] - Nomes 100
    """

    di = {}
    """
    di = {'mirna' = [1, 2, 3, 4, 5, 6, 7, 8]} 
    """

    # adjust for the mirnas
    with open(os.path.join(os.getcwd(), 'output', 'df_mirnas.csv'), 'r') as f:
        for line in f.readlines():
            mirna = line.replace('\n', '')
            di[mirna] = [0] * len(list_files)

    list_mirna_absents = []
    for index, file in enumerate(list_files):
#         print(file)

        # TODO: open a prediction sheet file wich correspond to the organism
        file_path = os.path.join(path, file)
        book = load_workbook(file_path)
        sheet = book.active

        # TODO: iterate over the sheet lines until the empty line
        i = 2
        while True:
            # TODO: get organism name
            organism = sheet['A' + str(i)].value
            mirna = sheet['F' + str(i)].value

            if organism == None and mirna == None:
                break

            else:

                # TODO: Find, at the miRNA 100 collum, values diferent of zero
                nu_mirna_100 = sheet['E' + str(i)].value
                # print(nu_mirna_100, nu_mirna_100 == None, type(nu_mirna_100))

                # TODO: take mirnas
                for j in range(nu_mirna_100):
                    mirna = sheet['F' + str(i + j)].value

                    # di[mirna][index] += 1
                    # all the commented code belllow are changed for the line above cause the adjustment of mirnas
                    # TODO: initialize mirna is in the dictionary
                    # TODO: refresh the number of predicted mirnas for the organim
                    if mirna in di.keys():
                        # refresh
                        # print('\trefreshing\n')
                        di[mirna][index] += 1

                    else:
#                         print('->>>>>>>\tinitializating\n' + mirna)
                        list_mirna_absents.append(mirna)
                        di[mirna] = [0] * len(list_files)
                        di[mirna][index] += 1

                if type(nu_mirna_100) == int and nu_mirna_100 > 0:
                    i += nu_mirna_100 - 1

                i += 1

                # limt the quantity of mirnas for the organism
                # if i > 100:
                #     break

        # break the organism
        # break

    # for key, value in di.items():
    #     print(key, value)

        # create pandas data frame
    df = pd.DataFrame(data=di,
                      index=[elem.replace('.xlsx', '') for elem in list_files])

#     for elem in di.keys():
#         print(elem)
    print('number of mirnas: ', len(di))

#     for elem in list_mirna_absents:
#         print(elem)
#     print('number of absent mirnas: ', len(list_mirna_absents))

    return df
