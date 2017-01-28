
## README
# Run the following command in the same directory as this Dockerfile
# sudo docker build -t vip-crawler .
# sudo docker run --name crawler -dt -v /local/vip-input:/var/vip-input vip-crawler

FROM python:3
RUN cd /var ; git clone https://github.com/MayankTahil/Spider.git
RUN pip install requests
RUN mkdir /var/vip-input/
RUN touch /var/log/crawler-log.log
WORKDIR /var/Spider 
CMD ["python", "vipCrawler-ssl.py", "/var/vip-input/vips.csv"]
