# src/data_cleaner.py

def clean_sales_data(records):
    valid_records = []
    invalid_count = 0

    for r in records:
        try:
            if not r["TransactionID"].startswith("T"):
                raise ValueError

            if not r["CustomerID"] or not r["Region"]:
                raise ValueError

            qty = int(r["Quantity"])
            if qty <= 0:
                raise ValueError

            price = int(r["UnitPrice"].replace(",", ""))
            if price <= 0:
                raise ValueError

            r["Quantity"] = qty
            r["UnitPrice"] = price
            r["Revenue"] = qty * price

            valid_records.append(r)

        except:
            invalid_count += 1

    return valid_records, invalid_count
