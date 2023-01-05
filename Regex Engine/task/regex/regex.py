# write your code here
import re

pattern, string = input().split("|")
match_or_not = bool(re.search(pattern, string))

print(match_or_not)
