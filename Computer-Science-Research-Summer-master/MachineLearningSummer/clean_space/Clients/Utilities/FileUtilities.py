import datetime
import os
from typing import List
import csv
import json
import re

def readfile(path) -> str:
    """
    get a string for a txt file
    """
    with open(path, 'r', encoding='utf-8') as fd:
        text = fd.read()
    return text

def readcsv(path) -> List[str]:
    """
    read a csv file
    """
    fd = open(path, "r")
    read = list(csv.reader(fd))
    fd.close()
    return read

def read_filelines(path) -> List[str]:
    """
    get an array where each element is a line of text
    """
    fd = open(path)
    text = fd.readlines()
    fd.close()
    return text

def readjson(path):
    """
    read a json file\n
    returns a json object
    """
    fd = open(path, "r")
    jsonobject = json.load(fd)
    fd.close()
    return jsonobject

def write_to_file_in_dir(dir, name, text, type="txt", text_analyzed="") -> str:
    """
    write to a file in a directory
    """
    try:
        # print("Writing to file")
        current_time = datetime.datetime.now()
        try:
            directory_list = os.listdir(dir)
        except:
            raise RuntimeError("Could not locate directory")
        count = 1
        for item in directory_list:
            if re.match(f'{name}_'+r'[0-9]+'+f'.{type}', item):
                count += 1
        path = f"{dir}/{name}_{count}.{type}"
        fd = open(path, "w")
        fd.write(f"New response iteration made at {current_time}\nFor {text_analyzed}\n" + text + "\n")
        # print("Write successful")
        fd.close()
        return path
    except:
        raise RuntimeError("Could not write to file")

def write_to_file(name, text, type="txt") -> str:
    """
    write to a file
    """
    try:
        print("Writing to file")
        current_time = datetime.datetime.now()
        print(current_time)
        path = f"{name}.{type}"
        fd = open(path, "w")
        print("file created")
        fd.write(f"New response iteration made at {current_time}\n" + text + "\n")
        print("Write successful")
        fd.close()
        return path
    except:
        raise RuntimeError("Could not write to file")

def directory_size(directory) -> int:
    """
    find out the size of a directory
    """
    return len(os.listdir(directory)) + 1

def write_tocsv(path, row) -> None:
    """
    write to a csv file\n
    Would append new row to the file if data already exists in the file
    """
    try:
        fd = open(path, "a")
        writer = csv.writer(fd)
        writer.writerow(row)
        fd.close()
    except:
        raise RuntimeError("Could not write to csv file")

def write_tojson(path, data) -> None:
    """
    Write to a json file\n
    Would override file if data already exists in the file
    """
    try:
        fd = open(path, "w")
        json.dump(data, fd)
        fd.close()
    except:
        raise RuntimeError("Could not write to json file")

def write_lines(path, lines) -> str:
    try:
        fd = open(path, 'w')
        fd.writelines(lines)
        fd.close()
        return path
    except:
        raise RuntimeError("Could not write to txt file")

def write_lines_to_dir(dir, name, lines, type="txt") -> str:
    try:
        # print("Writing to file")
        try:
            directory_list = os.listdir(dir)
        except:
            raise RuntimeError("Could not locate directory")
        count = 1
        for item in directory_list:
            if re.match(f'{name}_'+r'[0-9]+'+f'.{type}', item):
                count += 1
        path = ''
        if dir[-1] != '/':
            path = f"{dir}/{name}_{count}.{type}"
        else:
            path = f"{dir}{name}_{count}.{type}"
        write_lines(path, lines)
        return path
    except:
        raise RuntimeError("Could not write to file")

def write_dict_to_csv_in_dir(dir, name, dictionary, column_names) -> str:
    try:
        # print("Writing to file")
        try:
            directory_list = os.listdir(dir)
        except:
            raise RuntimeError("Could not locate directory")
        count = 1
        for item in directory_list:
            if re.match(f'{name}_'+r'[0-9]+'+f'.csv', item):
                count += 1
        path = ''
        if dir[-1] != '/':
            path = f"{dir}/{name}_{count}.csv"
        else:
            path = f"{dir}{name}_{count}.csv"

        write_dict_to_csv(path, dictionary, column_names)
        return path
    except:
        raise RuntimeError("Could not write to file")
    
def write_dict_to_csv(path:str, dictionary:dict[str], column_names: List[str]):
    fd = open(path, 'w')
    writer = csv.DictWriter(fd, column_names)
    writer.writeheader()
    writer.writerows(dictionary)
    fd.close()