#! /bin/env python
# -*- coding: utf-8 -*-

import cPickle as p
import weiboconfig as config
import client
import sys 

reload(sys) 
sys.setdefaultencoding('utf-8')

# Control parameters,EDIT here!
## UID means the user you want to analysis
UID ='1670662622' 

def writefile(filename,content):
    fw = file(filename,'a')
    fw.write(content)
    fw.close()


def getfriends(uid):
	"""Get the uid's friends and return the dict with uid as key,name as value."""
	print "Get %s 's friend list" % str(uid)
	dict1 = {}
	Client = client.Client.instance()
	if Client._init ==0:
		Client.init()
	users = Client.get_friend_bilateral(uid).users
	for user in users:
		no = user['id']
		uname = user['screen_name']
		dict1[no] = uname
	return dict1
	
def getdict(uid):
    """cache dict of uid in the disk."""
    try:
        with open(str(uid) + '.txt', 'r') as f:
            dict_uid = p.load(f)
    except:
        with open(str(uid) + '.txt', 'w') as f:
            p.dump(getfriends(uid), f)
        dict_uid = getdict(uid)
    return dict_uid

def getfriendsid(uid):
	"""Get the ids of the uid's friends and return the list"""
	print "Get %s 's friend ID list" % str(uid)
	Client = client.Client.instance()
	if Client._init ==0:
		Client.init()
	ids = Client.get_friend_bilateral_id(uid).ids
	return ids

def getfanscount(uids):
	Client = client.Client.instance()
	if Client._init ==0:
		Client.init()
	count = Client.get_user_counts(uids)
	return count
	
if __name__ == "__main__":
	dict_root = getdict(UID)
	for uid1, uname1 in dict_root.items():
		count1 = getfanscount(uid1)
		fans_count1 = count1[0].followers_count
		ids = getfriendsid(uid1)
		count_list = []
		for i in range(0,len(ids),99):
			ids_temp=ids[i:i+99]
			str_ids_temp = [str(item) for item in ids_temp]
			str_ids= ','.join(str_ids_temp)
			count_temp = getfanscount(str_ids)
			for count_temp_item in count_temp:
				count_list.append(count_temp_item.followers_count)
		average_count = sum(count_list)/len(count_list)
		writefile('C:/result.txt',str(uid1)+','+uname1+',')
		writefile('C:/result.txt',str(fans_count1)+',')
		writefile('C:/result.txt',str(average_count)+'\n')
	