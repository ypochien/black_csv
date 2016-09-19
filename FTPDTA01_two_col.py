# -*- coding: utf-8 -*-

import csv
import itertools

HTML_HEADER = '''
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
</style>\r'''

with open('data/FTPDTA01.csv' , mode='r' , encoding='cp950') as csvfile:
    reader = csv.reader(csvfile)
    csv_data = list(reader)

with open('out/FTPDTA01.html' , mode='w' , encoding='utf-8') as html_file:
    html_file.write(HTML_HEADER)
    html_file.write('<table align="center">\r')
    r = 0
    break_count = len(csv_data) / 2
    count = int(break_count) + 1
    for row in csv_data[int(break_count):]:
        c1 = row[0]
        c2 = row[1]
        if '收盤' == c2:
            break
        count +=1
    new_data = list(itertools.zip_longest(csv_data[1:count] , csv_data[count:] , fillvalue=''))
    new_data.insert(0,csv_data[0])
    for row in new_data:
        if r == 0:
            c1 = row[0]
            html_file.write('\t\t\t<tr><td COLSPAN=5 align="center">{c1}</td></tr>\r'.format(c1=row[0] , c2=row[1]))
        else:
            c1 = row[0][0]
            c2 = row[0][1]
            row_html = '<tr><td'
            if '收盤' == c2:
                row_html += ' align="right"'
            row_html += '>{c1}</td><td>{c2}</td><td></td>'
            if row[1] != '':
                c3 = row[1][0]
                c4 = row[1][1]
                row_html += '<td'
                if '收盤' == c4:
                    row_html += ' align="right"'
                row_html += '>{c3}</td><td>{c4}</td>\r'
                html_file.write(row_html.format(c1=c1, c2=c2,c3=c3,c4=c4))
            else:
                row_html += '\r'
                html_file.write(row_html.format(c1=c1, c2=c2))
        r += 1

    html_file.write(''' </table>''')
