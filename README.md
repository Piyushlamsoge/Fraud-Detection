# Fraud Detection

This repository contains a fraud detection system built in Python for identifying potential fraudulent transactions in a dataset. The system applies various criteria to flag transactions that exhibit suspicious behavior.

## Dataset

The fraud detection system utilizes a dataset containing transaction records. The dataset includes the following columns:

- `transaction_id`: Unique identifier for each transaction.
- `user_id`: Identifier of the user associated with the transaction.
- `transaction_amount`: The amount of the transaction.
- `transaction_date`: The date when the transaction occurred.
- `is_foreign_transaction`: Binary indicator specifying whether the transaction is from a foreign country.
- `transaction_type`: The type of the transaction (e.g., purchase, refund, cash withdrawal).

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Piyushlamsoge/fraud-detection.git

2. Place your fraud dataset CSV file inside the repository folder.

3. Update the `fraud_dataset.csv` file name or path in the Python code if needed.

4. Run the fraud detection system:
   ```bash
   python Transaction_fraud.py
   
  This will execute the fraud detection logic on the dataset and flag potentially fraudulent transactions.

5. Analyze the results:

   The system will output the flagged fraud transactions along with additional analysis, such as the count of flagged transactions, percentage of flagged transactions, distribution by transaction type, average transaction amount, and the highest transaction amount among the flagged fraud transactions.

6. Modify the fraud detection logic:

   If needed, you can modify the fraud detection criteria by adjusting the threshold values or adding additional conditions in the Python code. Refer to the comments in the code for guidance.
   
   
## License

This project is licensed under the MIT License.

Feel free to explore, use, and modify this fraud detection system to suit your specific requirements. Contributions are also welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.
