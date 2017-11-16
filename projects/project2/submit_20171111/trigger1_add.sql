-- 8. The Current_Price of an item must always match the Amount of the most recent bid for that item.
-- Add a trigger to update the 'currently' attribute on 'Items' table to the newly inserted 'amount' after each insert on Bids table.
PRAGMA foreign_keys = ON;
drop trigger if exists update_currently;
create trigger update_currently after insert ON Bids
	for each row
	begin
		update Items set currently = new.amount where item_id = new.item_id;
	end;