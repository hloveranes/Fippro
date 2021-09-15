import os
# from database.function import insert_vendor
from database.connection import connect
from operations.on_intstall import on_install
from database.function import delete_data, delete_in_bulk

# get current working directory
current_dir = os.getcwd()

# set the __name__ to the module being run ex __main__
if __name__ == "__main__":
    # reserve func
    # connect() 
    # print(insert_vendor('vendor_4'))
    # on_install()
    # delete_data('body', 21)

    # usage
    # list of tuples contains database IDs
    tuples = [(5,), (6,), (7,)]
    print(tuples)
    delete_in_bulk(tuples, 'body')
# print(current_dir)