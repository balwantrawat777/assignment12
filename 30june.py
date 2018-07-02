nameage='''Abc is 18 years old
Xyz is 20 years old'''

import re
#names=re.findall('[A-Z][a-z]*',nameage)
#print(names)

import re
#nameage="Abc is 18 years old"
ages=re.findall('[\d]{1,2}',nameage)
print(ages)

#import re
#emailid="balwantrawat333@gmail.com  acd.com  rawat333@gmail.com"
#em=re.findall("[\w._$+-=]{1,20}[@][\w]{1,20}[.][\w]{1,3}",emailid)
#print(em)

#import re
#abc= 'hat mat cat rat'
#regex=re.compile("[m]at")
#strr=regex.sub("xyz",abc)
#print(strr)
