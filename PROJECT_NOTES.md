## Dataset Understanding

Dataset Size:
- Rows: 7043
- Columns: 33

Observations:
- Dataset contains customer demographics, services, billing and churn information.
- No duplicate records are found.
- No missing values as well except Churn Reason, because it is only available for customers who actually churned.
- Dtaset appears and is ready for preprocessing.

## Dataset Cleaning

Current size: (7043, 20)

Before training the model, I removed columns that do not contribute meaningful information. Such as:
- CustomerID, unique identifier.
- Count, constant value for every row.
- Country, same value for all customers.
- State, same value for all.
- To avoid redundancy since ML models require numerical targets, I retained Churn Value and removed Churn Label.

Removing such features reduces unnecessary complexity without affective the predictive performance.