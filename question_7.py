# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:42:47 2023

@author: Efrain Santos Luna

@mail: efrain.santos.consultor@gmail.com

@phone:55-66-18-62-95
"""

import requests
from bs4 import BeautifulSoup

def get_data()->BeautifulSoup:
    """
    This function performs a get request to the url of data.gob and the repsonse obtained
    converts it to a BeautifulSoup object

    Returns
    -------
    BeautifulSoup
        BeautifulSoup object with response.

    """
    url = "https://datos.gob.mx/busca/dataset?_res_format_limit=0"

    response = requests.request("GET", url)

    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def get_num_datasets(soup:BeautifulSoup)->str:
    """
    This function obtains the number of datasets listed in data.gob

    Parameters
    ----------
    soup : BeautifulSoup
        object BeautifulSoup.

    Returns
    -------
    str
        number of datasets in datos.gob.

    """
    elements = soup.find_all('p')
    element = [x for x in elements if 'Datos en datos.gob.mx' in x.text][0]
    element = element.text.strip()
    num_datasets = element.split(' ')[0]
    return num_datasets

def get_datasets_by_type(soup:BeautifulSoup)->dict:
    """

    This function obtains the count grouped by data type
    of datasets listed on the data.gob page

    Parameters
    ----------
    soup : BeautifulSoup
        object BeautifulSoup.

    Returns
    -------
    dict
        dictionary with the obtained counts in the format type_data:count.

    """
    container = soup.find('div', {'id':'item-res_format'})
    container = container.find('ul')
    
    elements = container.find_all('li')
    types_data = {}
    for element in elements:
        strings = element.text.strip().split(' ')
        if strings[-1] != 'Populares Formatos':
            type_name = ' '.join(strings[:-1])
            type_name = type_name.strip()
            num_items = strings[-1]
            num_items = int(num_items.strip()[1:-1])
            types_data[type_name] = num_items
            
    return types_data
    
soup = get_data()
#number of datasets according to the count of datos.gob
num_datasets = get_num_datasets(soup)
print('Datasets in datos.gob:', num_datasets)
#datasets by data type
datasets_types = get_datasets_by_type(soup)
print('Datasets by data type in datos.gob:')
print(datasets_types)
#Number of datasets if we add the datasets by data type
num_datasets_2 = sum(datasets_types.values())






