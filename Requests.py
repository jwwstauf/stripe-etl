import pandas as pd
import stripe
from config import api_key
import numpy as np
from time import sleep

class CreateDataframe():


    def get_df():
        df = pd.DataFrame()
        stripe.api_key = api_key
                                                        
        #first query to get response id
        first_response = stripe.Subscription.list(status='all')
        #creating dataframe with responses
        df = df.append(pd.json_normalize(first_response['data']))
        #defining next page for loops
        start_after = first_response['data'][-1]['id']
        print('Getting Results')

        while True:    
            try:
                #appending to the dataframe
                response = stripe.Subscription.list(starting_after=start_after, status='all')
                subscription_df = pd.json_normalize(response['data'])
                df = df.append(subscription_df, ignore_index=True)
                #giving the key for the next iteration
                start_after = response['data'][-1]['id']
                #In case rate limiting is an issue
                sleep(.1)
            except Exception as e: 
                print(e)
                print('Stripe Request went wrong')
            
            if response["has_more"] == False:
                break
        return df

    def cleaning_df(df):
        #necessary columns
        df = df[['id', 'billing_cycle_anchor', 'cancel_at', 'cancel_at_period_end', 'canceled_at', 'created', 'current_period_end', 'current_period_start', 'customer', 'ended_at', 'quantity', 'start_date', 'status']]
        #changing to datetime
        df['billing_cycle_anchor'] = pd.to_datetime(df['billing_cycle_anchor'], unit='s')
        df['canceled_at'] = pd.to_datetime(df['canceled_at'], unit='s')
        df['cancel_at'] = pd.to_datetime(df['cancel_at'], unit='s')
        df['created'] = pd.to_datetime(df['created'], unit='s')
        df['current_period_end'] = pd.to_datetime(df['current_period_end'], unit='s')
        df['current_period_start'] = pd.to_datetime(df['current_period_start'], unit='s')
        df['ended_at'] = pd.to_datetime(df['ended_at'], unit='s')
        df['start_date'] = pd.to_datetime(df['start_date'], unit='s')
        #get rid of null values
        df = df.replace({np.NaN: None})
        return df

