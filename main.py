from Database import Database
from Requests import CreateDataframe
from queries import *
from config import host, database, user, password

def main():
    #pulls data from Stripe API and returns a dataframe
    df = CreateDataframe.get_df()
    #returns a dataframe with only the relevant columns and correct datatypes
    df = CreateDataframe.cleaning_df(df)

    #connects to the database
    conn = Database.connect(host, database, user, password)
    #creates the table if it does not already exist
    Database.setup(conn, create_subscription_table)
    #inserts values into the table, updates rows with existing ids
    Database.insert_values(conn, df)

    #closes the connection
    conn.close()


if __name__ == "__main__":
    main()