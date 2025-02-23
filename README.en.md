# daily-gold-price

A simple Flask web service for fetching gold price data. Currently supports fetching gold price and Chow Tai Fook gold price from Gold Price (www.jinjia.com.cn).

## Features

- Real-time gold price fetching
- Chow Tai Fook gold price query
- RESTful API interface
- JSON data return

## Software Architecture

- Python 3.10+
- Flask
- Requests
- BeautifulSoup4

## Installation

1. Create and activate virtual environment (Linux/Mac)
```bash
python -m venv venv
source venv/bin/activate 
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the service
```bash
python src/app.py
```

4. Access the API
```bash
curl http://localhost:5050/api/gold-prices
```

