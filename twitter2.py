import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


def get_data(json, type):
    """
    (str, str) -> dict
    Return a dictionary containing account names as keys and data of given type.
    """
    data = {}
    for user in json["users"]:
        data[user["name"]] = user[type]
    return data


def get_json(name):
    """
    (str) -> dict
    Return json containing data of given twitter account.
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': name, 'count': '200'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    return js


if __name__ == "__main__":
    print('')
    acct = input('Enter Twitter Account: ')
    js = get_json(acct)
    type = str(input("Enter data type you want to get: "))
    print(get_data(js, type))

