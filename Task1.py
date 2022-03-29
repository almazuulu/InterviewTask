from bs4 import BeautifulSoup as bs
import requests

# def parseFromWebsite(link):
#     response = requests.get(link)
#     soup = bs(response.text, 'html.parser')
#     #print(soup)
#
#     items = soup.find_all('div', class_ = 'comment')
#     #print(items)
#
#     items2 = soup.find('span', class_= 'commtext c00')
#     # for i in items2:
#     #     comments = i.find('span', class_='commtext c00').text.strip()
#     #     print(comments)
#
#     firstParagraph = items2.find('p')
#     parentText = firstParagraph.find_parent()
#
#     print(firstParagraph)
#     textOfPar = firstParagraph.get_text()
#
#     listOfText = textOfPar.split('.')
#     print(listOfText)
#
#     newList = []
#
#     for text in listOfText:
#         if text.startswith('The header'):
#             break
#         newList.append(text)
#
#     print(newList)
#     textForTask =  '.'.join(newList)
#     print(textForTask)
#
#     print(textOfPar)
#     firstParagraph = str(firstParagraph)
#
#     listOfPar = firstParagraph.split('<p>')
#     print(listOfPar)
#
#     print(parentText)
#
#
#     # parentFirstPar = firstParagraph.find('p')
#     # print(parentFirstPar)

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
    print(textFromLink)




if __name__ == '__main__':
    main()