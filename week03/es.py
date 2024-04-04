
f = open ('es.txt', 'r')
es = f.read ()
f.close ()

freq = es.count ('e')
print (freq)