#!/usr/bin/env python3
#how to find the web content?
#use this for force


import sys
import click
import os
import requests


class DIR(object):

    def __init__(self,url,w,e,o,only):
        self.url = url
        self.wordlist = w
        self.file_e = e
        self.output = o
        self.only = only

    def force(self):

        with open(self.wordlist,'r') as f:

            for line in f:
                line = line.strip()
                if self.file_e != '':

                    if self.url[-1] != '/':
                        rep = requests.get(self.url+"/"+line+"."+self.file_e)
                    else:
                        rep = requests.get(self.url+line+"."+self.file_e)

                else:
                    if self.url[-1] != '/':
                        rep = requests.get(self.url+"/"+line)
                    else:
                        rep = requests.get(self.url+line)

                if self.output != '':
                    if self.only.isnumeric():
                        if rep.status_code == int(self.only):
                            with open(self.output,'a') as f:
                                f.write(rep.url+" "+str(rep.status_code)+"\n")
                                f.close()

                    else:
                        with open(self.output,'a') as f:
                            f.write(rep.url+" "+str(rep.status_code)+"\n")
                            f.close()

                print(rep.url,rep.status_code)


            f.close()


@click.command()

@click.option('-w',default='',help='use wordlist to force')
@click.option('-e',default='',help='specific file extension to force: example use -e xml will be force http://url/wordlist.xml')
@click.option('-o',default='',help='save file')
@click.option('-only',default='',help='choce one of them to save web content, such 200,300,400,500')

@click.argument('url')


def OP(url,w,e,o,only):

    if os.path.isfile(w):
        # test on the connect
        try:
            rep = requests.get(url)
        except Exception as e:
            sys.exit(e)

        if not rep.ok:
            sys.exit("connect wrong of the target url")
        else:
            print('ss')
            Dir = DIR(url,w,e,o,only)
            Dir.force()
    else:
        print("we don't have wordlist,use -w")


if __name__=="__main__":
    OP()
