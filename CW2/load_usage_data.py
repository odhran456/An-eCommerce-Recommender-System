import pandas as pd


datasets = \
    {
        'users':'/Users/Odhran/Documents/Heriot Watt/eCommerce/CW2_excel/users_modified.xlsx',
        'items':'/Users/Odhran/Documents/Heriot Watt/eCommerce/CW2_excel/items_modified.xlsx',
        'users_items':'/Users/Odhran/Documents/Heriot Watt/eCommerce/CW2_excel/user_item_reduced.xlsx'
    }

userlist = pd.read_excel(datasets['users'])
itemlist = pd.read_excel(datasets['items'])
user_item_list = pd.read_excel(datasets['users_items'])

two_tables_joined = pd.merge(user_item_list, itemlist, on='Class')
full_table = pd.merge(two_tables_joined,userlist, on='ID')[['ID','Name','Class','Category','Plan']]
