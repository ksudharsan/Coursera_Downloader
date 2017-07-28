from bs4 import BeautifulSoup
import urllib2
import os
import urllib
import subprocess

print("Enter the URL for the required course : ")
url_in=raw_input()
print("Enter the Folder Name where the downloaded videos is to be saved : ")
folder_name=raw_input()

testfile=urllib.FancyURLopener()
path = os.getcwd()
if not os.path.exists(path+"/"+folder_name):
	p=subprocess.Popen("mkdir "+path+"/"+folder_name,shell=True)
content=urllib2.urlopen(url_in).read()
soup=BeautifulSoup(content,"lxml")
data=soup.findAll("ul",{"class":"course-item-list-section-list"})

for section in data:
	
	li=section.findAll("li",{"class":"unviewed"})
	for val in li:
		name=val.find("a").text	
		resources=val.findAll("div",{"class":"course-lecture-item-resource"})
		for items in resources:
			a_tags=items.findAll("a")
			if len(a_tags)==1:
				testfile.retrieve(a_tags[0]['href'],path+"/"+folder_name+"/"+name+".mp4")
				#print a_tags[0]['href']
			else:		
				testfile.retrieve(a_tags[len(a_tags)-1]['href'],path+"/"+folder_name+"/"+name+".mp4")
				testfile.retrieve(a_tags[len(a_tags)-2]['href'],path+"/"+folder_name+"/"+name+".srt")
				#print a_tags[len(a_tags)-1]['href']
				#print a_tags[len(a_tags)-2]['href']
