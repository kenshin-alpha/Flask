import re

pattern = '[abc]'
test_string = 'eyyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	

