# -*- coding: utf-8 -*-
from myauth import api
import tweepy
import os
import tweepy
import urllib.request

from datetime import datetime as dt

#= 画像の保存先ディレクトリ
tdatetime = dt.now()
tstr = tdatetime.strftime('%Y-%m-%d %H:%M:%S')
os.mkdir(tstr)
IMAGES_DIR = './' + tstr + '/'

pager = 0

class HobbyImageDownloader(object):
    def __init__(self):
        #super(HobbyImageDownloader, self).__init__()
        self.media_url_list = []
        self.media_id_list = []
        self.image_list = 0

    def run(self):
        self.download_url_list = []
        self.search()
        for url in self.download_url_list:
            self.download(url)

    def search(self):
        try:
            for status in api.list_timeline('ATH_ray_', 'kamieshi', count=200, page=pager):
            #for status in api.home_timeline():
            #見やすくするための線
                print('-----------------------------------------------------')

                #ユーザーネームを出力
                print('name:' + status.user.name)

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
                            self.media_id_list.append(media['display_url'])

                else:
                    print("error")

        #エラーが発生した場合TweepErrorが返ってくる
        except tweepy.TweepError as e:
            #エラー内容を出力
            print(e.reason)

    def download(self, url):
        url_orig = '%s:orig' % url
        filename = self.media_id_list[self.image_list].split('/')[-1]
        self.image_list = self.image_list+1
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
        for i in range(10):
            downloader = HobbyImageDownloader()
            downloader.run()
            global pager
            pager = pager+1
            print(pager)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
