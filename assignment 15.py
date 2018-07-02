import re
email="zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"


desired_output=re.findall("[\w+]@ ([a-z,A-Z,0-9]+)\.([A-Z]{2,4}",email)
print(desired_output)