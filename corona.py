import str_index
import time
import urllib.request

def _toint(n):
    n = n.replace(",", "")
    try:
        n = int(n)
    except:
        raise Exception("fail to convert str to int")
    return n


def get_data():

    link = "https://www.worldometers.info/coronavirus/"
    with urllib.request.urlopen(link) as response:
        html = response.read().decode("utf-8")
    # get Coronavirus Cases
    index_begin = html.find('#aaa">') + 6   
    # cut html     
    html = html[index_begin:]
    index_end = html.find('</span>')
    covid19_world_cases = html[:index_end].strip()

    # cut html
    html = html[index_end:]
    # get Deaths Number
    index_begin = html.find('<span>') + 6
    # cut html     
    html = html[index_begin:]
    index_end = html.find('</span>')
    deaths_world_number = html[:index_end].strip()

    # get brazil 
    # cut html
    html = html[index_end:]
    index_end = html.find('Brazil') + 11
    # cut html
    html = html[index_end:]
    # get brazil cases
    index_begin = html.find('">') + 2
    # cut html
    html = html[index_begin:]
    index_end = html.find('</td>')
    brazil_covid19_cases = html[:index_end].strip()

    # cut html
    html = html[index_end:]
    index_begin = html.find('">') + 2
    html = html[index_begin:]
    index_begin = html.find('">') + 2
    html = html[index_begin:]
    index_end = html.find('</td>')
    brazil_deaths_number = html[:index_end].strip()

    covid19_world_cases = _toint(covid19_world_cases)
    deaths_world_number = _toint(deaths_world_number)
    brazil_covid19_cases = _toint(brazil_covid19_cases)
    brazil_deaths_number = _toint(brazil_deaths_number)

    world_death_rate = (deaths_world_number * 100) / covid19_world_cases
    brazil_death_rate = (brazil_deaths_number * 100) / brazil_covid19_cases
    world_death_rate = round(world_death_rate, 2)
    brazil_death_rate = round(brazil_death_rate, 2)

    print(f"casos mundo: {covid19_world_cases} | mortos mundo: {deaths_world_number}")
    print(f"casos brasil: {brazil_covid19_cases} | mortos br: {brazil_deaths_number}")
    print(f'mundo: {world_death_rate}% | brazil: {brazil_death_rate}%')

    return (world_death_rate, 
    brazil_death_rate, 
    covid19_world_cases, 
    deaths_world_number, 
    brazil_covid19_cases, 
    brazil_deaths_number) 


def gen_page_html():

    data = get_data()
    localtime = time.asctime(time.localtime(time.time()))
    index = str_index.HTML_INDEX_PAGE.format(data[0], 
    data[1], 
    data[2],
    data[3],
    data[4],
    data[5], 
    localtime)
    
    with open('index.html', 'w') as file:
        file.write(index)


if __name__ == '__main__':
    gen_page_html()