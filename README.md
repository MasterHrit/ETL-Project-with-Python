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

3. **Transform Data**:
   - Add new columns to the DataFrame for market capitalization in GBP, EUR, and INR.
   - Use the exchange rate information provided in a CSV file.
   - Ensure values are rounded to two decimal places.

4. **Load Data**:
   - Save the transformed data locally in a CSV file.
   - Load the data into a SQL database as a table.

5. **Query Data**:
   - Write and execute SQL queries to extract information for below
	- Display all the entries from the table
	- Display the Average GBP in Billion from the table
	- Display the Top 5 Largest Banks from the table 

6. **Logging**:
   - Implement a logging mechanism to track the progress and execution of each step.
   - Maintain detailed log entries for all operations, including data initialization and function calls.

---

## **Pre-requisite**
Ensure the following libraries are installed:
- `pandas`
- `bs4`
- `sqlite3`

You can install the necessary Python packages using the following command:

```bash
pip install pandas bs4 sqlite3
```
---

## **Installation**
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/MasterHrit/ETL-Project-with-Python.git
   cd ETL-Project-with-Python
   ```
2. Ensure you have the Pre-requisite Python packages installed.

---

## **Usage**
To run the ETL process, execute the following Python script:
```bash
python etl_script.py
```
This will perform the following operations:
- Extract data from the specified URL page.
- Transform the data by converting market capitalization values into GBP, EUR, and INR.
- Load the transformed data into both a CSV file and a SQLite database.

---

## **Code Understanding**
1. **Logging Process**</br></br>
   - The log_progress function logs messages at various stages of the ETL process to a code_log.txt file.</br></br>
   Log Function</br>
   ![Log Function](screenshots/Task_1_log_function.png)</br></br>
   Logging Output Screen
   ![Logging Output Screen](screenshots/Task_7_log_content.png)</br></br>
2. **Extract Function**</br></br>
   - The extract function scrapes the list of largest banks and their market capitalizations in USD from the Wikipedia page.</br></br>
   Inspecting the Webpage to get Insights on Webpage Structure
   ![Inspecting the Webpage to get Insights on Webpage Structure](screenshots/Task_2a_extract.png)</br></br>
   Extract Function
   ![Extract Function](screenshots/Task_2b_extract.png)</br></br>
   Extracted Data Output
   ![Extracted Output](screenshots/Task_2c_extract.png)</br></br>
     
   
