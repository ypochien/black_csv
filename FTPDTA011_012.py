# -*- coding: utf-8 -*-

import csv
import io
import sys
import HTML
import itertools



def to_utf8(str_cp950):
    return str_cp950.decode('cp950').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)



with io.open('data/FTPDTA011.csv',mode='rb') as csv_file:
    reader = csv.reader(csv_file)
    data011_ = list(reader)
    data011 = [ row + [''] for row in data011_]

with io.open('data/FTPDTA012.csv',mode='rb') as csv_file:
    reader = csv.reader(csv_file)
    data012 = list(reader)

new_data = itertools.izip_longest(data011[1:],data012[1:],fillvalue='')
final_data=[]
for items in new_data:
    row = []
    for item in items:
        row.extend(item)

    final_data.append(row)
t = HTML.Table(final_data , header_row=data011[0])

with io.open('out/FTPDTA011_012.html', mode='w') as html_file:
    html_file.write(u'''
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
        }
    </style>\r''')
    html_file.write(to_utf8(str(t)))