--11. No auction may have a bid before its start time or after its end time.
--Add a trigger to forbid (before) the insertion of new bid on table 'Bids' if 'time' in table 'Bids' is before 'started' or after 'ends' for the same item_id in table 'Items'.
PRAGMA foreign_keys = ON;
drop trigger if exists auction_time;
create trigger auction_time before insert ON Bids
	for each row
	when exists (select * from items where item_id = new.item_id and (new.time<started or new.time>ends))
	begin
		select raise(rollback, "No auction may have a bid before its start time or after its end time.")
	end;