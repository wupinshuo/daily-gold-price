# 每日黄金价格查询
  
## 介绍
这是一个简单的 Flask Web 服务,用于获取金价数据。目前支持从金价网(www.jinjia.com.cn)获取黄金价格和周大福金价信息。

## 软件架构
- Python 3.10+
- Flask
- Requests
- BeautifulSoup4

## 功能特性

- 实时获取黄金价格
- 支持查询周大福金价
- RESTful API 接口
- JSON 格式数据返回

## 使用说明

1. 创建并激活虚拟环境(Linux/Mac)
```bash
python -m venv venv
source venv/bin/activate 
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行服务
```bash
python src/app.py
```

4. 访问 API
```bash
curl http://localhost:5050/api/gold-prices
```




