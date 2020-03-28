import requests

from lxml import html

page = requests.get('https://covid19ph.com/')

tree = html.fromstring(page.content)

cases = tree.xpath('//phmainlist-comp/@*[name()=":phcases"]')

print(cases)
