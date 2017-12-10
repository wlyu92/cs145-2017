import web

db = web.database(dbn='sqlite',
        db='AuctionBase.db' #TODO: add your SQLite database filename
    )

######################BEGIN HELPER METHODS######################

# wrapper method around web.py's db.query method
# check out http://webpy.org/cookbook/query for more info
def query(query_string, vars = {}):
    return list(db.query(query_string, vars))

# Enforce foreign key constraints
# WARNING: DO NOT REMOVE THIS!
def enforceForeignKey():
    db.query('PRAGMA foreign_keys = ON')

# initiates a transaction on the database
def transaction():
    return db.transaction()
# Sample usage (in auctionbase.py):
#
# t = sqlitedb.transaction()
# try:
#     sqlitedb.query('[FIRST QUERY STATEMENT]')
#     sqlitedb.query('[SECOND QUERY STATEMENT]')
# except Exception as e:
#     t.rollback()
#     print str(e)
# else:
#     t.commit()
#
# check out http://webpy.org/cookbook/transactions for examples

# returns the current time from your database
def getTime():
    # TODO: update the query string to match
    # the correct column and table name in your database
    query_string = 'SELECT time_current FROM CurrentTime'
    results = query(query_string)
    # alternatively: return results[0]['currenttime']
    return results[0].time_current # TODO: update this as well to match the
                                  # column name

def getItemByID(itemID, userID, category, description, minPrice, maxPrice, status):
    # TODO: rewrite this method to catch the Exception in case `result' is empty

    query_string = 'SELECT * FROM Items i, Category c WHERE i.item_id = c.item_id'
    if itemID:
        query_string += ' AND i.item_id = $itemID'
    if userID:
        query_string += ' AND i.seller_id = $userID'
    if category:
        query_string += ' AND c.category_name = $category'
    if description:
        query_string += ' AND i.description LIKE $description'
    if minPrice:
        query_string += ' AND i.currently >= $minPrice'
    if maxPrice:
        query_string += ' AND i.currently <= $maxPrice'
    
    curr_time = getTime()
    if status == 'open':
        query_string += ' AND i.started <= $curr_time AND $curr_time <=i.ends'
    elif status == 'close':
        query_string += ' AND (i.ends < $curr_time OR i.currently >= i.buy_price)'
    elif status == 'notStarted':
        query_string += ' AND $curr_time < i.started'
    else:
        pass

    # eliminates duplicates
    query_string += ' GROUP BY i.item_id'

    results = query(query_string, {'itemID': itemID, 'userID': userID, 'minPrice': minPrice, 'maxPrice': maxPrice, 'curr_time': curr_time, 'category': category, 'description': "%{0}%".format(description)})
    show_results = []
    # for search results display
    for result in results:
        # key of items must match names specified in search.html!
        items = {}
        items['ItemID'] = result.item_id
        items['Name'] = result.name
        items['End_time'] = result.ends
        items['Buy_Price'] = result.buy_price
        items['SellerID'] = result.seller_id
        items['Currently'] = result.currently
        show_results.append(items)        

    # return to auctionbase.py
    return show_results


#####################END HELPER METHODS#####################

#TODO: additional methods to interact with your database,
# e.g. to update the current time

# # Capability 1: update current time based on selected time input by user
# def setTime(select_time):
#     t = transaction()
#     try:
#         query_string = 'UPDATE CurrentTime SET time_current = $select_time' # put a $ sign here because I want to insert a value later
#         query(query_string, {'select_time':select_time})
#     except Exception as e:
#         t.rollback()
#     else:
#         t.commit()

#Capability 2: auction users to enter bids on open auctions
def addBid(itemID, userID, price):
    addedBid = 0
    query_string = 'INSERT INTO Bids (item_id, bidder_id, time, amount) VALUES ($itemID, $userID, $currTime, $price)'
    currTime = getTime()
    t = transaction()
    try:
        addedBid = db.query(query_string, {'itemID': itemID, 'userID': userID, 'currTime': currTime, 'price': price})
    except Exception as e:
        t.rollback()
#       print str(e)
    else:
        t.commit()
    return addedBid

# for class view
def getAttributes(itemID):
    query_string = 'SELECT * FROM Items WHERE item_id = $itemID'
    attributes = db.query(query_string, {'itemID': itemID})
    return attributes

def getCategories(itemID):
    query_string = 'SELECT c.category_name FROM Items i, Category c WHERE i.item_id = c.item_id AND c.item_id = $itemID'
    categories = query(query_string, {'itemID': itemID})
    return categories

def getBids(itemID):
    query_string = 'SELECT b.bidder_id, b.time, b.amount FROM Items i, Bids b WHERE i.item_id = b.item_id AND i.item_id = $itemID'
    bidders = query(query_string, {'itemID': itemID})
    return bidders

#status of a bid
def getStatus(itemID):
    curr_time = getTime()
    # not started
    query_string_1 = 'SELECT * FROM Items WHERE item_id = $itemID AND $curr_time < started'
    result_1 = query(query_string_1, {'curr_time': curr_time, 'itemID': itemID})
    # ends
    query_string_2 = 'SELECT * FROM Items WHERE item_id = $itemID AND ends < $curr_time'
    result_2 = query(query_string_2, {'curr_time': curr_time, 'itemID': itemID})
    # bidding price is higher than selling price
    query_string_3 = 'SELECT * FROM Items WHERE item_id = $itemID AND currently >= buy_price'
    result_3 = query(query_string_3, {'itemID': itemID})

    status = ''
    if result_1:
        status = 'Status: Not Started.'
    elif result_2 or result_3:
        status = 'Status: Closed.'
        query_string_4 = 'SELECT b.bidder_id FROM Items as i, Bids as b where i.item_id = $itemID and b.item_id = i.item_id and b.amount = i.currently'
        result_4 = query(query_string_4, {'itemID': itemID})
        if result_4:
            status += ' Winning Bid: %s.' % (result_4[0].bidder_id)
        else:
            status += ' No Winning Bid.' 
    else:
        status = 'Status: Open.'
    return status