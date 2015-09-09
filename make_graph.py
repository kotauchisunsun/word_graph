#coding:utf-8
import sys
from yahooapi import extract_keyphrase
from json import loads,dumps


def download_json(appid,input_file):
	return dumps(
		[
			loads(
				extract_keyphrase( appid , line , "json" )
			)
			for line
			in open(input_file)
		]
	)

def download():
	appid = sys.argv[1]
	filename = sys.argv[2]

	print download_json(appid,filename)

	

if __name__=="__main__":
	import sys
	import codecs
	sys.stdout = codecs.getwriter('utf8')(sys.stdout)

	from itertools import combinations

	json = loads( open( sys.argv[1] ).read() )
	
	pairs = dict()

	for obj in json:
		for pair in combinations(obj.keys(),2):
			key =  frozenset(pair)
			pairs[key] = pairs.setdefault( frozenset(pair) , 0) + 1


	print "graph keys {"
	for (a,b),weight in pairs.iteritems():
		print u'"{0:s}" -- "{1:s}" [ weight = {2:d} ];'.format(a,b,weight)
	print "}"


