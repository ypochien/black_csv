# coding=UTF-8
# __author__ == ypochien
import csv
import itertools

import HTML


def FTPDTA01():
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
            count += 1
        new_data = list(itertools.zip_longest(csv_data[1:count] , csv_data[count:] , fillvalue=''))
        new_data.insert(0 , csv_data[0])
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
                if row[1] != '' and len(row[1]) > 1:
                    c3 = row[1][0]
                    c4 = row[1][1]
                    row_html += '<td'
                    if '收盤' == c4:
                        row_html += ' align="right"'
                    row_html += '>{c3}</td><td>{c4}</td>\r'
                    html_file.write(row_html.format(c1=c1 , c2=c2 , c3=c3 , c4=c4))
                else:
                    row_html += '\r'
                    html_file.write(row_html.format(c1=c1 , c2=c2))
            r += 1
        html_file.write(''' </table>''')


def FTPDTA03():
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

    with open('data/FTPDTA03.csv' , mode='r' , encoding='cp950' , errors='replace') as csv_file:
        reader = csv.reader(csv_file)
        data013 = list(reader)

    t = HTML.Table(data013[1:])

    with open('out/FTPDTA03.html' , mode='w' , encoding='utf-8' , errors='replace') as html_file:
        html_file.write(HTML_HEADER)
        html_file.write(data013[0][0])
        html_file.write(str(t))


def FTPDTA011_012():
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

    with open('data/FTPDTA011.csv' , mode='r' , encoding='cp950' , errors='replace') as csv_file:
        reader = csv.reader(csv_file)
        data011 = list(reader)
        # data011 = [rec + [' '] for rec in list(reader)]

    with open('data/FTPDTA012.csv' , mode='r' , encoding='cp950' , errors='replace') as csv_file:
        reader = csv.reader(csv_file)
        data012 = list(reader)

    new_data = itertools.zip_longest(data011[1:] , data012[1:] , fillvalue='')
    final_data = []
    for items in new_data:
        row = []
        for item in items:
            row.extend(item)

        final_data.append(row)
    t = HTML.Table(final_data)

    with open('out/FTPDTA011_012.html' , mode='w' , encoding='utf-8' , errors='replace') as html_file:
        html_file.write(HTML_HEADER)
        html_file.write(data011[0][0])
        html_file.write(str(t))


def FTPDTA013():
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

    with open('data/FTPDTA013.csv' , mode='r' , encoding='cp950' , errors='replace') as csv_file:
        reader = csv.reader(csv_file)
        data013 = list(reader)

    t = HTML.Table(data013[1:])

    with open('out/FTPDTA013.html' , mode='w' , encoding='utf-8') as html_file:
        html_file.write(HTML_HEADER)
        html_file.write(data013[0][0])
        html_file.write(str(t))


def FTPDTA014():
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

    with open('data/FTPDTA014.csv' , mode='r' , encoding='cp950' , errors='replace') as csv_file:
        reader = csv.reader(csv_file)
        data014 = list(reader)

    t = HTML.Table(data014[1:])

    with open('out/FTPDTA014.html' , mode='w' , encoding='utf-8') as html_file:
        html_file.write(HTML_HEADER)
        html_file.write(data014[0][0])
        html_file.write(str(t))


def FTPDTA015():
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

    with open('data/FTPDTA015.csv' , mode='r' , encoding='cp950' , errors='replace') as csv_file:
        reader = csv.reader(csv_file)
        data015 = list(reader)

    t = HTML.Table(data015[2:])

    with open('out/FTPDTA015.html' , mode='w' , encoding='utf-8') as html_file:
        html_file.write(HTML_HEADER)
        html_file.write(data015[0][0] + '<BR>\r\n')
        html_file.write(data015[1][0] + '<BR>\r\n')
        html_file.write(str(t))


def main():
    print('Progress 01')
    FTPDTA01()
    print('Progress 03')
    FTPDTA03()
    print('Progress 011_012')
    FTPDTA011_012()
    print('Progress 013')
    FTPDTA013()
    print('Progress 014')
    FTPDTA014()
    print('Progress 015')
    FTPDTA015()
    print('Progress Completed.')


if __name__ == '__main__':
    main()
