--15. All new bids must be placed at the time which matches the current time of your AuctionBase system. 
--Add a trigger to update 'time' attribute after each new insertion to table 'Bids' to 'time_current' of table 'CurrentTime'.
PRAGMA foreign_keys = ON;
drop trigger if exists update_bid_time;
create trigger update_bid_time after insert ON Bids
	for each row
	begin
		update Bids set time = (select * from CurrentTime)
			where item_id = new.item_id;
	end;