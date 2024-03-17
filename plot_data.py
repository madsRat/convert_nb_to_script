"""
This file plots vehicle and people data
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def plot_csv_data(df_merged, output_file_name):
    """
    :param df_merged, output_file_name: dataframe of merged vehicle data and person data and output file name
    :return png, plot of binned vehicle data
    """
    # speed bin vs count ##########################################
    fig_1, ax_1 = plt.subplots()
    ax_1.hist(df_merged['TRAV_SP_1'], bins=np.arange(0,100,5), edgecolor='k')

    ax_1.set_xlabel(r'speed bins', fontsize=15)
    ax_1.set_ylabel(r'accident count', fontsize=15)
    # ax_1.set_title('')

    # ax_1.grid(True)
    # fig_1.tight_layout()
    plt.savefig(output_file_name)
    plt.show()
