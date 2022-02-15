# read data from url using urllib

import urllib.request

webUrl = urllib.request.urlopen('https://www.google.com')

print("Result code :" + str(webUrl.getcode()))

print("html code : \n", webUrl.read())
