# src/api_handler.py
"""
API Handler Module
------------------
Simulates integration with an external API to fetch
additional business data for sales analytics.

In this assignment:
- A mock API is used (no real HTTP calls)
- Demonstrates API interaction logic
- Safely handles missing data
"""

def get_product_discount(product_id):
    """
    Simulates fetching discount information from an external API.

    Args:
        product_id (str): Product ID (e.g., P101)

    Returns:
        float: Discount percentage (0.0 to 1.0)
    """

    # Mock API response data
    discount_data = {
        "P101": 0.10,  # Laptop
        "P102": 0.05,  # Mouse
        "P103": 0.07,  # Keyboard
        "P104": 0.08,  # Monitor
        "P109": 0.06   # Wireless Mouse
    }

    return discount_data.get(product_id, 0.0)


def apply_discount(records):
    """
    Applies discount to sales records based on ProductID.

    Adds:
    - DiscountRate
    - DiscountedRevenue

    Args:
        records (list): Cleaned sales records

    Returns:
        list: Updated sales records
    """

    for record in records:
        discount = get_product_discount(record["ProductID"])
        record["DiscountRate"] = discount
        record["DiscountedRevenue"] = record["Revenue"] * (1 - discount)

    return records
