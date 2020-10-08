import requests


def get_stock_data(sotck_id):
    url = 'http://hq.sinajs.cn/list={0}'.format(sotck_id)
    r = requests.get(url)
    print(r.text)



def main():
    sotck_id = 'sh601006'
    get_stock_data(sotck_id)


if __name__=='__main__':
    main()

