from flask import Flask, jsonify
from crawler import GoldPriceCrawler
import os
app = Flask(__name__)

@app.route('/api/gold-prices', methods=['GET'])
def get_gold_prices():
    crawler = GoldPriceCrawler()
    html_content = crawler.get_page_content()
    if html_content:
        data = crawler.parse_gold_prices(html_content)
        if data:
            return jsonify({
                'success': True,
                'status': 200,
                'data': {
                    'date': data['date'],
                    'gold_price': data['gold_price'],
                    'ctf_price': data['ctf_price']
                }
            })
    return jsonify({
        'success': False,
        'message': '获取数据失败'
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
