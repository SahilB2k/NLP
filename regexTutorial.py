#reger101 <-- website to learn regex easily

import re

# chat1='codebasics:you ask  lot of questions 12345678912, abc@xyz.com'
# chat2='codebasics:here it is : (123)-567-8912, abc@xyz.com'
# chat3='codebasics:yes , phone: 1235678912: abc@xyz.com'
# chat4='abc_56@vxy.com'
# chat5='hello , i have my issue with my order # 42134567'
# chat6='hello , i have my issue with my order number 42134567'
# chat7='My age is 66'
# chat8='hello i was born elon musk and my age 34'


# number=r'\d{10}' #for extracting numbers
# mails=r'[a-z0-9A-Z_]*@[a-z]*\.[a-z]*' #for extracting emails
# order_number=r'order[^\d]*(\d*)' #fr order number
# age=r'age[^\d]*(\d+)'  # Matches 'age' followed by any non-digit chars, then captures digits
# name=r'born(.*)'


# matches=re.findall(name,chat8)
# print(matches)


text='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.
'''

# url=r'http[^\d]*[a-z]*\n'
# urls=re.findall(url,text)
# print(urls)

transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"
money=r'[a-z]*[^\d]'
moneys=re.findall(money,transactions)
print(moneys)



