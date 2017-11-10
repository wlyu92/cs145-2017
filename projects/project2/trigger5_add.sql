--14. Any new bid for a particular item must have a higher amount than any of the previous bids for that particular item.
--Add a trigger to forbid (before) an insertion of each new bids to table 'Bids' if the 'amount' attribute is lower than or equal to the maximum value of all previous 'amount' for the same 'item_id'.
PRAGMA foreign_keys = ON;
drop trigger if exists bid_amount;
create trigger bid_amount before insert ON Bids
	for each row
	when exists (select * from Bids b where b.amount >= new.amount and b.item_id = new.item_id)
	begin
		select raise(rollback, "Any new bid for a particular item must have a higher amount than any of the previous bids for that particular item.")
	end;