import os
import pandas as pd
import numpy as np
from olist.utils import haversine_distance
from olist.data import Olist


class Order:
    '''
    DataFrames containing all orders as index,
    and various properties of these orders as columns
    '''

    def __init__(self):
        # Assign an attribute ".data" to all new instances of Order
        self.data = Olist().get_data()

    def get_wait_time(self, is_delivered=True):
        """
        02-01 > Returns a DataFrame with:
        [order_id, wait_time, expected_wait_time, delay_vs_expected, order_status]
        and filtering out non-delivered orders unless specified
        """
        # Hint: Within this instance method, you have access to the instance of the class Order in the variable self, as well as all its attributes

        from olist.data import Olist
        olist=Olist()
        data=olist.get_data()
        matching_table = olist.get_matching_table()

        orders = data['orders'].copy()

        dates = [
            'order_purchase_timestamp', 'order_approved_at',
            'order_delivered_carrier_date', 'order_delivered_customer_date',
            'order_estimated_delivery_date'
        ]

        for dat in dates:
            orders[dat] = pd.to_datetime(orders[dat])

        orders['wait_time'] = orders['order_delivered_customer_date'].map(pd.Timestamp.to_julian_date) \
            - orders['order_approved_at'].map(pd.Timestamp.to_julian_date)

        orders['expected_wait_time'] = orders['order_estimated_delivery_date'].map(pd.Timestamp.to_julian_date) \
            - orders['order_approved_at'].map(pd.Timestamp.to_julian_date) \

        orders['delay_vs_expected'] = orders['order_delivered_customer_date'].map(pd.Timestamp.to_julian_date) \
            - orders['order_estimated_delivery_date'].map(pd.Timestamp.to_julian_date)

        orders['delay_vs_expected'] = np.where(orders['delay_vs_expected'] < 0, 0, orders['delay_vs_expected'])

        return orders

    def get_review_score(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, dim_is_five_star, dim_is_one_star, review_score
        """
        from olist.data import Olist
        olist=Olist()
        data=olist.get_data()

        reviews = data['order_reviews'].copy()

        def dim_five_star(d):

            if d == 5:
                return 1
            else:
                return 0

        def dim_one_star(d):
            if d == 1:
                return 1
            else:
                return 0

        reviews["dim_is_five_star"] = reviews["review_score"].map(dim_five_star) # --> Series([0, 1, 1, 0, 0, 1 ...])
        reviews["dim_is_one_star"] = reviews["review_score"].map(dim_one_star) # --> Series([0, 1, 1, 0, 0, 1 ...])

        return reviews[['order_id', 'dim_is_five_star', 'dim_is_one_star', 'review_score']]

    def get_number_products(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, number_of_products
        """

        from olist.data import Olist
        olist=Olist()
        data=olist.get_data()
        df = data['order_items'][['order_id', 'order_item_id']].groupby('order_id').sum()

        df.rename(columns={'order_item_id': 'number_of_products'},
                           inplace=True)
        return df


    def get_number_sellers(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, number_of_sellers
        """
        from olist.data import Olist
        olist = Olist()
        data = olist.get_data()

        df=data['order_items'][['order_id', 'seller_id']].groupby('order_id').nunique()

        df.rename(columns={'seller_id': 'number_of_sellers'},
                           inplace=True)
        return df

    def get_price_and_freight(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, price, freight_value
        """
        from olist.data import Olist
        olist = Olist()
        data = olist.get_data()

        return data['order_items'][['order_id', 'price', 'freight_value'
                                    ]].groupby('order_id').sum()

    def get_distance_seller_customer(self):
        """
        02-01 > Returns a DataFrame with order_id
        and distance between seller and customer
        """
        # Optional
        # Hint: you can use the haversine_distance logic coded in olist/utils.py

    def get_training_data(self, is_delivered=True,
                          with_distance_seller_customer=False):
        """
        02-01 > Returns a clean DataFrame (without NaN), with the following columns:
        [order_id, wait_time, expected_wait_time, delay_vs_expected, order_status,
        dim_is_five_star, dim_is_one_star, review_score, number_of_products,
        number_of_sellers, price, freight_value, distance_customer_seller]
        """
        # Hint: make sure to re-use your instance methods defined above
