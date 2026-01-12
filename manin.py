# main.py

from src.data_loader import load_sales_data
from src.data_cleaner import clean_sales_data
from src.analytics import sales_by_region, top_products

DATA_FILE = "data/sales_data.txt"

def main():
    records = load_sales_data(DATA_FILE)
    cleaned_data, invalid_count = clean_sales_data(records)

    print("Validation Output:")
    print(f"Total records parsed: {len(records)}")
    print(f"Invalid records removed: {invalid_count}")
    print(f"Valid records after cleaning: {len(cleaned_data)}")

    region_summary = sales_by_region(cleaned_data)
    top_items = top_products(cleaned_data)

    print("\nSales by Region:")
    for k, v in region_summary.items():
        print(f"{k}: {v}")

    print("\nTop 3 Products by Revenue:")
    for product, revenue in top_items:
        print(f"{product}: {revenue}")

if __name__ == "__main__":
    main()
