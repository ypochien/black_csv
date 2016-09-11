# -*- coding: utf-8 -*-

import csv
import io
import sys

def to_utf8(str_cp950):
    return str_cp950.decode('cp950').encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding)

with io.open('data/FTPDTA01.csv', mode='rb') as csvfile:
    reader = csv.reader(csvfile)
    csv_data = list(reader)

with io.open('out/FTPDTA01.html', mode='w', encoding='utf-8') as html_file:
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

    html_file.write(u'<table>\r')
    r = 0
    for row in csv_data:
        if r == 0:
            c1 = to_utf8(row[0])
            html_file.write(u'\t\t\t<tr><td COLSPAN=2 align="center">{c1}</td></tr>\r'.format(c1=to_utf8(row[0]), c2=to_utf8(row[1])))
        else:
            c1 = to_utf8(row[0])
            c2 = to_utf8(row[1])
            if u'收盤' == c2:
                html_file.write(u'\t\t\t<tr><td align="right">{c1}</td><td>{c2}</td></tr>\r'.format(c1=to_utf8(row[0]), c2=to_utf8(row[1])))
            else:
                html_file.write(u'\t\t\t<tr><td>{c1}</td><td>{c2}</td></tr>\r'.format(c1=to_utf8(row[0]), c2=to_utf8(row[1])))
        r += 1

    html_file.write(u''' </table>''')
