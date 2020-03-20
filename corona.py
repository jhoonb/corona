import sys
import str_index
import time
import urllib.request
import datetime


def _toint(n):
    n = n.replace(",", "")
    try:
        n = int(n)
    except:
        raise Exception("fail to convert str to int")
    return n


def _convert2date(ds):
    fmt =  '%m-%d-%Y'
    return datetime.datetime.strptime(ds, fmt)


def sort_csv_file():
    pass


def get_brazil_data():
    pass


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

    print("\n####################################")
    print(f"- Casos no mundo: {covid19_world_cases}")
    print(f"- Número de mortos no Mundo: {deaths_world_number}")
    print(f"- Casos no Brasil: {brazil_covid19_cases}")
    print(f"- Número de Mortos no Brasil: {brazil_deaths_number}")
    print("-"*20)
    print(f"- Taxa de Mortalidade(Mundo): {world_death_rate}%")
    print(f"- Taxa de Mortalidade(Brasil): {brazil_death_rate}%")
    print("\n####################################\n")

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
    if len(sys.argv) > 1:
        if sys.argv[1] == 'monitor':
            print("Press Control + Z to exit...")
            cont_tempo = 0
            cont_max = 60 * 60
            while True:
                tmp = time.asctime(time.localtime(time.time()))
                print(tmp, end="\r")
                if cont_tempo % cont_max == 0:
                    gen_page_html()
                    cont_tempo = 0

                time.sleep(10) # 10 segs
                cont_tempo += 10
    else: 
        gen_page_html()
