import json
import random

with open('scriptures.json') as scriptures_file:
    scriptures = json.load(scriptures_file)

bom_only = [entry for entry in scriptures if entry["volume_title"] == "Book of Mormon"]
bom_num = len(bom_only)

def get_scripture():
    return bom_only[random.randint(0,bom_num-1)]