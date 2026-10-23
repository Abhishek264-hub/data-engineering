# Data Engineering Practice

Learning projects for my data engineering path.

## etl_practice
A Python ETL script that extracts car price data from CSV, JSON and XML files,
rounds prices to 2 decimals, loads the result into `transformed_data.csv`,
and logs each phase to `log_file.txt`.

Run it:

    pip install -r requirements.txt
    cd new_project/data_source
    python3 etl_practice.py
