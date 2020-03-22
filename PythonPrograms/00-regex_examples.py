#!/usr/bin/env python3
import re
def check_character_groups(text):
    ''' verifier 2 groupes alphanumerique separes par un ou plusieurs espace'''
  result = re.search(r"\w+(\s)+(\w)+", text)
  return result != None

def check_sentence(text):
    '''standard sentence, meaning that it starts with an uppercase letter,
    followed by at least some lowercase letters or a space, and ends with a period,
    question mark, or exclamation point.'''
  result = re.search(r"^[A-Z]([a-z(\s)])+[(\.)(\?)(\!)]$", text)
  return result != None

def check_time(text):
    '''timestamp'''
  pattern = r"^[0-9]?[0-9][:][0-5][0-9](\s)*(:?AM|am|PM|pm)$"
  result = re.search(pattern, text)
  return result != None

def rearrange_name(name):
    # full words use of: \b....\b
  result = re.search(r"^(\w*), (\w*) (\w\.)*$", name)
  #result = re.search(r"^([\w]*), ([\w \.]*)$", name)
  print(result.groups())
  if result == None:
    return name
  return "{} {} {}".format(result[2], result[3],result[1])

def sub_rearrange(name):
    re.sub(r"^([\w .-]*), ([\w .-]*)$",r"\2 \1","Lovelace, Ada")


print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


name=rearrange_name("Kennedy, John F.")
print(name)
subname = sub_rearrange("Kenny, John F.")
print(subname)


def convert_phone_number(phone):
  result = re.sub(r"(\d{3})-(\d{3})-(\b\d{4}\b)",r"(\1) \2-\3",phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

def transform_record(record):
  new_record = re.sub(r"(\d{3}-)+(\d{3,})",r"+1-\1\2",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

def multi_vowel_words(text):
  pattern = (r"(\w*[aeiou]{3,}\w*)")
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

def transform_record(record):
  new_record = re.sub(r"([\d{3}-]+)",r"+1-\1",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator
