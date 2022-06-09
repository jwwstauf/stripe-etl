from config import host, database, user, password
from queries import *
import psycopg2


class database_driver():

    def connect(host, database, user, password):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(host=host, database=database, user=user, password=password)
            conn.autocommit = True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            sys.exit(1) 
        print("Connection successful")
        return conn

    def setup(conn, table):
        cur = conn.cursor()
        cur.execute(table)


    def insert_values(conn, df):
    
        cur = conn.cursor()
    
        for value in df.values:
            subscription_id, billing_cycle_anchor, cancel_at, cancel_at_period_end, canceled_at, created, current_period_end, current_period_start, customer, ended_at, quantity, start_date, status = value
            #insert subscriber record
            subscriber_data = (subscription_id, billing_cycle_anchor, cancel_at, cancel_at_period_end, canceled_at, created, current_period_end, current_period_start, customer, ended_at,quantity, start_date, status)
            cur.execute(insert_table, subscriber_data)
        conn.commit()
