list1= list(range(1,9))  # [1, 2, 3, 4, 5, 6, 7, 8]
squares = [1, 4, 9, 16, 25, 36, 49, 64]
squares.sort(reverse=True)

squares.append(9**2)
squares.remove(1)
squares.pop()   #remove last element and return popped element
squares.insert(3,9999)
len(squares)

list2=[[1,2,3,4],[2,3,4,5],3,8]
list2[1][2]

#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#List Comprehension
squares1 = [ x**2 for x in range(1,9)]  # [1, 4, 9, 16, 25, 36, 49, 64]

#split digits into ones/tens/hundreds
input_number = 1234
ones = (input_number%10)
tens = int(str(input_number)[-2])
hundreds = int(str(input_number)[-3])
thousands = int(str(input_number)[-4])


#http://www.cemc.uwaterloo.ca/contests/computing/2011/stage1/seniorEn.pdf J2
# 2016 J1
#http://www.cemc.uwaterloo.ca/contests/computing/2014/stage%201/juniorEn.pdf   J3