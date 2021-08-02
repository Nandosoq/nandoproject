import os
import pandas as pd


class Olist:

    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrame loaded from csv files
        """
        # Hints: Build csv_path as "absolute path" in order to call this method from anywhere.
        csv_path = '/home/nandosoq/code/Nandosoq/data-challenges/04-Decision-Science/data/csv'
        # Do not hardcode your path as it only works on your machine ('Users/username/code...')
        # Use __file__ as absolute path anchor independant of your computer

        # Make extensive use of `import ipdb; ipdb.set_trace()` to investigate what `__file__` variable is really
        # Use os.path library to construct path independent of Unix vs. Windows specificities

        #Create the list file_names containing all csv file names in the csv directory
        file_names = os.listdir(csv_path)

        for v in file_names:
            if v[-3:] != 'csv':
                file_names.remove(v)


        #Create the list of dict key key_names
        key_names = []

        for v in file_names:

            txt = ''
            txt = v.replace('_dataset.csv', '')
            txt = txt.replace(".csv", "")
            txt = txt.replace('olist_', '')

            key_names.append(txt)

        #Construct the dictionary data

        data = {}

        for (x, y) in zip(key_names, file_names):

            data[x] = pd.read_csv(os.path.join(csv_path, y))

        return data

    def get_matching_table(self):
        """
        01-01 > This function returns a matching table between
        columns [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """

    def ping(self):
        """
        You call ping I print pong.
        """
        print('pong')
