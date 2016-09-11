# -*- coding: utf-8 -*-

import HTML
import csv
import io
import sys
import itertools

def to_utf8(str_cp950):
    return str_cp950.decode('cp950').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)

with io.open('data/FTPDTA01.csv', mode='rb') as csvfile:
    reader = csv.reader(csvfile)
    csv_data = tuple(reader)

break_count = len(csv_data[1:]) / 2
count = break_count + 1
for row in csv_data[break_count:]:
    if u'收盤' == to_utf8(row[1]):
        break
    count += 1
new_data = tuple(itertools.izip_longest(csv_data[1:count], csv_data[count:], fillvalue=''))
final_data=[]
for items in new_data:
    row = []
    for item in items:
        row.extend(item)
    final_data.append(row)

t = HTML.Table( final_data, header_row=csv_data[0])

with io.open('out/FTPDTA01_using_html.html', mode='w') as html_file:
    html_file.write(u'''
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>
    <style>
        table {
            border-collapse: collapse;
        }
        table, td, th {
            border: 1px solid black;
        }
    </style>\r''')
    html_file.write(to_utf8(str(t)))