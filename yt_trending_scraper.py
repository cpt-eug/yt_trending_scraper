from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import csv

def trend_scrape():
    date_today = datetime.today().strftime('%Y%m%d')
    header = ['Rank','Title','URL','Uploader','Channel URL','Uploaded','Views']
        
    url = 'https://www.youtube.com/feed/trending'
    driver = webdriver.Chrome()
    driver.get(url)

    videos = driver.find_elements(By.CLASS_NAME, "style-scope ytd-video-renderer")

    count = 0

    #with open('yt_trend_{date}.csv'.format(date=date_today), 'w', encoding='utf-16', newline='') as openfile:
        #writer = csv.writer(openfile)
        #writer.writerow(header)
        
    with open('yt_trend_{date}.csv'.format(date=date_today), 'w', encoding='utf-16', newline='') as openfile:
        writer = csv.writer(openfile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(header)
    
        for video in videos:
            if count == 50:
                continue
            title_div = video.find_element(By.XPATH,'.//*[@id="video-title"]')
            title = title_div.text
            yt_url = title_div.get_attribute("href")
            views = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
            upload_date = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text
            uploader_info = video.find_element(By.XPATH,'.//*[@id="text"]/a')
            uploader = uploader_info.text
            uploader_link = uploader_info.get_attribute("href")
            writer.writerow([count+1,title,yt_url,uploader,uploader_link,upload_date,views])
            count += 1
            
        print('scraping done')
        
    
if __name__ == "__main__":
    trend_scrape()