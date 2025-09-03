ss = "sammy shark"
print(ss.upper(),ss.capitalize()) #String Convert  SAMMY SHARK \n Sammy shark
#mys krahs ymmas shark 11 2
print(ss[2:8:2])  # print every other letter starting from third one
print(ss[::-1])  #reverse string
print(len(ss),ss.count('a')) 

#OUTPUT: False False True True False
print(ss.isnumeric(),ss.isupper(),ss.islower(), ss.startswith("sa"),ss.endswith("victor")) 

# join,split,replace

sHappy = "I’m happy-:).I’m sad-:(  I’m happy again-:)"
happyCount= sHappy.count('-:)')
sadCount = sHappy.count('-:(')
#Count sub-string occurance
happyCount = len(sHappy.split("-:)"))  - 1  # ['I’m happy', '.I’m sad-:(  I’m happy again', '']
sadCount= len(sHappy.split("-:(")) - 1  # ['I’m happy-:).I’m sad', '  I’m happy again-:)']


sList = "1 2 5 6 9 10"
sListNew = sList.split()[2:6]   # Convert string to list  ['5', '6']

#Convert string list to int list
sListNewInt = [int(x) for x in sListNew ]


#Remove Certain string
s3="abcaaabcdddaaa"
print(''.join(s3.split('a')))  #bcbcddd
print(s3.replace('a',''))  #bcbcddd


"".join(reversed(ss))  # Reserve string ss
print(",".join(["sharks", "crustaceans", "plankton"]))  #sharks,crustaceans,plankton

year=2017
month=1
day=23
hour=1
mins=4

print("%d-%02d-%02d  %02d:%02d" % (year,month,day,hour,mins))


#https://www.python-course.eu/python3_formatted_output.php



#http://www.cemc.uwaterloo.ca/contests/computing/2011/stage1/seniorEn.pdf  S1 , English or French
#2015 J2/J3, 2014 J2
#http://www.cemc.uwaterloo.ca/contests/computing/2014/stage%201/juniorEn.pdf J2
