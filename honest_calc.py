# write your code here
msg_0 = 'Enter an equation'
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

msg_lst = ["Are you sure? It is only one digit! (y / n)", "Don't be silly! It's just one number! Add to the memory? (y / n)", "Last chance! Do you really want to embarrass yourself? (y / n)"]

result = 0
memory = 0
msg_index = 0

def is_one_digit(number):
    if float(number).is_integer() == True and (float(number) > -10) and (float(number) < 10):
        output = True
    else:
        output = False
    return output

def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) == True and is_one_digit(v2) == True:
        msg = msg + msg_6
    if (float(v1) == 1.0 or float(v2) == 1.0) and (v3 == '*'):
        msg = msg + msg_7
    if (float(v1) == 0.0 or float(v2) == 0.0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
    print(msg)
        

while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
        
    try:
        float(x)    
    except ValueError:
        print(msg_1)
    else: 
        try:
            float(y)   
        except ValueError:
            print(msg_1)
        else:        
            if (oper != '+') and (oper != '-') and (oper != '/') and (oper != '*'):
                print(msg_2)
            else:
                check(x, y, oper) 
                if oper == '+':
                    result = float(x) + float(y)
                    print(result)
                if oper == '-':
                    result = float(x) - float(y)
                    print(result)
                if oper == '*':
                    result = float(x) * float(y)
                    print(result)
                if (oper == '/') and (y != '0') and (y != 0):
                    result = float(x) / float(y)
                    print(result)
                elif (oper == '/') and (y == '0' or y == 0):
                    print(msg_3)
                    continue
               
                print(msg_4)
                answer = input()
                if answer == 'y':
                    if is_one_digit(result) == True:
                        msg_index = 0
                        while msg_index <= 2:
                            print(msg_lst[msg_index])
                            answer = input()
                            if answer == 'y':
                                msg_index += 1
                            elif answer == 'n':
                                break
                            else:
                                continue
                        if msg_index > 2:
                            memory = result
                    else:
                        memory = result
                      
                    print(msg_5)
                    answer = input()
                    if answer == 'y':
                        continue
                    elif answer == 'n':
                        break
                    else:
                        print(msg_5)
                
                elif answer == 'n':
                    print(msg_5)
                    answer = input()
                    if answer == 'y':
                        continue
                    elif answer == 'n':
                        break
                    else:
                        print(msg_5)
                else:
                    print(msg_4)
