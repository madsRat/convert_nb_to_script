from load_data import load_csv_data
from clean_data import clean_csv_data
from plot_data import plot_csv_data

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_vehicle_csv', help='vehicle_csv')
    parser.add_argument('input_person_csv', help='person_csv')
    parser.add_argument('output_file', help='plot in png format')
    args = parser.parse_args()

    # import data
    df_vehicle, df_person = load_csv_data(args.input_vehicle_csv, args.input_person_csv)

    # clean data
    df_merged = clean_csv_data(df_vehicle, df_person)

    # plot data
    plot_csv_data(df_merged, args.output_file)

    print('Process Complete.')
