#generate .dat files from .json files
#python wlyu_parser.py ~/Desktop/ebay_data/items-*.json
python wlyu_parser.py /usr/class/cs145/project/ebay_data/items-*.json

#remove duplicates
sort Items.dat | uniq > Items_uniq.dat
sort Bids.dat | uniq > Bids_uniq.dat
sort AuctionUser.dat | uniq > AuctionUser_uniq.dat
sort Category.dat | uniq > Category_uniq.dat