#coding:utf-8

import urllib
import urllib2

def extract_keyphrase( appid , text , output_type):
	query = {
		"appid" : appid ,
		"output": output_type,
		"sentence" : text
	}

	url = "http://jlp.yahooapis.jp/KeyphraseService/V1/extract?" + urllib.urlencode(query) 

	return urllib2.urlopen(url).read()


if __name__=="__main__":
	import sys
	import json
	data = json.loads(extract_keyphrase( sys.argv[1] , sys.argv[2] , "json" ))
	
	for k,v in  data.iteritems():
		print k,v
