import requests
from lxml import html
def get(find='Anime memes'):
    find = ''.join(list(map(lambda x: x if x != ' ' else '+', find)))
    response = requests.get(f'https://www.bing.com/images/search?q={find}&form=HDRSC2&first=1')
    page = html.fromstring(response.text)
    urls = page.xpath('//img')
    outmass = []
    for url in urls:
        if 'src2' in url.attrib:
            outmass.append(url.attrib['src2'])
    outmass = list(map(lambda x: x[:x.find('w=42')] + 'w=500&h=500&c=100&' + x[x.find('p=0&'):], outmass))
    return outmass

def save_picture(url):
    url = f'{url}'
    to_save = requests.get(url)
    to_save = to_save.content
    f = open(f'C:\\Users\\aleks\\Desktop\\frog_file\\picture.jpg', 'wb')
    f.write(to_save)
    f.close()
get()