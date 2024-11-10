import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(0)

# Define the number of rows and columns
num_rows = 1000000
num_cols = 10

# Generate random data for each column
customer_id = np.random.randint(1, 1000, num_rows)
product_id = np.random.randint(1, 100, num_rows)
quantity = np.random.randint(1, 10, num_rows)
price_per_unit = np.round(np.random.uniform(1, 100, num_rows), 2)
total_sales_amount = np.round(quantity * price_per_unit, 2)

# Generate random city and state data for each row
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
states = ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA', 'TX', 'CA']
city = np.random.choice(cities, size=num_rows)
state = np.random.choice(states, size=num_rows)


# Generate random sales dates for each row
start_date = pd.Timestamp('2020-01-01')
end_date = pd.Timestamp('2024-12-31')
sales_dates = pd.date_range(start=start_date, end=end_date, periods=num_rows)
sales_dates = np.random.choice(sales_dates, size=num_rows, replace=True)

# Create a DataFrame with the generated data
data = pd.DataFrame({
    'customer_id': customer_id,
    'product_id': product_id,
    'quantity': quantity,
    'price_per_unit': price_per_unit,
    'total_sales_amount': total_sales_amount,
    'sales_date': sales_dates,
    'city': city,
    'state': state
})

# Add some additional columns with random data
data['discount'] = np.round(np.random.uniform(0, 0.2, num_rows), 2)
data['shipping_cost'] = np.round(np.random.uniform(5, 20, num_rows), 2)
data['payment_method'] = np.random.choice(['credit_card', 'debit_card', 'paypal'], num_rows)

# Save the DataFrame to a CSV file
data.to_csv('C://Users//suran//Downloads//python_project//venv//customer_sales_data.csv', index=False)
