# src/data_loader.py

def load_sales_data(file_path):
    records = []
    with open(file_path, "r", encoding="utf-8") as file:
        headers = file.readline().strip().split("|")

        for line in file:
            values = line.strip().split("|")
            record = dict(zip(headers, values))
            records.append(record)

    return records
