import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py


def get_data(json, type):
    data = []
    for user in json["users"]:
        data.append(user[type])
    return data


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


print('')
acct = input('Enter Twitter Account: ')
url = twurl.augment(TWITTER_URL,
                    {'screen_name': acct, 'count': '5'})
print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

js = json.loads(data)

type = str(input("Enter data type you want to get: "))
print(get_data(js, type))
print(json.dumps(js, indent=2))
# print(js)
# print(json.dumps(js, indent=2))

# headers = dict(connection.getheaders())
# print('Remaining', headers['x-rate-limit-remaining'])
#
# for u in js['users']:
#     print(u['screen_name'])
#     if 'status' not in u:
#         print('   * No status found')
#         continue
#     s = u['status']['text']
#     print('  ', s[:50])
