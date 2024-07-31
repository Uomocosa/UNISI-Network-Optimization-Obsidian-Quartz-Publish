[GitHub - Original](https://gist.github.com/hixann/af466e96b1988b67fdde5b2afdb735cf)

```python
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import requests
import json
import wget
import sys
from termcolor import cprint, colored
from collections import OrderedDict

headers = {'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}

#===========================def func======================================================

#Coloring some text
def colorify_output(text, text2 = None,COLOR = None, on_COLOR = None):
    output_text = colored('%s'%text,'%s'%COLOR,'%s'%on_COLOR,attrs =[] )
    return output_text


#The main function
def main():
    try:
        book_title = sys.argv[1]
        result = search(book_title)
        if result:
            print_result(result)
            download(result)
    except KeyboardInterrupt:
        print('\n')
        print(colorify_output('Bye Bye',COLOR = 'red', on_COLOR = 'on_grey'),'\n')

#Get Ids values from the table
def search(book_title):
    value = {'req':book_title}
    qstring = urllib.parse.urlencode(value)
    url = "http://libgen.io/search.php?%s&open=0&res=100&view=simple&phrase=1&column=def" % qstring
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    resp_data = resp.read()
    soup = BeautifulSoup(resp_data,"lxml")
    table = soup.find('table',{'class':'c'})
    trs = table.find_all('tr')[1:]
    rows = [tr.find_all('td') for tr in trs]
    ids = [row[0].text for row in rows]
    if not ids:
        print("Book not found")
        try_agian = input('Do you want to try again? [y/n] :')
        if try_agian in 'yY':
            search(book_title)
        else:
            return
    # url = 'http://libgen.io/json.php?ids=%s&fields=Title,Author,MD5,edition,id,year,filesize'%(",".join(ids))

    url = 'http://libgen.io/json.php?ids=%s&fields=Title,Author,MD5,edition,id,extension,year,filesize'%(",".join(ids))

    req = requests.get(url)
    json = req.json()
    return json


#Get detailed book view : Book title,author,id, md5 and edition
def print_result(result):
            count_id = 0

            for book in result:
                #To Do: filesize in Mb

                book['filesize'] = str(round(int(book['filesize'])/(1024*1024),1)) + ' Mb'
                book['serial_No'] = str(count_id)

                # Dictionary with ordered keys
                main_dict = OrderedDict()
                main_dict['Title'] = book['title']
                main_dict['Author'] = book['author']
                main_dict['edition'] = book['edition']
                main_dict['filesize'] = book['filesize']
                main_dict['year'] = book['year']
                main_dict['id'] = book['id']
                main_dict['MD5'] = book['md5']
                main_dict['extension'] = book['extension']
                main_dict['serial_No'] = str(count_id)

                print('-----***------')
                print(colorify_output(count_id, COLOR='yellow', on_COLOR = 'on_grey'))
                print('-----***------')
                for key, value in main_dict.items():
                    key = colored(key, 'red', 'on_grey', ['bold','underline'])
                    # value = colorify_output(value, COLOR ='red', on_COLOR ='on_white')
                    if key == 'md5' or key == 'serial_No':
                        pass
                    else:
                        print(key, value, sep="\t\t")
                count_id += 1


def download(json):
    print('==================================================')
    id = input('Write the ID of the desired book :')
    for book in json:

        if id == book["serial_No"]:
            print('Your book was : %s'% book['title'])
            print('It is being fetched...')
            url = 'http://libgen.io/get.php?md5=%s'%(book['md5'])
            req = urllib.request.Request(url,headers=headers)
            resp = urllib.request.urlopen(req)
            resp_data = resp.read()
            soup = BeautifulSoup(resp_data,"lxml")
            for item in soup.find_all('a'):
                if 'http' in str(item.get('href')):
                    link = item.get('href')
                    print("That's your link: %s"%link)
                    wget.download(link,"../Books/")
                    print('\n')

main()
```