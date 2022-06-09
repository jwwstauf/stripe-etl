from Database import database_driver
from Requests import extract_transform
from queries import *
from config import host, database, user, password

def main():
    #pulls data from Stripe api and returns a dataframe
    df = extract_transform.get_df()
    #returns a dataframe with only the relevant columns and correct datatypes
    df = extract_transform.cleaning_df(df)

    #connects to the database
    conn = database_driver.connect(host, database, user, password)
    #creates the schema and tables if they do not already exist
    database_driver.setup(conn, create_subscription_table)
    #inserts values into the table
    database_driver.insert_values(conn, df)

    #closes the connection
    conn.close()


if __name__ == "__main__":
    main()