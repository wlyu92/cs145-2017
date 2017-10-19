select COUNT(DISTINCT(category_name)) 
from Category 
where item_id in (SELECT DISTINCT(item_id) 
	FROM Bids 
	WHERE amount>100 AND amount<>'NULL');