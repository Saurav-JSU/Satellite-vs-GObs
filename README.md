# Satellite and USGS Data Downloader

This repository provides Python scripts for downloading satellite products from Google Earth Engine (GEE) and USGS station and precipitation data using the NWIS API. The scripts are designed to facilitate easy access to large datasets over specified periods, useful for hydrological, environmental, and climate studies.

## Features

- **Google Earth Engine Satellite Data Exporter**: Downloads specific satellite datasets for a given Area of Interest (AOI) and parameters over a specified time range.
- **USGS Station and Precipitation Data Downloader**: Retrieves and downloads discharge, precipitation, or other specified parameters for multiple states in the CONUS (Continental United States).

## Getting Started

### Prerequisites

- Python 3.12.4
- Required Python packages: `earthengine-api`, `dataretrieval`, `pandas`, `os`, `shutil`
- Google Earth Engine account and authentication
- NWIS API access

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
   ```

2. Install the required Python packages:

   ```bash
   pip install earthengine-api dataretrieval pandas
   ```

3. Authenticate with Google Earth Engine:

   ```bash
   earthengine authenticate
   ```

### Scripts

#### 1. Satellite Data Exporter (`satellite_exporter.py`)

This script allows you to download satellite data for a specific Area of Interest (AOI) over a time range.

- **Parameters:**
  - `aoi_id`: The ID of the area of interest in Google Earth Engine.
  - `dataset_id`: The ID of the satellite dataset to download.
  - `parameters`: List of parameters to export.
  - `start_year`, `end_year`: The range of years for data export.

- **Usage:**

  ```python
  from satellite_exporter import DataExporter
  
  exporter = DataExporter(
      'location_of_asset',
      'gee_image_collection',
      ['parameter_name'],
      1980,
      2023
  )
  
  exporter.export_data()
  ```

#### 2. USGS Data Downloader (`usgs_data_downloader.py`)

This script downloads USGS station and precipitation data for specified states and parameters.

- **Parameters:**
  - `state`: State abbreviation (e.g., 'KS', 'OK').
  - `parameter_code`: The NWIS parameter code (e.g., '00060' for discharge).
  - `output_folder`: The parent path where data will be saved.

- **Usage:**

  ```python
  python usgs_data_downloader.py
  ```

  - Enter the required `parameter_code` and `output_folder` when prompted.

## Folder Structure

- **GEE_MS_temp**: Folder for satellite data exported from Google Earth Engine.
- **USGS Data**: Folder for USGS station data, organized by state and parameter.

## Contributing

Please feel free to submit issues, fork the repository, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the contents to better match your project specifics.
