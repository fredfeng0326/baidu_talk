# encoding:utf-8
import urllib.request as urllib2
import json
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=D1r6hjZkh0FXs4yhebUsbe2g&client_secret=74rdSMWGNhFjBeHzoATStHuAd25fC9lt'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
my_json = content.decode('utf8').replace("'", '"')
data = json.loads(my_json)
access_token = ''
if (data):
    access_token = data['access_token']

url = 'https://aip.baidubce.com/rpc/2.0/solution/v1/unit_utterance?access_token=' + access_token
post_data = "{\"scene_id\":100,\"query\":\"贝塔傻不傻？\",\"session_id\":\" \"}"
request = urllib2.Request(url, bytearray(post_data, 'utf8'))
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request)
content = response.read()
response_talk = []
if (content):
    content_json = json.loads(content.decode('utf8'))
    for arr in content_json['result']['action_list']:
        response_talk.append(arr['say'])
    print (response_talk)

