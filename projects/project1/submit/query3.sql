SELECT COUNT(item_id) 
FROM Items 
WHERE item_id IN (SELECT item_id FROM Category GROUP BY item_id HAVING count(item_id) = 4);