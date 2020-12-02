import requests #let access to the page content
from bs4 import BeautifulSoup
import datetime
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

#URL of product scan
URL = 'https://www.amazon.es/AMD-Ryzen-5-5600X-Box/dp/B08166SLDF/ref=sr_1_1?'
#URL = 'https://www.amazon.es/AMD-Ryzen-3700X-Procesador-Disipador/dp/B07SXMZLPK/ref=bmx_4/261-0187993-0437100?'
#URL = 'https://www.amazon.es/Corsair-Semitorre-Templado-Ventiladores-Incluidos/dp/B08C74694Z/ref=bmx_6/261-0187993-0437100?'

#User agent
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320'}

#now we can do requests
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser') #obtaining page content with soup

#print(soup.prettify()) --> return the whole content of the page

def scanStock():
    actualTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-7] #obtains the actual time without decimals

    title = soup.find(id="productTitle").get_text().strip()  # obtains the id content (title)
    titleFilter = word_tokenize(str(title))[:10] #Using the nltk library, filters the product title to obtain first 10 words
    showTitle = ' '.join(titleFilter) #concatenates the words obtaining the reduced title

    price = soup.find(id="")

    #print(title)  # Shows the title

    stock = soup.find(id='availability').get_text().strip()  # obtains the id content (availability) and delete spaces with strip()

    if (stock == "En stock."): #If there's stock then show the alert
        print('<', actualTime, '>', '[', showTitle, '] --> (ALERT) Product IN STOCK')
    else:
        print('<', actualTime, '>', '[', showTitle, '] --> (i) Product without stock')

#-- End scanStock()

scanStock()