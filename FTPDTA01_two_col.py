# -*- coding: utf-8 -*-

import csv
import io
import sys
import itertools

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

    html_file.write(u'<table align="center">\r')
    r = 0
    break_count = len(csv_data) / 2
    print break_count

    count = break_count+1
    for row in csv_data[break_count:]:
        c1 = to_utf8(row[0])
        c2 = to_utf8(row[1])
        if u'收盤' == c2:
            break
        count +=1
    new_data = list(itertools.izip_longest(csv_data[1:count],csv_data[count:],fillvalue=''))
    print 'Total record [{}].'.format(len(csv_data))
    new_data.insert(0,csv_data[0])
    for row in new_data:
        if r == 0:
            c1 = to_utf8(row[0])
            html_file.write(u'\t\t\t<tr><td COLSPAN=5 align="center">{c1}</td></tr>\r'.format(c1=to_utf8(row[0]), c2=to_utf8(row[1])))
        else:
            c1 = to_utf8(row[0][0])
            c2 = to_utf8(row[0][1])
            row_html = u'<tr><td'
            if u'收盤' == c2:
                row_html += u' align="right"'
            row_html += u'>{c1}</td><td>{c2}</td><td></td>'
            if row[1] != '':
                c3 = to_utf8(row[1][0])
                c4 = to_utf8(row[1][1])
                row_html += u'<td'
                if u'收盤' == c4:
                    row_html += u' align="right"'
                row_html += u'>{c3}</td><td>{c4}</td>\r'
                html_file.write(row_html.format(c1=c1, c2=c2,c3=c3,c4=c4))
            else:
                row_html += u'\r'
                html_file.write(row_html.format(c1=c1, c2=c2))
        r += 1

    html_file.write(u''' </table>''')
