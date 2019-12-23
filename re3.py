import re
print(re.sub(r'\sAND\s', '&', 'Baked Beans And Spam', flags=re.IGNORECASE))
print (re.sub(r'\sOR\s', '/', 'Munna Or Shihab', flags=re.IGNORECASE))
