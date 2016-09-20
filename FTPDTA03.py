# -*- coding: utf-8 -*-

import csv

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
            font-size: 12px;
        }
    </style>\r'''

with open('data/FTPDTA03.csv' , mode='r' , encoding='cp950') as csv_file:
    reader = csv.reader(csv_file)
    data013 = list(reader)

t = HTML.Table(data013[1:])

with open('out/FTPDTA03.html' , mode='w' , encoding='utf-8') as html_file:
    html_file.write(HTML_HEADER)
    html_file.write(data013[0][0])
    html_file.write(str(t))
