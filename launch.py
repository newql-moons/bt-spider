import logging

from dht import Spider


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S', )
    spiders = []
    for i in range(5):
        spider = Spider('0.0.0.0', 6886 + i)
        spider.start()
        spiders.append(spider)
    for spider in spiders:
        spider.join()
