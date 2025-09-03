
s= "AFB+88HC-444"

result = dict()
cord,cord_tmp = '',''
number,number_tmp = '',''
sign = ''
flag = False
for i in s:
    if i.isalpha():
        if flag:
            result[cord] = [sign, number_tmp]
            number_tmp = ''
            flag = False
        print(i,'string')
        cord_tmp += i
    elif i.isdigit():
        flag = True
        print(i,'number')
        number_tmp += i
        # end = True
    elif i == "+" or i=="-":
        sign = i
        cord = cord_tmp
        print(i,'operator')
    else:
        print(i,'other')
result[cord_tmp] = [sign, number_tmp]        
print(result)
