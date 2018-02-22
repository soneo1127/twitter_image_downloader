# -*- coding: utf-8 -*-
from myauth import api
import tweepy
import os
import tweepy
import urllib.request
import sys

from datetime import datetime as dt

#= 画像の保存先ディレクトリ
tdatetime = dt.now()
tstr = tdatetime.strftime('%Y-%m-%d %H:%M:%S')
os.mkdir(tstr)
IMAGES_DIR = './' + tstr + '/'

user_name = sys.argv[1]

class HobbyImageDownloader(object):
    def __init__(self):
        #super(HobbyImageDownloader, self).__init__()
        self.media_url_list = []

    def run(self):
        self.download_url_list = []
        self.search()
        for url in self.download_url_list:
            print("画像のurl= "+url)
            self.download(url)

    def search(self):
        try:
            for status in tweepy.Cursor(api.user_timeline,screen_name = user_name,exclude_replies = True).items():
                #for status in api.home_timeline():
            #見やすくするための線
                print('-----------------------------------------------------')

                #投稿内容を出力
                print(status.text)
                print("id= " + str(status.id) )
                status = api.get_status(status.id)

                count = 0
                if hasattr(status, "extended_entities"):
                    for media in status.extended_entities['media']:
                        print(media['media_url'])
                        url = media['media_url_https']
                        if url not in self.media_url_list:
                            self.media_url_list.append(url)
                            self.download_url_list.append(url)

                else:
                    print("error")

        #エラーが発生した場合TweepErrorが返ってくる
        except tweepy.TweepError as e:
            #エラー内容を出力
            print(e.reason)

    def download(self, url):
        url_orig = '%s:orig' % url
        filename = url.split('/')[-1]
        savepath = IMAGES_DIR + filename
        try:
            #https = urllib3.PoolManager()
            #response = https.request('GET', url)
            response = urllib.request.urlopen(url_orig)
            with open(savepath, "wb") as f:
                f.write(response.read())
        except Exception as e:
            print ("[-] Error: ", e)

def main():
    try:
        downloader = HobbyImageDownloader()
        downloader.run()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
