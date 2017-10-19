SELECT item_id 
FROM Items 
WHERE currently = (SELECT max(currently) FROM Items);
