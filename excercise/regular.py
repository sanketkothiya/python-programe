import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 87
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map
tax: +91 1234567891
Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +91 (703)-243-9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com Fax
Website: www.northamerica.tata.com
Directions: View map fass
Fax harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# findall, search, split, sub, finditer
# patt = re.compile(r'fass')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'ai{1}|Fax')


# Special Sequences
# patt = re.compile(r'\bFax')
patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')
# patt = re.compile(r'\b91.{10}')
# Task
# Given a string with a lot of indian phone numbers starting from +91

matches = patt.finditer(mystr)
for match in matches:
    print(match)

print()