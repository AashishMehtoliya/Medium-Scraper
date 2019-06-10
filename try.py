from bs4 import BeautifulSoup
import requests
import pdfkit

query = str(input('Enter your keyword for search\n'))

list_of_link = []
i = 0

def search_query(query):
    source = requests.get('https://medium.com/search?q={}'.format(query)).text
    source = source.encode('utf-8')
    soup = BeautifulSoup(source , "lxml" )



    try :
        for parent in soup.find_all('div', class_ = 'postArticle-content'):
            for link in parent.find_all('a'):
                link = link['href']
                list_of_link.append(link)
                convert_to_pdf(link)

        print(list_of_link)

    except Exception as e:
        print(e)


def convert_to_pdf(link):
    global i
    config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_url(link,'medium-python{}.pdf'.format(str(i)) , configuration = config)
    i = i + 1


search_query(query)












