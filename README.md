# **Top 10 Largest Banks by Market Capitalization**

## **Description**
This project tests the application of Python programming skills and the concepts of **ETL (Extraction, Transformation, and Loading)** using real-world data. It involves extracting data about the largest banks in the world, transforming it into multiple currencies based on exchange rates, and loading the processed data into both CSV files and a database. The project also demonstrates the ability to query and log operations for seamless data engineering.

---

## **Project Scenario**
You are a **Data Engineer** hired by a multi-national firm to process and manage data related to the top 10 largest banks by market capitalization. Your responsibilities include:
- **Extracting** the relevant data from an online source.
- **Transforming** the data into multiple currencies (USD, GBP, EUR, INR) using provided exchange rates.
- **Loading** the data into a CSV file and a database table for accessibility by global managers.

---

## **Key Tasks**
1. **Extract Data**:
   - Extract tabular data from a web source under the heading *"By Market Capitalization"* and store it in a Pandas DataFrame.

2. **Transform Data**:
   - Add new columns to the DataFrame for market capitalization in GBP, EUR, and INR.
   - Use the exchange rate information provided in a CSV file.
   - Ensure values are rounded to two decimal places.

3. **Load Data**:
   - Save the transformed data locally in a CSV file.
   - Load the data into a SQL database as a table.

4. **Query Data**:
   - Write and execute SQL queries to extract information for below
	- Display all the entries from the table
	- Display the Average GBP in Billion from the table
	- Display the Top 5 Largest Banks from the table 

5. **Logging**:
   - Implement a logging mechanism to track the progress and execution of each step.
   - Maintain detailed log entries for all operations, including data initialization and function calls.

---
