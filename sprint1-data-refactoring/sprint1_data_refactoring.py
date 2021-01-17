"""
@author: Bruno Conde Costa da Silva
"""

import os
import numpy as np
import pandas as pd
from Bio import SeqIO
import matplotlib as plt
import plotly
from openpyxl import load_workbook, Workbook

# TODO: get current work directory and input files directory
dir_cwd = os.getcwd()
dir_input = os.path.join(dir_cwd, 'input')

"""
Genomes
"""
# TODO: get genome fasta files directory
dir_proteomes = os.path.join(dir_input, 'proteome_fasta_files')

# TODO: get genome fasta files
list_proteome_files = os.listdir(dir_proteomes)

"""
Predictions
"""
# TODO: get miRDB prediction files directory
dir_predictions = os.path.join(dir_input, 'miRDB_prediction_files')

# TODO: get miRDB predictions
list_prediction_files = os.listdir(dir_predictions)

"""
Data adjusting
di_proteome_prediction[genome] = prediction
"""

# TODO: create a dictionary, where key is the genome and value is the prediction
di_proteome_prediction = dict()
for protein in list_proteome_files:
    for prediction in list_prediction_files:
        if protein.replace('.fasta', '') in prediction:
            di_proteome_prediction[protein] = prediction

# TODO: iterate over genome and prediction at the same time
for protein, prediction in di_proteome_prediction.items():
    print(f'\n\n{protein} {prediction}')

    """
    Open simultaneously both genome and prediction
    """

    # TODO: get prediction data frame
    df_prediction = pd.read_excel(open(os.path.join(dir_predictions, prediction), 'rb'), sheet_name='Planilha1')
    # print(df_prediction.head())

    """
    print(df_prediction.keys())
    Index(['Organismo', 'Gene', '#miRNA (Humans)', 'size', 'miRNA 100',
       'nomes 100', 'Unnamed: 6'],
      dtype='object')
    """

    print(df_prediction['Unnamed: 6'])

    # TODO: open fasta file with biopython package
    array_id = np.array([])
    array_length = np.array([])
    array_sequence = np.array([])

    i = 0
    for record in SeqIO.parse(os.path.join(dir_proteomes, protein), 'fasta'):
        print(i)
        # print(record.id)
        # print(record.name)
        # print(record.seq)
        # print(record.description)
        id = record.__dict__['id']
        name = record.__dict__['name']

        try:
            if not id != name:
                pass
        except:
            print('\n\n----------------id diferente do nome-----------------')

        seq = record.__dict__['_seq']
        length = "".join([d for d in record.__dict__['description'].split(sep=' ') if 'length' in d]).split(sep='=')[1]
        # print(length, type(length))

        array_id = np.append(array_id, [id])
        array_length = np.append(array_length, [length])
        array_sequence = np.append(array_sequence, [seq])

        i += 1

    # for i in range(array_id):
    #     print(array_id[i], array_length[i])
    #     print(array_sequence[i])

