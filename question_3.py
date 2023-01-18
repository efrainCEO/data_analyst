# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:56:34 2023

@author: Efrain Santos Luna

@mail: efrain.santos.consultor@gmail.com

@phone:55-66-18-62-95
"""

import requests
import pandas as pd

def get_json_data()->dict:
    """
    This function that allows obtaining the data of the url "url_data" using a
    get petition

    Returns
    -------
    json_data : dict
        Dictionary with the data of response

    """
    url_data ='https://secure.toronto.ca/nm/notices.json'
    response = requests.get(url_data)
    json_data = response.json()
    return json_data

def dict_to_text(dict_to_transfor:dict)->str:
    """
    This function convert a dictionary in text with the format:
        key_1: value_1, key_2: text_2, ....

    Parameters
    ----------
    dict_to_transfor : dict
        Dictionary to transform.

    Returns
    -------
    text : str
        sting result.

    """
    text = ''
    for key in dict_to_transfor:
        text = '{}, {}: {}'.format(text, key, dict_to_transfor[key])
        
    text = text.strip(', ')
    
    return text

def parse_dict(items: object)->str:
    """
    This function transforms a column containing dictionaries or lists of dictionaries
    in text, return a string for each row with the format:
        
        Dict_1 \n dict2 \n dict_n
    

    Parameters
    ----------
    items : object
        object that contain a list or dictionary
        
    Returns
    -------
    final_text : str
        final string

    """
    if type(items) == float:
        return ''
    
    if type(items) == dict:
        items = [items]
     
    final_text = ''
    for item in items:
        text = dict_to_text(item)
        final_text = final_text + text + '\n'

    return final_text
    
def parse_df(df:pd.DataFrame)->pd.DataFrame:
    """
    This function converts to text the different columns that a dataframe contains 
    in dictionary or list format

    Parameters
    ----------
    df : pd.DataFrame
        Data frame with data to transfor.

    Returns
    -------
    df : pd.DataFrame
        Dataframe with tranformed data.

    """
    columns_list = ['uniqueMapUrl', 'topics', 'planningApplicationNumbers']
    for column_list in columns_list:
        df[column_list] = df[column_list].apply(lambda x: '\n'.join(x))


    columns_object = ['eventList', 'contact', 'backgroundInformationList', 'addressList', 'otherReferenceList']
    for column_object in columns_object:
        df[column_object] = df[column_object].apply(parse_dict)
    
    return df

json_data = get_json_data()
records = json_data['Records']
df = pd.DataFrame(records)
df = parse_df(df)
#cambiamos el formato de timestamp a datatime
df['noticeDate'] = pd.to_datetime(df['noticeDate'], unit='ms')
#guardamos el dataframe como csv
df.to_excel('Question 3.xlsx', index=False, encoding='utf-8')
print('CSV file saved')


