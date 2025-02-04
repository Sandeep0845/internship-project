import scrapy
from scrapy.crawler import CrawlerProcess
import json
import csv


class ReviewSpider(scrapy.Spider):
    name = "review_spider"
    custom_settings = {
		'DOWNLOAD_DELAY': 1 # 1 second delay between each request
		}

    def __init__(self, base_url, *args, **kwargs):
        super(ReviewSpider, self).__init__(*args, **kwargs)
        self.base_url = base_url
        self.reviews = []
        self.page_number = 1
        self.end_page = 1000
        
    def start_requests(self):
        for self.page_number in range(1, self.end_page):
            yield scrapy.Request(
                url=self.base_url.format(page=self.page_number)
            )

    def parse(self, response):
        # Find all review elements with IDs that start with 'review_'
        review_elements = response.xpath("//*[starts-with(@id, 'review-')]")

        for review in review_elements:
            review_html = review.get()

            review_id = review.xpath("./@id").get()  # review-id
            review_datePublished = review.xpath(".//meta[@itemprop='datePublished']/@content").get()  # datePublished
            review_author = review.xpath(".//meta[@itemprop='name']/@content").get()  # Author
            review_jobTitle = review.xpath(".//meta[@itemprop='jobTitle']/@content").get()  # jobTitle
            review_worksFor = review.xpath(".//meta[@itemprop='worksFor']/@content").get()  # worksFor
            review_workLocation = review.xpath(".//meta[@itemprop='workLocation']/@content").get()  # workLocation
            review_ratingValue = review.xpath(".//meta[@itemprop='ratingValue']/@content").get()  # ratingValue
            review_bestRating = review.xpath(".//meta[@itemprop='bestRating']/@content").get()  # bestRating
            review_worstRating = review.xpath(".//meta[@itemprop='worstRating']/@content").get()  # worstRating
          
            rating_overall = review.xpath(".//span[contains(@class, 'avg-rating')]/text()").get()
            rating_promotions = review.xpath(".//div[@class='avg_review_item'][1]/p[contains(@class, 'rating-val')]/text()").get().strip()
            rating_skilldev = review.xpath(".//div[@class='avg_review_item'][2]/p[contains(@class, 'rating-val')]/text()").get().strip()
            rating_culture = review.xpath(".//div[@class='avg_review_item'][3]/p[contains(@class, 'rating-val')]/text()").get().strip()
            rating_worksatis = review.xpath(".//div[@class='avg_review_item'][4]/p[contains(@class, 'rating-val')]/text()").get().strip()
            rating_salarybenifits = review.xpath(".//div[@class='avg_review_item'][5]/p[contains(@class, 'rating-val')]/text()").get().strip()
            rating_jobsecurity = review.xpath(".//div[@class='avg_review_item'][6]/p[contains(@class, 'rating-val')]/text()").get().strip()
            rating_worklifebal = review.xpath(".//div[@class='avg_review_item'][7]/p[contains(@class, 'rating-val')]/text()").get().strip()

            likes = review.xpath(".//h3[contains(@class, 'input-fields')]/following-sibling::p[1]/text()").get()
            dislikes = review.xpath(".//h3[contains(@class, 'input-fields')]/following-sibling::p[2]/text()").get()
            work_details = review.xpath(".//h3[contains(@class, 'input-fields')]/following-sibling::p[position() > 3]//text()").getall()
            
            self.reviews.append(
                {
                    "review_id": review_id,
                    "review_datePublished": review_datePublished,
                    "review_author": review_author,
                    "review_jobTitle": review_jobTitle,
                    "review_worksFor": review_worksFor,
                    "review_workLocation": review_workLocation,
                    "review_ratingValue": review_ratingValue,
                    "review_bestRating": review_bestRating,
                    "review_worstRating": review_worstRating,
                    "rating_overall": rating_overall,
                    "rating_promotions": rating_promotions,
                    "rating_skilldev": rating_skilldev,
                    "rating_culture": rating_culture,
                    "rating_worksatis": rating_worksatis,
                    "rating_salarybenifits": rating_salarybenifits,
                    "rating_jobsecurity": rating_jobsecurity,
                    "rating_worklifebal": rating_worklifebal,
                    "likes": likes,
                    "dislikes": dislikes,
                    "work_details": work_details,
                }
            )

        with open('reviews.json', 'w', encoding='utf-8') as f:
            json.dump(self.reviews, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    base_url_to_scrape = "https://www.ambitionbox.com/reviews/jio-reviews?page={page}&sort_by=popularity"
    process = CrawlerProcess()
    process.crawl(ReviewSpider, base_url=base_url_to_scrape)
    process.start()
