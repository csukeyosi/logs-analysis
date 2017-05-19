from log_analysis import *

if __name__ == '__main__':
	print 'What are the most popular three articles of all time?'
	print '----------------------------------------------------------'
	mostPopularArticle()
	print '\nWho are the most popular article authors of all time?'
	print '----------------------------------------------------------'
	mostPopularAuhtor()
	print '\nOn which days did more than 1% of requests lead to errors?'
	print '----------------------------------------------------------'
	daysMoreOnePerErrors()