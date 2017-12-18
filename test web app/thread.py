import threading
import urllib2

def f():
    response = urllib2.urlopen('http://mail.ru')
    print len(response.read())    

ts = []
for i in xrange(100):
    t = threading.Thread(target=f)
    t.start()
    ts.append(t)
    
for t in ts:
    t.join()
