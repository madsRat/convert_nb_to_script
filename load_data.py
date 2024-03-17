"""
This file loads data for pipelines
"""
import pandas as pd
def load_csv_data(vehicle_file_path, person_file_path):
    """
    :param vehicle_file_path, person_file_path: the csv file path for vehicle data and person data
    :return Two Dataframes, one vehicle df and one person df
    """
    df_vehicle = pd.read_csv('data/crss_2021_csv/vehicle.csv')
    df_person = pd.read_csv('data/crss_2021_csv/person.csv')
    return df_vehicle, df_person