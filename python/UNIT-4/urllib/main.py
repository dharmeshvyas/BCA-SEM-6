import urllib.request


def main():
    webUrl = urllib.request.urlopen('https://www.google.com')
    print("Result code :" + str(webUrl.getcode()))


if __name__ == "__main__":
    main()

