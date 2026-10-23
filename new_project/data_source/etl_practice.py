import glob 
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt"
target_file = "transformed_data.csv"



def log_progress(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H%:M:%S")
    with open(log_file, "a") as f:
        f.write(f"{timestamp}, {message}\n")




def extract_from_csv(file):
    return pd.read_csv(file)



def extract_from_json(file):
    return pd.read_json(file, lines=True)


def extract_from_xml(file):
    root = ET.parse(file).getroot()
    rows = []
    for record in root:
        rows.append({
            "car_model": record.find("car_model").text,
            "year_of_manufacture": record.find("year_of_manufacture").text,
            "price":float(record.find("price").text),
            "fuel":record.find("fuel").text,
            })
    return pd.DataFrame(rows)



def extract():
    frames = []

    for f in glob.glob("*.csv"):
        if f != target_file:
           frames.append(extract_from_csv(f))

    for f in glob.glob("*.json"):
        frames.append(extract_from_json(f))


    for f in glob.glob("*.xml"):
        frames.append(extract_from_xml(f))

    return pd.concat(frames, ignore_index=True)


def transform(data):
    data["price"] = data["price"].round(2)
    return data



def load_data(target_file, data):
    data.to_csv(target_file, index =False)



log_progress("ETL Job Started")


log_progress("Extract Phase Started")
extracted_data = extract()
log_progress("Extract Phase Ended")


log_progress("Transform Phase Started")
transformed_data = transform(extracted_data)
print(transformed_data.head())
log_progress("Transformed Phase Ended")


log_progress("Load Phase Started")
load_data(target_file, transformed_data)
log_progress("Load Phase Ended")

log_progress("ETL Job Ended")

