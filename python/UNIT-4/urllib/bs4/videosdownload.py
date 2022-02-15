import requests
import bs4
import os

def Create_dir(videos):

    try:
        dirname = input("Enter Directory name for downlaoding :")
        if dirname =="":
            dirname ="VideoDownloads"
        else:
            os.mkdir(dirname)
    except:
        print("Directory is alreay exist!!!")
        Create_dir()

    ContentDownload(videos,dirname)

def ContentDownload(videos,dirname):
    count = 0
    print(f"Total {len(videos)} files found to download")
    if len(videos)!=0:
        for i,video in enumerate(videos):
            url = video['href']
            print(url)
    else:
        print("there no files downloadable")

def main(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text,'html.parser')
    videos = soup.findAll('video')
    Create_dir(videos)

url = input("Enter url :")
main(url)

