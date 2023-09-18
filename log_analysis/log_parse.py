import re
from dateutil.parser import parse
from datetime import datetime
import timeit


def log_parse(data):
    # Response Size
    try:
        size = re.search(r'[0-9] (\d{1,6})', data).group(1)
    except AttributeError as e:
        size = 'n/a'
    # Server Response    
    try:
        server_response = re.search(r'http.*?[\"]', data).group(0).replace('"', '')
    except AttributeError as e:
        server_response = 'n/a'
        
    # Date Parameter
    original_date_time_str = re.sub(r':.*', '', re.search(r'\[.*\]', data).group(0).split()[0].replace('[', ''))
    date = parse(timestr=original_date_time_str)
    date_str = date.strftime('%m/%d/%Y')
    
    # Requested resource
    requested_element = re.search(r'"(GET|POST|PUT|PATCH|DEBUG|HEAD|INDEX|PROPFIND|SEARCH|OPTIONS).*" [0-9]', data).group(0)
    if 'GET' in requested_element:
        request_type = 'GET'
        requested_element = requested_element.replace('"GET ', '')
    elif 'POST' in requested_element:
        request_type = 'POST'
        requested_element = requested_element.replace('"POST ', '')
    elif 'PUT' in requested_element:
        request_type = 'PUT'
        requested_element = requested_element.replace('"PUT ', '')
    elif 'PATCH' in requested_element:
        request_type = 'PATCH'
        requested_element = requested_element.replace('"PATCH ', '')
    elif 'DEBUG' in requested_element:
        request_type = 'DEBUG'
        requested_element = requested_element.replace('"DEBUG ', '')
    elif 'HEAD' in requested_element:
        request_type = 'HEAD'
        requested_element = requested_element.replace('"HEAD ', '')
    elif 'INDEX' in requested_element:
        request_type = 'INDEX'
        requested_element = requested_element.replace('"INDEX ', '')
    elif 'PROPFIND' in requested_element:
        request_type = 'PROPFIND'
        requested_element = requested_element.replace('"PROPFIND ', '')
    elif 'SEARCH' in requested_element:
        request_type = 'SEARCH'
        requested_element = requested_element.replace('"SEARCH ', '')
    elif 'OPTIONS' in requested_element:
        request_type = 'OPTIONS'
        requested_element = requested_element.replace('"OPTIONS ', '')
    main_request = re.sub('" [0-9]', '', requested_element).split(' ')[0]
    
    data = data.strip()
    date_str = re.search(r'\[(.*?)\]', data).group(1)
    date = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z')
    request = re.search(r'\"(.*?)\"', data).group(1)
    main_request = request.split()[1]
    request_type = request.split()[0]
    server_response = int(re.search(r'\s(\d{3})\s', data).group(1))
    size = int(re.search(r'\s(\d+)\s', data).group(1))
    user_agent = re.search(r'"(.+?)"', data).group(1)
    ip_address = re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data).group(0)
    host_match = re.search(r'host=(\S+)', data)
    host = host_match.group(1) if host_match else ''
    log_dict = {
        'ip_address': ip_address,
        'date': date,
        'request_type': main_request,
        'request_method': request_type,
        'status_code': server_response,
        'size': size,
        'server_response': server_response,
        'user_agent': user_agent,
        'host': host
    }
    return log_dict


if __name__ == "__main__":
    with open("apache_logs") as file:
        logs = file.readlines()
    log_data = [log_parse(line) for line in logs]
    
    status_code = [(i, log_data[i]['status_code']) for i, line in enumerate(log_data)]
    status_200 = [(status_code[i]) for i, tup in enumerate(status_code) if status_code[i][1] == 200]
    print(len(status_200))
    status_404 = [(status_code[i]) for i, tup in enumerate(status_code) if status_code[i][1] == 404]
    print(len(status_404))