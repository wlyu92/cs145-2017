--2. All sellers and bidders must exist as users
SELECT seller_id 
FROM Items 
WHERE seller_id NOT IN (SELECT user_id FROM AuctionUsers);
SELECT bidder_id
FROM Bids
WHERE bidder_id NOT IN (SELECT user_id FROM AuctionUsers);

--SELECT seller_id, bidder_id
--FROM Items
--LEFT OUTER JOIN Bids ON item_id
--WHERE (seller_id NOT IN (SELECT user_id FROM AuctionUsers)) OR 
--	(seller_id NOT IN (SELECT user_id FROM AuctionUsers));
--4. Every bid must correspond to an actual item
SELECT item_id
FROM Bids
WHERE item_id NOT IN (SELECT i.item_id FROM Items i);
--5. The items for a given category must all exist
SELECT item_id 
FROM Category
WHERE item_id NOT IN (SELECT i.item_id FROM Items i);