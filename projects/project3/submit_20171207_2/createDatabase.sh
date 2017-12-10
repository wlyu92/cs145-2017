#load into sqlite

#/usr/class/cs145/bin/sqlite3 AuctionBase.db < create.sql
#/usr/class/cs145/bin/sqlite3 AuctionBase.db < load.txt
#/usr/class/cs145/bin/sqlite3 AuctionBase.db < constraints_verify.sql
#/usr/class/cs145/bin/sqlite3 AuctionBase.db < trigger1_add.sql
#/usr/class/cs145/bin/sqlite3 AuctionBase.db < trigger2_add.sql
#/usr/class/cs145/bin/sqlite3 AuctionBase.db < trigger3_add.sql
#/usr/class/cs145/bin/sqlite3 AuctionBase.db < trigger4_add.sql
#/usr/class/cs145/bin/sqlite3 AuctionBase.db < trigger5_add.sql
#/usr/class/cs145/bin/sqlite3 AuctionBase.db < trigger6_add.sql
#/usr/class/cs145/bin/sqlite3 AuctionBase.db < trigger7_add.sql

#~/Documents/2017_18_Aut/cs145-2017/projects/project3/sqlite3 AuctionBase.db < create.sql

sqlite3 AuctionBase.db < create.sql
sqlite3 AuctionBase.db < load.txt
sqlite3 AuctionBase.db < constraints_verify.sql
sqlite3 AuctionBase.db < trigger1_add.sql
sqlite3 AuctionBase.db < trigger2_add.sql
sqlite3 AuctionBase.db < trigger3_add.sql
sqlite3 AuctionBase.db < trigger4_add.sql
sqlite3 AuctionBase.db < trigger5_add.sql
sqlite3 AuctionBase.db < trigger6_add.sql
sqlite3 AuctionBase.db < trigger7_add.sql