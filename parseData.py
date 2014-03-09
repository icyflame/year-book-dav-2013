filin = open('data.csv')

allData = []

NAME,STREAM,URL = 1,2,3

for i in filin:

    if i[-1] == '\n' or i[-1] == '\r':

        i = i[:-1]

    gh = i.split(',')

    gh = tuple(gh)

    if not gh[0] == 'Timestamp':

        allData.append(gh)   

filin.close()


##now we have all the data in the list of lists allData

##sort it into three lists that have the three streams:

comp = []
bio = []
comm = []

for i in allData:

    if i[STREAM]=='Computer Science':

        comp.append(i)

    elif i[STREAM] == 'Biology':

        bio.append(i)


    else:

        comm.append(i)
    
##we will create the html file:

fil = open('output.html','w')

fil.write('<!DOCTYPE html>\n\n<html>\n\n<body>\n\n<div style="text-align:center">\
            \n<h1>DAV PUBLIC SCHOOL, NERUL</h1><h2> YEARBOOK</h2>\
            \n<h2>Class of 2013</h2><img src="http://i40.tinypic.com/10yjbpt.jpg"\
            width="200" height="200" alt="Class of 2013"/>\n</div>\
            \n\n<table border="2" bordercolor="black" width="100%" height="100%">\n\n')


for x in range(3):

    if x == 0:

        allData = bio

    if x == 1:

        allData = comm

    if x == 2:

        allData = comp


    ##sort this by the name.

    allData = sorted(allData, key=lambda student:student[NAME])

    ##write to the file.

    for i in allData:

        toBeWritten = '\n\t<tr>\n\t\t<td rowspan="2" width="200">\n\t\t\t<img src="' + i[URL]+'" alt="' + i[NAME] +\
                      '"width="200" height="200"/>\n\t\t</td>\n\t\t<td height="100">\n\t\t\t<h2>' + i[NAME] + \
                      '</h2>\n\t\t</td>\n\t</tr>\n\t<tr>\n\t\t<td>\n\t\t\t<h4>' + i[STREAM] + '</h4>\n\t\t</td>\n\t</tr>\n'

 
        fil.write(toBeWritten)
        
        
fil.write('\n\n</table>\n\n</body>\n\n</html>')

fil.close()

import webbrowser

webbrowser.open('output.html')
