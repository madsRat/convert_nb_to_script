"""
Cleans vehicle data by including only necessary fields
"""
import numpy as np
import pandas as pd
def clean_csv_data(df_vehicle, df_person):
    """
    :param df_vehicle, df_person: dataframes
    :return Dataframe, merged dataframe
    """
    # create list to remove fault codes
    replace_vals_trav_speed = {997:np.NaN, 998:np.NaN, 999:np.NaN}
    replace_vals_speed_lim = {98:np.NaN, 99:np.NaN}

    df_vehicle['TRAV_SP_1'] = df_vehicle['TRAV_SP'].replace(replace_vals_trav_speed)
    df_vehicle['VSPD_LIM_1'] = df_vehicle['VSPD_LIM'].replace(replace_vals_speed_lim)

    # merge vehicle and person df by CASENUM
    df_merged = df_vehicle.merge(df_person, how='outer', on='CASENUM')

    # definitions of crash codes listed below:
    # 0 No Apparent Injury (O)
    # 1 Possible Injury (C)
    # 2 Suspected Minor Injury (B)
    # 3 Suspected Serious Injury (A)
    # 4 Fatal Injury (K)
    # 5 Injured, Severity Unknown (U)
    # 6 Died Prior to Crash
    # 9 Unknown/Not Reported

    # create travel speed bins for plotting
    df_merged['TRAV_SP_1_bins'] = pd.cut(df_merged['TRAV_SP_1'], bins=20)

    df_inj_sev_count = df_merged.groupby(['TRAV_SP_1_bins'], dropna=True).count()
    print(df_inj_sev_count)
    print(df_inj_sev_count['INJ_SEV'])
    print(df_inj_sev_count.index)
    return df_inj_sev_count
