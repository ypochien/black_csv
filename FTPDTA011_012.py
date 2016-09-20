# -*- coding: utf-8 -*-

import csv
import itertools

import HTML

HTML_HEADER = '''
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>
    <style>
        table {
            border-collapse: collapse;
            align: center;
        }
        table, td, th {
            border: 1px solid black;
            font-size: 14px;
        }
    </style>\r'''

with open('data/FTPDTA011.csv' , mode='r' , encoding='cp950') as csv_file:
    reader = csv.reader(csv_file)
    data011 = [rec + [' '] for rec in list(reader)]
for item in data011:
    print(item)

with open('data/FTPDTA012.csv' , mode='r' , encoding='cp950') as csv_file:
    reader = csv.reader(csv_file)
    data012 = list(reader)
for item in data012:
    print(item)

new_data = itertools.zip_longest(data011[1:] , data012[1:] , fillvalue='')
final_data = []
for items in new_data:
    row = []
    for item in items:
        row.extend(item)

    final_data.append(row)
t = HTML.Table(final_data)

with open('out/FTPDTA011_012.html' , mode='w' , encoding='utf-8') as html_file:
    html_file.write(HTML_HEADER)
    html_file.write(data011[0][0])
    html_file.write(str(t))
