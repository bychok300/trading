import requests
import json 
    

tiker_list = [{"name": "AAVEUSDT", "dollar_value": 250000.0}, {"name": "ADAUSDT", "dollar_value": 500000.0}, 
              {"name": "ALGOUSDT", "dollar_value": 100000.0}, {"name": "ALPHAUSDT", "dollar_value": 100000.0}, 
              {"name": "ATOMUSDT", "dollar_value": 200000.0}, 
              {"name": "AVAXUSDT", "dollar_value": 100000.0}, {"name": "AXSUSDT", "dollar_value": 50000.0},
              {"name": "BALUSDT", "dollar_value": 50000.0}, {"name": "BANDUSDT", "dollar_value": 500000.0},
              {"name": "BATUSDT", "dollar_value": 100000.0}, {"name": "BCHUSDT", "dollar_value": 500000.0},
              {"name": "BNBUSDT", "dollar_value": 500000.0}, {"name": "BZRXUSDT", "dollar_value": 100000.0}, 
              {"name": "COMPUSDT", "dollar_value": 50000.0}, {"name": "CRVUSDT", "dollar_value": 200000.0},
              {"name": "CTKUSDT", "dollar_value": 50000.0}, {"name": "CVCUSDT", "dollar_value": 100000.0},
              {"name": "DASHUSDT", "dollar_value": 100000.0}, {"name": "EGLDUSDT", "dollar_value": 100000.0},
              {"name": "DOTUSDT", "dollar_value": 100000.0}, {"name": "ENJUSDT", "dollar_value": 100000.0},
              {"name": "EOSUSDT", "dollar_value": 200000.0}, {"name": "ETCUSDT", "dollar_value": 100000.0},
              {"name": "FTMUSDT", "dollar_value": 100000.0}, {"name": "HNTUSDT", "dollar_value": 20000.0},
              {"name": "KSMUSDT", "dollar_value": 30000.0}, {"name": "LINKUSDT", "dollar_value": 500000.0},
              {"name": "LRCUSDT", "dollar_value": 300000.0}, {"name": "LTCUSDT", "dollar_value": 300000.0},
              {"name": "MKRUSDT", "dollar_value": 50000.0}, {"name": "NEARUSDT", "dollar_value": 100000.0},
              {"name": "NEOUSDT", "dollar_value": 100000.0}, {"name": "OCEANUSDT", "dollar_value": 100000.0},
              {"name": "OMGUSDT", "dollar_value": 50000.0}, {"name": "RENUSDT", "dollar_value": 100000.0},
              {"name": "QTUMUSDT", "dollar_value": 100000.0}, {"name": "RLCUSDT", "dollar_value": 50000.0},
              {"name": "RSRUSDT", "dollar_value": 100000.0}, {"name": "SKLUSDT", "dollar_value": 100000.0},
              {"name": "RUNEUSDT", "dollar_value": 100000.0}, {"name": "SNXUSDT", "dollar_value": 200000.0},
              {"name": "SOLUSDT", "dollar_value": 50000.0}, {"name": "STORJUSDT", "dollar_value": 100000.0},
              {"name": "SRMUSDT", "dollar_value": 50000.0}, {"name": "THETAUSDT", "dollar_value": 100000.0},
              {"name": "SUSHIUSDT", "dollar_value": 250000.0}, {"name": "TRXUSDT", "dollar_value": 100000.0},
              {"name": "SXPUSDT", "dollar_value": 500000.0}, {"name": "VETUSDT", "dollar_value": 200000.0},
              {"name": "TOMOUSDT", "dollar_value": 100000.0}, {"name": "WAVESUSDT", "dollar_value": 200000.0},
              {"name": "TRBUSDT", "dollar_value": 100000.0}, {"name": "XLMUSDT", "dollar_value": 500000.0},
              {"name": "UNIUSDT", "dollar_value": 200000.0}, {"name": "XMRUSDT", "dollar_value": 250000.0},
              {"name": "XRPUSDT", "dollar_value": 1000000.0}, {"name": "YFIIUSDT", "dollar_value": 100000.0},
              {"name": "YFIUSDT", "dollar_value": 300000.0}, {"name": "ZENUSDT", "dollar_value": 150000.0},
              {"name": "ZILUSDT", "dollar_value": 100000.0}, {"name": "ZRXUSDT", "dollar_value": 100000.0}]

amount_dollars = 150000.0
qty_prices = []

def getTikerCurrentPrice(ticker_name):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=" + ticker_name
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    json_rs = response.json()
    return (str(json_rs["price"]))

def findByTikerName(name):
    for el in tiker_list:
        if (el['name'] == name):
            return el
        
def custom_filter(data_array, min_value):
    rs_array = []
    for i in data_array: 
        if (float(i[1]) >= min_value):
            rs_array.append(i)
    return rs_array

def get_big_amount(ticker_name, tiker_cur_price):
    return findByTikerName(ticker_name)["dollar_value"] / float(tiker_cur_price)

def getHigthBidAskQty(ticker_name): 

    url = "https://api.binance.com/api/v3/depth?symbol="+ticker_name+"&limit=100"
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    json_rs = response.json()
    asks = json_rs["asks"]
    bids = json_rs["bids"]
    
    tiker_cur_price = getTikerCurrentPrice(ticker_name)
    
    filtred_asks = custom_filter(asks, get_big_amount(ticker_name, tiker_cur_price))
    filtred_bids = custom_filter(bids, get_big_amount(ticker_name, tiker_cur_price))
    
    if (len(filtred_asks) > 0 or len(filtred_bids) > 0):
        
        print(ticker_name + ":")
        print("Tiker current price: "+ tiker_cur_price)

        for i in filtred_asks:
            print("ASK: ")
            i.append(float(i[0]) * float(i[1]))
            print(i)
         
        for i in filtred_bids:
            print("BID: ")
            i.append(float(i[0]) * float(i[1]))
            print(i)

print("Script has been running")
for i in tiker_list: 
    getHigthBidAskQty(i["name"])
    
print("Script has been stopped")
