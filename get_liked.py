import json, pprint, sys

if len(sys.argv) != 2:
    print "python get_liked.py <LAST_LIKED_ID_YOU_WANT_TO_KEEP>"
    exit(0)

pp = pprint.PrettyPrinter(indent=4)

id_list = []

fw = open('write.txt', 'w')
fr = open('read.txt', 'r')

for line in fr:
    #print line
    b = json.loads(line)
    #pp.pprint(b['data'])
    for e in b['data']:
        if str(e['id']) != sys.argv[1]:
            id_list.append(str(e['id']))
            fw.write(str(e['id']) + '\n')
        else:
            print "id_list:"
            pp.pprint(id_list)
            print "-----------------------"
            fw.close()
            fr.close()
            exit(0)
            
        #id_list.append(str(e['id']))
        
print "id_list:"
pp.pprint(id_list)
print "-----------------------"
fw.close()
fr.close()
