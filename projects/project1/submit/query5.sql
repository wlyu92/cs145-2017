SELECT COUNT(user_id)
FROM AuctionUser
WHERE rating > 1000 AND user_id IN (SELECT seller_id FROM Items);