import requests
import time

last_time = time.time()
watch_symbol = 'XDAG_VB'
failed_count = 0
max_delay = 0
requested_count = 0


def get_data(data_sets, symbol):
    for data in data_sets:
        if data['symbol'] == symbol:
            return data
    return None


while True:
    try:
        requested_count += 1
        response = requests.get('https://api.vbitex.com/Usdmark/tickers', timeout=3)
        time_seconds = time.time()
        time_delay = time_seconds - last_time
        last_time = time_seconds
        data_sets = response.json()
        data = get_data(data_sets, watch_symbol)
        if time_delay > max_delay:
            max_delay = time_delay
        print('request delay: ', time_delay,
              '24h:', data['24_num_vb'],
              'max delay: ', max_delay,
              'requested count: ', requested_count,
              'failed count: ', failed_count)

        # print(data)
    except Exception as e:
        failed_count += 1
        print("Get data error!", e)
    # time.sleep(1)
