from bs4 import BeautifulSoup as bs
import requests

def addingSing(text):
    splittedText = text.split()
    newListText = []

    for i in splittedText:
        if len(i) == 6:
            i+= '™'

        newListText.append(i)

    textWithSign = ' '.join(newListText)
    #print(textWithSign)

    return  textWithSign


def parseFromWebsite(link):
    response = requests.get(link)
    soup = bs(response.text, 'html.parser')
    items = soup.find('span', class_='commtext c00')
    itemsText = items.get_text()

    listOfText = itemsText.split('.')

    newList = []

    for text in listOfText:
        if text.startswith('The header'):
            break
        newList.append(text)

    textOfTask = '.'.join(newList) + '.'
    return textOfTask


def main():
    link_address = 'https://news.ycombinator.com/item?id=13713480'
    textFromLink = parseFromWebsite(link_address)

    print(addingSing(textFromLink))


if __name__ == '__main__':
    main()