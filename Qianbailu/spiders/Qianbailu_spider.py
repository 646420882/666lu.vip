import scrapy
from scrapy import Request
from ..items import QianbailuItem
class Qianbailu(scrapy.Spider):
    name = "Qianbailu"
    index = 'https://666lu.vip'
    pic_classs = ['/html/tupian/toupai','/html/tupian/yazhou','/html/tupian/siwa','/html/tupian/oumei','/html/tupian/mingxing','/html/tupian/qingchun','/html/tupian/dongman']
    pic_names = ['偷拍自拍','亚洲色图','丝袜美腿','欧美性爱','激情明星','清纯唯美','成人动漫']
    #download_delay = 5
    page = 348

    a = int(input('1:偷拍自拍\n2:亚洲色图\n3:丝袜美腿\n4:欧美性爱\n5:激情明星\n6:清纯唯美\n7:成人动漫\n'))-1
    pic_class = pic_classs[a]
    pic_name =  pic_names[a]
    print(pic_name)

    def start_requests(self):
        url = self.index + self.pic_class+ '/index.html'
        yield Request(url, callback=self.get_img_page)
        for i in range(2,self.page+1):
            url = self.index + self.pic_class+'/index_' + str(i) + '.html'
            yield Request(url, callback=self.get_img_page)

    def get_img_page(self,response):
        urls = response.xpath('//div[@class="art"]/ul/li/a/@href').extract()
        for url in urls:
            yield Request(self.index+url,callback=self.get_imgs)
        # for title,url in zip(titles,urls):
        #     print('标题:%s\nURL：%s'%(title,self.index+url))

    def get_imgs(self,response):
        item = QianbailuItem()
        image = []
        name = response.xpath('//meta[@name="keywords"]/@content').extract_first()
        url = response.url
        img_urls = response.xpath('//div[@class="artbody imgbody"]/p/img[contains(@src,".jpg")]/@src').extract()
        for i in img_urls:
            image.append('https:' + i)
        item['pic_class'] = self.pic_name
        item['name'] = name
        item['url'] = url
        item['image_urls'] = image
        yield item
        #

