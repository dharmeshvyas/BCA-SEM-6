import urllib.request
file = urllib.request.urlopen("https://www.python.org/")
#get unicode from url
#charset=file.info().get_content_charset()
#print(charset)
webpage = file.read().decode('utf-8')
print(webpage)