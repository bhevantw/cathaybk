from datetime import datetime
import logging


def validate_iso8601_date(date_str):
    try:
        datetime.fromisoformat(date_str)
        logging.debug("validated date = " + date_str)
        return True
    except ValueError:
        logging.debug("invalid date = " + date_str)
        return False
    

def normalize_string(str):
    replaced_str = str.replace('_x000D_', '\r').strip()
    # s = s.replace('\r\n', '')
    logging.info("replaced string = " + replaced_str)
    return replaced_str

def compare_rsp_with_data(rsp, data):
    logging.info("response = " + repr(rsp))
    logging.info("data = " + repr(data))
    if(rsp.strip() == data.strip()):
        return True
    else:
        return False