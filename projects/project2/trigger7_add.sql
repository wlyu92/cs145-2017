--16. The current time of your AuctionBase system can only advance forward in time, not backward in time.
--Add a trigger to forbid (before) an attempt to change the 'time_current' attribute on table 'CurrentTime' if the new time is earlier than 'time_current'.
PRAGMA foreign_keys = ON;
drop trigger if exists advance_current_time;
create trigger advance_current_time before update ON CurrentTime
	for each row
	when exists new.time_current<=old.time_current
	begin
		select raise (rollback, "The current time of your AuctionBase system can only advance forward in time, not backward in time.")
	end;
