from Spider import *
from time import sleep
from random import randint, random


# vips = [
#     #"http://<vip>:port/",
#     "http://172.16.0.11:8080",
#     "http://172.16.0.11:8081",
#     "http://172.16.0.11:8082",
#     "http://172.16.0.11:8083",
#     "http://172.16.0.11:8084",
#     "http://172.16.0.11:8085",
#     "http://172.16.0.11:8086",
#     "http://172.16.0.11:8087",
#     "http://172.16.0.11:8088",
#     "http://172.16.0.11:8089",
#     "http://172.16.0.11:8090",
#     "http://172.16.0.11:8091",
# ]

## For Testing
vips = [
    "http://dreamhost.com"
    "http://dreamhost.com"
]

numOfVips = len(vips)
completedVips = 0
while completedVips > -1:
    try:
        urls2seekDeep = randint(3, 20)
        vip = vips[randint(0, numOfVips)]
        spider(vip, urls2seekDeep)
    except:
        pass

#spider("http://www.dreamhost.com", 5)

