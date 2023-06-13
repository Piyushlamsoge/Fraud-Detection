#Necessary Package
#pip install faker


#Dataset Creation Using Faker
import pandas as pd
from faker import Faker
from random import randint, uniform, choice

# Set seed for reproducibility
Faker.seed(42)

# Create Faker instance
fake = Faker()

# Generate fake data
data = []
for _ in range(10000):
    transaction_id = fake.uuid4()
    user_id = randint(1, 1000)
    transaction_amount = round(uniform(1, 10000), 2)
    transaction_date = fake.date_between(start_date='-1y', end_date='today')
    is_foreign_transaction = randint(0, 1)
    transaction_type = choice(['purchase', 'refund', 'cash withdrawal'])
    data.append([transaction_id, user_id, transaction_amount, transaction_date, is_foreign_transaction, transaction_type])

# Create DataFrame from generated data
columns = ['transaction_id', 'user_id', 'transaction_amount', 'transaction_date', 'is_foreign_transaction', 'transaction_type']
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV
df.to_csv('fraud_dataset.csv', index=False)


#Fraud Logic Code
import pandas as pd
from datetime import datetime, timedelta

# Read the fraud dataset from the CSV file
df = pd.read_csv('fraud_dataset.csv')

# Define the fraud detection criteria
threshold_amount = 100000
threshold_locations = 3
threshold_days = 1

# Apply fraud detection logic
is_fraud = (
    (df['transaction_amount'] > threshold_amount) |
    (df.groupby('user_id')['transaction_type'].transform('nunique') > threshold_locations) |
    (pd.to_datetime(df['transaction_date']) >= datetime.now() - timedelta(days=threshold_days)) |
    (df['is_foreign_transaction'] == 1)
)

# Update the 'is_fraud' column in the dataframe
df['is_fraud'] = is_fraud.astype(int)

# Print flagged fraud transactions
fraud_transactions = df[df['is_fraud'] == 1]
print(fraud_transactions)

#Analysis of Fraud Detection system


# Analyze the flagged fraud transactions
flagged_transactions = df[df['is_fraud'] == 1]

# Print the count of flagged fraud transactions
print("Total flagged fraud transactions:", len(flagged_transactions))

# Calculate the percentage of flagged fraud transactions
percentage_fraud_transactions = (len(flagged_transactions) / len(df)) * 100
print("Percentage of flagged fraud transactions: {:.2f}%".format(percentage_fraud_transactions))

# Print the distribution of flagged fraud transactions by transaction type
fraud_transactions_by_type = flagged_transactions['transaction_type'].value_counts()
print("Flagged fraud transactions distribution by transaction type:")
print(fraud_transactions_by_type)

# Calculate the average transaction amount of flagged fraud transactions
average_fraud_transaction_amount = flagged_transactions['transaction_amount'].mean()
print("Average transaction amount of flagged fraud transactions: {:.2f}".format(average_fraud_transaction_amount))

# Calculate the maximum transaction amount among flagged fraud transactions
max_fraud_transaction_amount = flagged_transactions['transaction_amount'].max()
print("Maximum transaction amount among flagged fraud transactions: {:.2f}".format(max_fraud_transaction_amount))

# Print the flagged fraud transactions with the highest transaction amount
highest_amount_fraud_transactions = flagged_transactions[flagged_transactions['transaction_amount'] == max_fraud_transaction_amount]
print("Flagged fraud transactions with the highest transaction amount:")
print(highest_amount_fraud_transactions)
