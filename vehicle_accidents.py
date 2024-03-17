import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair

# Import data ##########################################################
df_vehicle = pd.read_csv('data/crss_2021_csv/vehicle.csv')
df_person = pd.read_csv('data/crss_2021_csv/person.csv')

# Daniel's Topics: Fast driving, unbuckled driving
# relate to accident type, injury, and damage
# indicators: SPEEDREL, VSPD_LIM, TRAV_SP, CASENUM
# TODO look at accident dataframe and generate basic statistics

# Data cleaning and manipulation #######################################
replace_vals_trav_speed = {997:np.NaN, 998:np.NaN, 999:np.NaN}
replace_vals_speed_lim = {98:np.NaN, 99:np.NaN}

df_vehicle['TRAV_SP_1'] = df_vehicle['TRAV_SP'].replace(replace_vals_trav_speed)
df_vehicle['VSPD_LIM_1'] = df_vehicle['VSPD_LIM'].replace(replace_vals_speed_lim)

# merge vehicle and person df by CASENUM
df_merged = df_vehicle.merge(df_person, how='outer', on='CASENUM')

# 0 No Apparent Injury (O)
# 1 Possible Injury (C)
# 2 Suspected Minor Injury (B)
# 3 Suspected Serious Injury (A)
# 4 Fatal Injury (K)
# 5 Injured, Severity Unknown (U)
# 6 Died Prior to Crash
# 9 Unknown/Not Reported

# INJSEV_IM
# TODO use pandas cut,
# TODO pandas groupby, plot travel speed vs count(INJ_SEV),
df_merged['TRAV_SP_1_bins'] = pd.cut(df_merged['TRAV_SP_1'], bins=20)

df_inj_sev_count = df_merged.groupby(['TRAV_SP_1_bins'], dropna=True).count()
print(df_inj_sev_count)
print(df_inj_sev_count['INJ_SEV'])
print(df_inj_sev_count.index)

# filter based on speed related crashes? df_vehicle['SPEEDREL']
# quit()

# # speed limit vs travel speed ##########################################
# fig, ax = plt.subplots()
# ax.scatter(df_vehicle['VSPD_LIM_1'], df_vehicle['TRAV_SP_1'],alpha=0.5)
#
# ax.set_xlabel(r'SPEEDLIMIT', fontsize=15)
# ax.set_ylabel(r'TRAVEL SPEED', fontsize=15)
# ax.set_title('')
#
# ax.grid(True)
# fig.tight_layout()
#
# # plt.show()
#
# # travel speed vs injury severity ##########################################
# fig_1, ax_1 = plt.subplots()
# ax_1.scatter(df_merged['TRAV_SP_1'], df_merged['INJ_SEV'],alpha=0.5)
#
# ax_1.set_xlabel(r'TRAVEL SPEED', fontsize=15)
# ax_1.set_ylabel(r'INJURY SEVERITY', fontsize=15)
# ax_1.set_title('')
#
# ax_1.grid(True)
# fig_1.tight_layout()
#
# # plt.show()

# speed bin vs count ##########################################
fig_1, ax_1 = plt.subplots()
ax_1.hist(df_merged['TRAV_SP_1'], bins=np.arange(0,100,5), edgecolor='k')

ax_1.set_xlabel(r'speed bins', fontsize=15)
ax_1.set_ylabel(r'accident count', fontsize=15)
# ax_1.set_title('')

# ax_1.grid(True)
# fig_1.tight_layout()

plt.show()
