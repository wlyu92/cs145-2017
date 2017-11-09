SELECT COUNT(DISTINCT seller_id)
FROM Items, Bids
WHERE seller_id = bidder_id;