--9. A user may not bid on an item he or she is also selling.
--Add a trigger to forbid (before) the insersion of new bids on table 'Bids' if 'bidder_id' attribute is already listed as a 'seller_id' in the 'Items' table for the same 'item_id'.
PRAGMA foreign_keys = ON;
drop trigger if exists no_bid_on_self
create trigger no_bid_on_self before insert ON Bids
	for each row 
	when exists (select * from Items i where i.seller_id = new.bidder_id and i.item_id = new.item_id)
	begin
		select raise (rollback, 'A user may not bid on an item he or she is also selling.')
	end;
