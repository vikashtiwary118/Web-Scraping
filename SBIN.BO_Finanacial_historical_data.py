from bs4 import BeautifulSoup
import urllib
import requests
import os,os.path



def yahoo_data(url):
    agent = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(url, headers=agent)
    if page.status_code == 200:
        try:
            plain_text = page.text
            soup = BeautifulSoup(plain_text, "html.parser")
            os.chdir(os.path.dirname(__file__))
            current_path = os.getcwd()

            if (os.path.exists(os.path.join(current_path, 'financial_data_history.csv'))):
                os.remove(os.path.join(current_path,'financial_data_history.csv'))
                print('Previous File deleted')

            with open('financial_data_history.csv','a+') as f:
                f.write('Date' + '|' + 'Open' + '|' 'High' + '|' + 'Low' '|' + 'Close' + '|' +'Adj.Close' + '|' + 'Volume')
                f.write('\n')
                for pp in soup.findAll('tr', {'class': 'BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)'}):
                    date=pp.find('td',{'class':  'Py(10px) Ta(start) Pend(10px)'})
                    f.write(date.find('span').text + '|')
                    open_high_close_vol=pp.findAll('td',{'class': 'Py(10px) Pstart(10px)'})
                    for each_value in open_high_close_vol:
                        f.write(each_value.find('span').text + '|')
                    f.write('\n')
            f.close()
            print('Data Extraction successful,check financial_data_history.csv in your current working directory')
        except :
            print('Something bad happened, please try again')
    else:
        print(' Not able to get the response')


if __name__ == '__main__':
    yahoo_data('https://in.finance.yahoo.com/quote/SBIN.BO/history?p=SBIN.BO')
