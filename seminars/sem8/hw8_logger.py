# logger
from datetime import datetime

def logger(data, file_path = 'hw8_log.csv', func_name = None):
    time = datetime.now()
    with open(file_path, 'a', encoding = 'utf-8') as f:
        f.write(f'{time}; {func_name}; {data}\n')