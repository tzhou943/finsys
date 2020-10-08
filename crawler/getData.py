import requests


def get_stock_data(stock_id):
    url = 'http://hq.sinajs.cn/list={0}'.format(stock_id)# url for getting data
    return_data = requests.get(url)# send http get request
    # parsing return data
    s = return_data.text
    s = s.split('="')[1].split(',')
    stock_name = s[0] 
    open_price = float(s[1])
    close_price = float(s[2]) 
    current_price = float(s[3])
    max_price = float(s[4])
    min_price = float(s[5])
    # data struct for return 
    dt = {
            'stock_id':stock_id,
            'stock_name':stock_name,
            'open_price':open_price,
            'close_price':close_price,
            'current_price':current_price,
            'max_price':max_price,
            'min_price':min_price
            }
    return dt



def main():
    stock_id_list = ['sh601006','sz399006','sz399001','sz002163','sz000858','sh600519','sz000725',
                    'sz002594','sh600381','sh601318']
    for sotck_id in stock_id_list:
        data = get_stock_data(sotck_id)
        print(data)

if __name__=='__main__':
    main()

