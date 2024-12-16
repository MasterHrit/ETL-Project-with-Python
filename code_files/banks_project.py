# Code for ETL operations on Country-GDP data

# Importing the required libraries
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3 as sq
import requests

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

    timeformat="%d-%b-%Y %H:%M:%S"
    current_time=datetime.now()
    formatted_time=current_time.strftime(timeformat)

    with open("code_log.txt","a") as f:
        f.write(f"{formatted_time} : {message}\n")


def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

    html_text=requests.get(url).text
    html_object=BeautifulSoup(html_text,"html.parser")

    table_list=html_object.find_all("tbody")
    rows=table_list[0].find_all("tr")
    df=pd.DataFrame(columns=table_attribs)
    for row in rows:
        cells=row.find_all("td")
        if(len(cells)!=0):
            name=cells[1].find_all("a")[1].string
            market_cap=float(cells[2].string)
            df=pd.concat([df,pd.DataFrame([{"Name":name,"MC_USD_Billion":market_cap}])],ignore_index=True)
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    exchange_rate_df=pd.read_csv(csv_path)
    df["MC_GBP_Billion"]=round(df["MC_USD_Billion"]*exchange_rate_df.loc[exchange_rate_df["Currency"]=="GBP"]["Rate"].iloc[0],2)
    df["MC_EUR_Billion"]=round(df["MC_USD_Billion"]*exchange_rate_df.loc[exchange_rate_df["Currency"]=="EUR"]["Rate"].iloc[0],2)
    df["MC_INR_Billion"]=round(df["MC_USD_Billion"]*exchange_rate_df.loc[exchange_rate_df["Currency"]=="INR"]["Rate"].iloc[0],2)
    print(f"{df['MC_EUR_Billion'][4] = }")
    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

    df.to_csv(output_path,index=False)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

    df.to_sql(table_name,sql_connection,if_exists="replace",index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''

    print("\n"+query_statement)
    dataframe=pd.read_sql(query_statement,sql_connection)
    print(dataframe)

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

url="https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attributes_extraction=["Name","MC_USD_Billion"]
table_attributes_final=["Name","MC_USD_Billion","MC_GBP_Billion","MC_EUR_Billion","MC_INR_Billion"]
output_csv_path="./Largest_banks_data.csv"
database_name="Banks"
table_name="Largest_banks"
exchange_rate_csv="exchange_rate.csv"
log_progress("Preliminaries complete. Initiating ETL process.")

df=extract(url,table_attributes_extraction)
log_progress("Data extraction complete. Initiating Transformation process.")

transformed_df=transform(df,exchange_rate_csv)
log_progress("Data transformation complete. Initiating Loading process.")

load_to_csv(transformed_df, output_csv_path)
log_progress("Data saved to CSV file.")

conn=sq.connect("Banks.db")
log_progress("SQL Connection initiated.")

load_to_db(transformed_df, conn, table_name)
log_progress("Data loaded to Database as a table, Executing queries.")

query1=f"SELECT * FROM {table_name}"
run_query(query1, conn)
query2=f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query2, conn)
query3=f"SELECT Name from {table_name} limit 5"
run_query(query3, conn)
log_progress("Process Complete.")

conn.close()
log_progress("Server Connection closed.")