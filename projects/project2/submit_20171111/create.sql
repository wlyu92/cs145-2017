DROP TABLE if exists Items;
DROP TABLE if exists Bids;
DROP TABLE if exists AuctionUser;
DROP TABLE if exists Category;
DROP TABLE if exists CurrentTime;

CREATE TABLE Items (
item_id 	int NOT NULL,
name 		text NOT NULL,
currently 	real NOT NULL,
buy_price	real,
first_bid	real,
number_of_bids	int NOT NULL,
seller_id	text NOT NULL,
started	datetime NOT NULL,
ends	datetime NOT NULL,
description text NOT NULL,
PRIMARY KEY (item_id),
FOREIGN KEY (seller_id) REFERENCES AuctionUser(user_id),
CHECK (started < ends)
);

CREATE TABLE Bids(
item_id	int NOT NULL,
bidder_id text NOT NULL,
time datetime NOT NULL,
amount real NOT NULL,
unique (item_id, time),
unique (item_id,bidder_id,amount),
PRIMARY KEY (bidder_id, time),
FOREIGN KEY (bidder_id) REFERENCES AuctionUser(user_id),
FOREIGN KEY (item_id) REFERENCES Items(item_id)
);

CREATE TABLE AuctionUser(
user_id int NOT NULL,
rating int NOT NULL,
location text,
country text,
PRIMARY KEY (user_id)
);

CREATE TABLE Category(
item_id	int NOT NULL,
category_name text NOT NULL,
PRIMARY KEY (item_id, category_name),
FOREIGN KEY (item_id) REFERENCES Items(item_id)
);

CREATE TABLE CurrentTime(
time_current datetime NOT NULL
);
INSERT INTO CurrentTime values (datetime('2001-12-20 00:00:01'));
SELECT * from CurrentTime;
