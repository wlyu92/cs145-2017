
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS145 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

def bidder_location(bid_dict):
    if 'Location' in bid_dict:
        return str(bid_dict['Location'])
    else:
        return 'NULL'

def bidder_country(bid_dict):
    if 'Country' in bid_dict:
        return str(bid_dict['Country'])
    else:
        return 'NULL'
def buy_price(item_dict):
    if 'Buy_Price' in item_dict:
        return transformDollar(item_dict['Buy_Price'])
    else:
        return 'NULL'

def clean_quote (str_val):
    return '"'+str_val.replace('"','""')+'"'

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""

def parseJson(json_file):
    
    #Create .dat file for each entity set
    table_Items = open('Items.dat','a')
    table_Bids = open('Bids.dat','a')
    table_User = open('AuctionUser.dat','a')
    table_Cat = open('Category.dat','a')
    
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:
            """
            print (item)
            return
            """
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            
            #Populate Items table
            # item_id | name | currently | buy_price | first_bid, number_of_bids, seller_id, ends, started, description)

            table_Items.write(str(item['ItemID'])+columnSeparator
                +clean_quote(str(item['Name']))+columnSeparator
                +str(transformDollar(item['Currently']))+columnSeparator
                +str(buy_price(item))+columnSeparator
                +str(transformDollar(item['First_Bid']))+columnSeparator
                +str(item['Number_of_Bids'])+columnSeparator
                +clean_quote(str(item['Seller']['UserID']))+columnSeparator
                +str(transformDttm(item['Started']))+columnSeparator
                +str(transformDttm(item['Ends']))+columnSeparator
                +clean_quote(str(item['Description']))+'\n')
            
            # Populate Bids table
            # item_id | bidder_user_id | time_of_bid | amount
            if item['Bids'] == None:
                pass
            else:
                for bid in item['Bids']:
                    table_Bids.write(str(item['ItemID'])+columnSeparator
                        +clean_quote(str(bid['Bid']['Bidder']['UserID']))+columnSeparator
                        +transformDttm(bid['Bid']['Time'])+columnSeparator
                        +transformDollar(str(bid['Bid']['Amount']))+'\n')
                    
            # Populate AuctionUser table
            # user_id | rating | location | country
            # write seller info
            
            table_User.write(str(item['Seller']['UserID'])+columnSeparator
                +str(item['Seller']['Rating'])+columnSeparator
                +clean_quote(str(item['Location']))+columnSeparator
                +clean_quote(str(item['Country']))+ '\n')
            # write bidder info
            if item['Bids'] == None:
                pass
            else:
                for bid in item['Bids']:
                    table_User.write(str(bid['Bid']['Bidder']['UserID'])+columnSeparator
                        +str(bid['Bid']['Bidder']['Rating'])+columnSeparator
                        +clean_quote(bidder_location(bid['Bid']['Bidder']))+columnSeparator
                        +clean_quote(bidder_country(bid['Bid']['Bidder']))+'\n')
            # Populate Category table
            # item_id | category_name
            for cat in item['Category']:
                table_Cat.write(str(item['ItemID'])+columnSeparator
                    +clean_quote(cat)+'\n')
                
            pass
            

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print "Success parsing " + f

if __name__ == '__main__':
    main(sys.argv)






























