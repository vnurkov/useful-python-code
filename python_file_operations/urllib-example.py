import urllib

url_file = urllib.urlopen("https://docs.python.org/2.7/library/urllib.html")
urllib_docs = url_file.read()
url_file.close()

print len(urllib_docs)
print urllib_docs[:80]
print urllib_docs[-80:]