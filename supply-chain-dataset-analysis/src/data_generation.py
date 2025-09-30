import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# Initialize Faker
fake = Faker()

# Parameters
num_records = 5000   # adjust as needed

# Weighted categories (uneven distribution)
categories = ["Electronics", "Apparel", "Office Supplies", "Food & Beverage", "Medical Supplies"]
category_weights = [0.35, 0.25, 0.15, 0.15, 0.10]  # Electronics & Apparel dominate

# Weighted suppliers (uneven distribution)
suppliers = ["Supplier_A", "Supplier_B", "Supplier_C"]
supplier_weights = [0.5, 0.3, 0.2]  # Supplier_A dominates

# Warehouse names with uneven distribution
warehouses = [f"WH_{fake.lexify(text='??').upper()}{random.randint(1,9)}" for _ in range(10)]
warehouse_weights = [0.25, 0.2, 0.15, 0.1, 0.1, 0.07, 0.05, 0.04, 0.025, 0.025]  # top warehouses dominate
warehouse_locations = {wh: fake.city() for wh in warehouses}

# Associates (always assigned, reused multiple times)
associates = ["Niva", "Sam", "Liam", "Olivia", "Emma", "Noah", "Mia", "Ava", "Ethan", "Sophia"]

# Status distribution (random)
statuses = ["Pending", "Received", "Backordered", "Canceled"]

# Generate data
data = []
today = pd.Timestamp.today()

for i in range(1, num_records+1):
order_id = i

# Weighted random choice for uneven distribution
category = random.choices(categories, weights=category_weights, k=1)[0]
supplier = random.choices(suppliers, weights=supplier_weights, k=1)[0]
warehouse = random.choices(warehouses, weights=warehouse_weights, k=1)[0]
location = warehouse_locations[warehouse]

associate = random.choice(associates)  # always assigned
status = random.choice(statuses)

# Quantities
qty_required = random.randint(5, 300)
if status == "Canceled":
    qty_received = 0
elif status == "Pending":
    qty_received = random.randint(0, int(qty_required * 0.3))  # few or none
else:
    qty_received = random.randint(int(qty_required * 0.5), qty_required)

qty_in_transfer = qty_required - qty_received
unit_price = {
    "Electronics": random.randint(100, 500),
    "Apparel": random.randint(20, 150),
    "Office Supplies": random.randint(5, 80),
    "Food & Beverage": random.randint(2, 50),
    "Medical Supplies": random.randint(50, 300)
}[category]
order_cost = qty_received * unit_price

# Dates
order_date = fake.date_between(start_date="-120d", end_date="today")
lead_time = random.randint(1, 20)
need_by_date = order_date + timedelta(days=random.randint(5, 30))

# Receive date logic
receive_date = None
if status == "Received":
    if random.random() > 0.3:  # 70% on-time
        receive_date = order_date + timedelta(days=lead_time)
    else:  # 30% late
        receive_date = order_date + timedelta(days=lead_time + random.randint(1, 5))
elif status in ["Pending", "Backordered"]:
    if random.random() > 0.5:
        receive_date = None
    else:
        receive_date = order_date + timedelta(days=lead_time + random.randint(-2, 5))

# Ensure consistency: if associate exists + qty_received > 0
if associate and receive_date is None and qty_received > 0:
    receive_date = order_date + timedelta(days=lead_time)

row = {
    "order_id": order_id,
    "item_category": category,
    "supplier_name": supplier,
    "warehouse_name": warehouse,
    "warehouse_location": location,
    "fc_associate": associate,
    "order_status": status,
    "total_quantity_required": qty_required,
    "total_quantity_received": qty_received,
    "total_quantity_in_transfer": qty_in_transfer,
    "unit_price": unit_price,
    "order_cost": order_cost,
    "lead_time_days": lead_time,
    "need_by_date": need_by_date,
    "receive_date": receive_date
}
data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Preview
print(df.head(10))

# Save to CSV
df.to_csv("supply_chain_data.csv", index=False)
print("✅ supply_chain_data.csv saved with", len(df), "rows.")