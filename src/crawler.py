import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class GoldPriceCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': os.getenv('USER_AGENT')
        }
        self.base_url = os.getenv('BASE_URL')
    
    def get_page_content(self):
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.encoding = 'utf-8'
            return response.text
        except Exception as e:
            print(f"获取页面时发生错误: {str(e)}")
            return None

    def parse_gold_prices(self, html_content):
        if not html_content:
            return None
        
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 获取今日金价
            gold_price = None
            price_rows = soup.find_all('li')
            for row in price_rows:
                name_div = row.find('div', class_='name')
                if name_div and '今日金价' in name_div.text:
                    price_div = row.find('div', class_='new')
                    if price_div:
                        price_span = price_div.find('span')
                        if price_span:
                            gold_price = price_span.text.strip()
                    break

            # 获取周大福金价
            ctf_price = None
            rows = soup.find_all('li')
            for row in rows:
                name_div = row.find('div', class_='name')
                if name_div and '周大福' in name_div.text:
                    price_div = row.find('div', class_='new')
                    if price_div:
                        price_span = price_div.find('span', class_='npx')
                        if price_span:
                            ctf_price = price_span.text.strip()
                    break

            data = {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'gold_price': gold_price,
                'ctf_price': ctf_price
            }
            
            print("解析到的数据:", data)
            return data
            
        except Exception as e:
            print(f"解析数据时发生错误: {str(e)}")
            return None

    def save_to_csv(self, data):
        if not data:
            return False
        
        try:
            df = pd.DataFrame([data])
            file_path = os.path.join('data', 'gold_prices.csv')
            
            # 如果文件存在，追加数据；如果不存在，创建新文件
            if os.path.exists(file_path):
                df.to_csv(file_path, mode='a', header=False, index=False)
            else:
                df.to_csv(file_path, index=False)
            
            return True
        except Exception as e:
            print(f"保存数据时发生错误: {str(e)}")
            return False

    def run(self):
        html_content = self.get_page_content()
        if html_content:
            data = self.parse_gold_prices(html_content)
            if data:
                if self.save_to_csv(data):
                    print("数据已成功保存！")
                    print(f"今日金价: {data['gold_price']}")
                    print(f"周大福金价: {data['ctf_price']}")
                else:
                    print("数据保存失败！")
            else:
                print("数据解析失败！")
        else:
            print("获取页面内容失败！") 