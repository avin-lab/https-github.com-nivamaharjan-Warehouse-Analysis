import pandas as pd
import numpy as np
import random
from faker import Faker

def generate_supply_chain_data(n=2000):
    fake = Faker()
    np.random.seed(42)
    random.seed(42)

    # Delivery settings
    LATE_DELIVERY_MIN_DAYS = 1
    LATE_DELIVERY_MAX_DAYS = 7
    LATE_DELIVERY_PROBABILITY = 0.3  # 30% chance of late delivery

    # Categories and suppliers
    item_categories = {
        "Electronics": (50, 500),
        "Apparel": (10, 100),
        "Office Supplies": (5, 50),
        "Food & Beverage": (2, 20),
        "Medical Supplies": (20, 200),
    }
    suppliers = ["Supplier_A", "Supplier_B", "Supplier_C"]
    statuses = ["Pending", "Received", "Backordered", "Canceled"]

    # Warehouses
    letters_list = [''.join(np.random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3)) for _ in range(10)]
    digits_list = [random.randint(1, 9) for _ in range(10)]
    warehouses = [f"WH_{letters}{digit}" for letters, digit in zip(letters_list, digits_list)]
    warehouse_locs = {w: fake.city() for w in warehouses}

    data = []
    for i in range(n):
        order_id = fake.unique.random_int(10000, 99999)
        category = random.choice(list(item_categories.keys()))
        supplier = random.choice(suppliers)
        warehouse = random.choice(warehouses)
        warehouse_loc = warehouse_locs[warehouse]
        fc_associate = f"Assoc_{random.randint(100,999)}"

        status = random.choice(statuses)

        qty_required = random.randint(10, 200)
        qty_received = qty_required if status == "Received" else random.randint(0, qty_required)
        qty_in_transfer = qty_required - qty_received

        unit_price = random.randint(*item_categories[category])
        order_cost = qty_received * unit_price

        order_date = fake.date_between(start_date="-60d", end_date="today")
        need_by_date = order_date + pd.Timedelta(days=random.randint(3, 15))

        if status == "Received":
            if random.random() < LATE_DELIVERY_PROBABILITY:
                # Late delivery
                receive_date = need_by_date + pd.Timedelta(days=random.randint(LATE_DELIVERY_MIN_DAYS, LATE_DELIVERY_MAX_DAYS))
            else:
                # On time
                receive_date = need_by_date
            lead_time = (receive_date - order_date).days
        else:
            receive_date = None
            lead_time = None

        data.append([
            order_id, category, supplier, warehouse, warehouse_loc, fc_associate,
            status, qty_required, qty_received, qty_in_transfer,
            unit_price, order_cost, lead_time, need_by_date, receive_date
        ])

    columns = [
        "order_id", "item_category", "supplier_name", "warehouse_name", "warehouse_location",
        "fc_associate", "order_status", "total_quantity_required", "total_quantity_received",
        "total_quantity_in_transfer", "unit_price", "order_cost", "lead_time_days",
        "need_by_date", "receive_date"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv("data/warehouse_orders.csv", index=False)
    print(f"✅ Generated {n} rows and saved to data/warehouse_orders.csv")
    return df

if __name__ == "__main__":
    generate_supply_chain_data()
