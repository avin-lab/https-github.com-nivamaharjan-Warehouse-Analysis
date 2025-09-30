# Supply Chain Dataset Analysis

## Overview
# 📦 Supply Chain Dataset Analysis (Python)

This project demonstrates how to generate and analyze a synthetic **supply chain dataset** using Python.  
The dataset simulates warehouse orders, suppliers, associates, and order statuses, allowing us to practice **data cleaning, transformation, and visualization** with Pandas, Matplotlib, and Plotly.

---

## 📊 Project Overview
- **Data Generation**  
  - Created a synthetic dataset of 5,000 orders using Python & Faker.  
  - Dataset includes warehouses, suppliers, item categories, fulfillment center associates, and order-level details.  
  - Uneven distributions to reflect realistic business scenarios (some suppliers dominate, some warehouses busier).  

- **Data Analysis**  
  - Used **Pandas** for data cleaning, aggregation, and grouping.  
  - Performed category, supplier, and warehouse-level analysis.  
  - Defined a **custom function** to summarize cancellations by supplier.  

- **Data Visualization**  
  - Built **Pie Charts** → Order status distribution.  
  - **Stacked Bar Charts** → On-time vs Overdue orders by warehouse and supplier.  
  - **Monthly Trends** → Mean lead time and overdue order trends over time.  
  - **Grouped Bars** → Supplier vs Category demand and cancellations.  

---

## 🗂 Dataset Structure
The dataset contains **15 columns**:

| Column Name | Description |
|-------------|-------------|
| `order_id` | Unique ID for each order |
| `item_category` | Product category (Electronics, Apparel, Office Supplies, Food & Beverage, Medical Supplies) |
| `supplier_name` | Supplier of the item (Supplier_A, Supplier_B, Supplier_C) |
| `warehouse_name` | Identifier for the warehouse (e.g., WH_AB3) |
| `warehouse_location` | Location assigned to the warehouse |
| `fc_associate` | Fulfillment center associate who processed the order |
| `order_status` | Status of the order (Pending, Received, Backordered, Canceled) |
| `total_quantity_required` | Total number of units ordered |
| `total_quantity_received` | Total number of units actually received |
| `total_quantity_in_transfer` | Pending units = required – received |
| `unit_price` | Price per unit (varies by category) |
| `order_cost` | Total cost of received items |
| `lead_time_days` | Days from order to delivery |
| `need_by_date` | Deadline for order fulfillment |
| `receive_date` | Actual date items were received (may be null) |

---

## 📈 Key Insights
- **Supplier Reliability:** Identified suppliers with higher cancellation rates.  
- **Warehouse Performance:** Some warehouses (e.g., WH_GY4, WH_FK3) had higher overdue volumes.  
- **Seasonal Trends:** Orders and overdue items spike in certain months → potential staffing bottlenecks.  
- **Decision Support:** Data helps managers prioritize warehouses and negotiate with underperforming suppliers.  

---

## 🛠️ Tech Stack
- **Python 3**  
- **Libraries:** Pandas, Numpy, Matplotlib, Plotly, Faker  

---

## 🚀 Next Steps
- Add advanced visualizations (heatmaps, dual-axis charts).  
- Extend analysis to associate-level performance.  
- Automate KPI dashboards for real-time monitoring.  



## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd supply-chain-dataset-analysis
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
- To generate the supply chain dataset, run the `data_generation.py` script located in the `src` directory.
- Open the `Warehouse Analysis.ipynb` notebook in Jupyter to explore the generated dataset and derive insights.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.