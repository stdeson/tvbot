# TvBot
TradingView的下单回调机器人, 基于CCXT和FastAPI

## 1 快速开始

以下步骤建议在有公网IP的服务器上进行:

### 1 拉取代码
> git clone git@github.com:stdeson/tvbot.git

### 2 安装依赖
```bash
sudo apt update
apt install docker.io
apt install docker-compose
```

### 3 修改配置
1. 修改nginx配置
```
vim ./nginx/conf.d/my.conf
# 把 154.26.209.187 改成你自己的ip
:%s#154.26.209.187#your_server_ip#g
```

2. 修改环境变量TV_AUTH_KEY
注意回调的消息入参要保持一致, 此KEY用于避免黑客攻击

3. 修改环境变量OKEX_API_KEY和OKEX_API_SECRET
如果用其它交易所也可以

### 4 运行容器
> make pull

### 5 测试接口
> curl -X POST http://your_server_ip/api/ping

### 6 tradingView上配置回调地址
配置下面这个api
> http://your_server_ip/api/webhook

