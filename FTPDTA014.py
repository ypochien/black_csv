# -*- coding: utf-8 -*-

import csv
import io
import sys
import HTML
import itertools



def to_utf8(str_cp950):
    return str_cp950.decode('cp950').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)



with io.open('data/FTPDTA014.csv',mode='rb') as csv_file:
    reader = csv.reader(csv_file)
    data013 = list(reader)

t = HTML.Table(data013[1:] , header_row=data013[0])

with io.open('out/FTPDTA014.html', mode='w') as html_file:
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