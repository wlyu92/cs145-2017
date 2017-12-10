#!/usr/bin/env python

import sys; sys.path.insert(0, 'lib') # this line is necessary for the rest
import os                             # of the imports to work!

import web
import sqlitedb
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

###########################################################################################
##########################DO NOT CHANGE ANYTHING ABOVE THIS LINE!##########################
###########################################################################################

######################BEGIN HELPER METHODS######################
db = web.database(dbn='sqlite',
        db='AuctionBase.db' #TODO: add your SQLite database filename
    )

# helper method to convert times from database (which will return a string)
# into datetime objects. This will allow you to compare times correctly (using
# ==, !=, <, >, etc.) instead of lexicographically as strings.

# Sample use:
# current_time = string_to_time(sqlitedb.getTime())

def string_to_time(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

# helper method to render a template in the templates/ directory
#
# `template_name': name of template file to render
#
# `**context': a dictionary of variable names mapped to values
# that is passed to Jinja2's templating engine
#
# See curr_time's `GET' method for sample usage
#
# WARNING: DO NOT CHANGE THIS METHOD
def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(autoescape=True,
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
            extensions=extensions,
            )
    jinja_env.globals.update(globals)

    web.header('Content-Type','text/html; charset=utf-8', unique=True)

    return jinja_env.get_template(template_name).render(context)

#####################END HELPER METHODS#####################

urls = ('/currtime', 'curr_time',
        '/selecttime', 'select_time',
        # TODO: add additional URLs here
        '/search', 'search',
        '/add_bid', 'add_bid',
        '/view','view', # used to show details of an auction
        # first parameter => URL, second parameter => class name
        )

# Display current time
class curr_time:
    # A simple GET request, to '/currtime'
    #
    # Notice that we pass in `current_time' to our `render_template' call
    # in order to have its value displayed on the web page
    def GET(self):
        current_time = sqlitedb.getTime()
        return render_template('curr_time.html', time = current_time)

# Ability to manually change the "current time."
class select_time:
    # Another GET request, this time to the URL '/selecttime'
    def GET(self):
        return render_template('select_time.html')

    # A POST request
    #
    # You can fetch the parameters passed to the URL
    # by calling `web.input()' for **both** POST requests
    # and GET requests

    def POST(self):
        params = web.input()
        MM = params['MM']
        dd = params['dd']
        yyyy = params['yyyy']
        HH = params['HH']
        mm = params['mm']
        ss = params['ss'];
        enter_name = params['entername']

        selected_time = '%s-%s-%s %s:%s:%s' % (yyyy, MM, dd, HH, mm, ss)
        
        update_message = '(Hello, %s. Previously selected time was: %s.)' % (enter_name, selected_time)
        # TODO: save the selected time as the current time in the database
        t = sqlitedb.transaction()
        try:
            query_string = 'UPDATE CurrentTime SET time_current = $time' # put a $ sign here because I want to insert a value later
            db.query(query_string, {'time':selected_time})
        except Exception as e: 
            update_message = str(e)
            t.rollback()
        else:
            t.commit()
        # Here, we assign `update_message' to `message', which means
        # we'll refer to it in our template as `message'
        return render_template('select_time.html', message = update_message)

# Ability for auction users to enter bids on open auctions.
class add_bid:
    def GET(self):
        return render_template('add_bid.html')
    def POST(self):
        params = web.input()
        itemID = params['itemID']
        userID = params['userID']
        price = params['price']

        currTime = sqlitedb.getTime()
        query_string = 'INSERT INTO Bids (item_id, bidder_id, time, amount) VALUES ($itemID, $userID, $currTime, $price)'
         # if all fields are filled out
        if itemID and userID and price:
            result = sqlitedb.addBid(itemID, userID, price)
            if result:
                message = "You have successfully added a bid!"
                return render_template('add_bid.html', add_result = result, message = message)
            else:
                message = "Your attempt to adding a bid has failed. Please try again."
                return render_template('add_bid.html', add_result = result, message = message)
        # if not all fields are filled out
        else:
            message = "Please fill out all fields."
            return render_template('add_bid.html', message = message)

# class add_bid:
#     def GET(self):
#         return render_template('add_bid.html')
#     def POST(self):
#         post_param = web.input()
#         itemID = post_param['itemID']
#         userID = post_param['userID']
#         price = post_param['price']
        
#         if itemID and userID and price:
#             items = sqlitedb.addBid(itemID, userID, price)
#             if items:
#                 good_message = 'You have successfully added a bid!'
#                 return render_template('add_bid.html', add_result = items, message = good_message)
#             else:
#                 bad_message = 'Your attempt to add a bid violates constraints.'
#                 return render_template('add_bid.html', add_result = items, message = bad_message)
#         else:
#             warning_message = 'Please fill out all fields!'
#             return render_template('add_bid.html', message = warning_message)

# Ability to browse auctions of interest based on the following named input paramters.
class search:
    def GET(self):
        return render_template('search.html')
    def POST(self):
        params = web.input()
        itemID = params['itemID']
        userID = params['userID']
        category = params['category']
        description = params['description']
        minPrice = params['minPrice']
        maxPrice = params['maxPrice']
        status = params['status']
        items = sqlitedb.getItemByID(itemID, userID, category, description, minPrice, maxPrice, status)
        if items:
            return render_template('search.html', search_result = items, message = "We found the following items based on your searching criteria.")
        else:
            return render_template('search.html', search_result = items, message = "Sorry, there are no items that match your searching criteria.")

# view the details of an item/bids on a separate page
class view:
    def GET(item_id):
        i = web.input(item_id=None)
        details = sqlitedb.getAttributes(i.item_id)
        status = sqlitedb.getStatus(i.item_id)
        bids = sqlitedb.getBids(i.item_id)
        categories = sqlitedb.getCategories(i.item_id)
        return render_template('view.html', search_result = details, auction_status = status, search_bids = bids, auction_categories = categories)

###########################################################################################
##########################DO NOT CHANGE ANYTHING BELOW THIS LINE!##########################
###########################################################################################

if __name__ == '__main__':
    web.internalerror = web.debugerror
    app = web.application(urls, globals())
    app.add_processor(web.loadhook(sqlitedb.enforceForeignKey))
    app.run()

