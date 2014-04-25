import urllib2
import urllib
import re
import sys
from bs4 import BeautifulSoup
import os

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

default_link='http://www.espncricinfo.com'
save_links=[]

try:
	page = urllib.urlopen('http://www.espncricinfo.com/').read()

	soup=BeautifulSoup(page,'html.parser')
	search=soup.find('table',attrs={'id':'international'})


	if search:
		mad=search.findAll('a')
		
		count=1
		for i in mad:
			names=i.findAll('span')
			if len(names)>0:
				x=str(names[0].text)
				y=str(names[2].text)
				Sno=str(count)+':'
				print Sno,
				count+=1
				print x+' VS '+y
				link=default_link+str(i['href'])
				save_links.append(link)
			

except urllib2.HTTPError, e:
	pass
except urllib2.URLError, e:
	pass		
		

if len(save_links)==0:
	print 'No live/recent international match.'

else:
	while(1):
		match_no=input('Enter the match id: ')
		if match_no<=len(save_links) and match_no>0:
			break
		else:
			print 'Enter a correct value between '+str('1')+' and '+str(len(save_links))+' inclusive.'

	while(1):
		time=input('Enter the time interval (in sec.(>10)): ')
		if time>10:
			break
		else:
			print 'Enter a correct value.'

	myurl=save_links[match_no-1]
	path=os.getcwd()
	img_path=str(path)+'/ball.jpg'

	while(1):

		try:
			htmltext=opener.open(myurl).read()
			soup=BeautifulSoup(htmltext)
	
			a=[]
			p=0
			lat = soup.findAll('a')
			for i in lat:
				p+=1
				if p==10:
					m=str(i)
					a=m.split('"')
					break

			score=str(a[5])
			temp="'"+score+"'"
			f_score="notify-send "+temp+' -i '+img_path
			
			os.system(f_score)
			
			sl='sleep '+str(time)
			os.system(sl)	

		except urllib2.HTTPError, e:
			pass
		except urllib2.URLError, e:
			pass			
