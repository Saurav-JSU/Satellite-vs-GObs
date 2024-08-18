import os
from dataretrieval import nwis

def create_folder(folder_path):
  """Creates a folder if it doesn't already exist."""
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)


def get_state_stations(state, parameter_code):
    stations, _ = nwis.what_sites(stateCd=state, outputDataTypeCd='dv', parameterCd=parameter_code)
    if stations.empty:
        print(f"No stations found for {state} measuring the specified parameter.")
        return None, None
    else:
        print(f"Stations found in {state} measuring the specified parameter ({parameter_code}):")
        station_dates = {}
        for index, row in stations.iterrows():
            # Ensuring the index is displayed uniquely
            print(f"{index + 1}: {row['station_nm']} (ID: {row['site_no']}) - Data available from {row['begin_date']} to {row['end_date']}")
            # Map station's site ID to its corresponding date range
            station_dates[row['site_no']] = (row['begin_date'], row['end_date'])
        return stations, station_dates


def retrieve_and_download_data(stations_info, station_dates, parameter_code, state_abbr, output_folder):
    """Downloads data for each station and saves it with state abbreviation."""
    parameter_code_folder = os.path.join(output_folder, parameter_code)  # Folder within output path
    create_folder(parameter_code_folder)

    state_folder = os.path.join(parameter_code_folder, state_abbr)  # Subfolder by state
    create_folder(state_folder)

    for index, row in stations_info.iterrows():
        site_id = row['site_no']
        begin_date, end_date = station_dates[site_id]

        filename = f"{site_id}_{begin_date}_to_{end_date}.csv"
        filepath = os.path.join(state_folder, filename)

        print(f"Downloading data for Station ID: {site_id} from {begin_date} to {end_date}")
        data, _ = nwis.get_dv(sites=site_id, parameterCd=parameter_code, start=begin_date, end=end_date)

        if not data.empty:
            data.to_csv(filepath)
            print(f"Data successfully downloaded to {filepath}")
        else:
            print(f"No data available for Station ID: {site_id}")


if __name__ == "__main__":
    # Define CONUS US state abbreviations (modify if needed)
    states = ['KS', 'OK', 'TX', 'MN', 'IA', 'MO', 'AR', 'LA', 'WI', 'IL', 'MS', 'MI', 'IN', 'KY', 'TN', 'AL', 'FL', 'GA', 'SC', 'NC', 'VA', 'WV', 'OH', 'PA', 'NY', 'VT', 'NH', 'MA', 'RI', 'CT', 'NJ', 'DE', 'MD']

    parameter_code = input("Enter the parameter code (e.g., '00060' for discharge): ").strip()
    output_folder = input("Enter the output folder parent path (e.g., /path/to/data): ").strip()

    for state in states:
        stations_info, station_dates = get_state_stations(state, parameter_code)
        if stations_info is not None:
            state_abbr = state  # Assuming state code can be used as abbreviation
            retrieve_and_download_data(stations_info, station_dates, parameter_code, state_abbr, output_folder)



