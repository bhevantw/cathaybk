#Standard library imports.
import logging
import os.path

#Related third party imports.
from allure_commons.types import AttachmentType
import allure
import pandas as pd

#Local application/library specific imports.   



def get_data(sheet_name):    
    filename = 'test_data_films.xlsx'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '../test_data', filename)
    df = pd.read_excel(data_path, sheet_name=f"{sheet_name}", dtype=str)        
    df = df.fillna("")    
    raw_data = df.to_dict(orient='records')
    result = []
    for row in raw_data:           
        result.append(modify_data(row))    
    logging.info(f"Get data from excel\n{result}")
    return result

def get_data(sheet_name=None):   
    filename = 'test_data_films.csv'  
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '../test_data', filename)
    df = pd.read_csv(data_path, dtype=str)
    df = df.fillna("")    
    raw_data = df.to_dict(orient='records')
    result = []
    
    for row in raw_data:           
        result.append(modify_data(row))    
        
    logging.info(f"Get data from CSV\n{result}")
    return result

def modify_data(data_row):  
    result = {}        
    for key,value in data_row.items():            
        if " chars" in value:            
           result[key] = int(value.replace(" chars","")) * 'f' 
        else:          
           result[key] = value
    return result