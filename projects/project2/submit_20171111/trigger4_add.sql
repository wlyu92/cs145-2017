--13. In every auction, the Numer_of_Bids attribute corresponds to the actual number of bids for that particular item.
--Add a trigger to update the 'number_of_bids' attribute in table 'Items' for a 'item_id' after each new insertion into table 'Bids' for that same 'item_id'.
PRAGMA foreign_keys = ON;
drop trigger if exists update_num_of_bids;
create trigger update_num_of_bids after insert ON Bids
	for each row
	begin
		update Items set number_of_bids = number_of_bids + 1 where item_id = new.item_id;
	end;