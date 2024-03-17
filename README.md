# Convert Notebook to Script Assignment

Introduction:
This program plots crash rates based on vehicle and person dataset from NHTSA. 
Using 2021 CRSS dataset from NHTSA. All csv format.

Dataset candidates: accident, vehicle, person, weather, distract, damage, violation

Motivation:
https://zerodeathsmd.gov/how-you-can-help/crashes-are-no-accident/
https://zerodeathsmd.gov/how-you-can-help/be-the-driver/
https://zerodeathsmd.gov/resources/crashdata/crashdashboard/

Environment and Setup:
Use the requirements.txt file to setup environment. Main packages include: numpy, pandas, and Matplotlib.
Data files should be from: https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/CRSS/2021/
Data folder should be 'CRSS2021CSV' placed in a 'data' directory with main.py.
Usiing specifically vehicle.csv and person.csv

Usage:
python3 main.py 'data/crss_2021_csv/vehicle.csv' 'data/crss_2021_csv/person.csv' 'output.png'

