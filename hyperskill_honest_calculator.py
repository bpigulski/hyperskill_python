# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
x = 0.0
y = 0.0
z = 1
memory = 0
memory_q = 1
out = 0.0
cont = ''
operation = ''
continue_calc = 1
store = ''
dictionary = ["+", "-", "/", "*"]
print(msg_0)
def is_one_digit (v):
    out_digit = False
    v = float(v)
    if ((v.is_integer() == True) and (float(v) > -10) and (float(v) < 10)):
        out_digit = True
    else:
        out_digit = False
    return out_digit
def check (v1, v2, v3):
    msg = ""
    if ((is_one_digit(v1) and is_one_digit(v2)) == True):
        msg = msg + msg_6
    if (float(v1) == 1 or float(v2) == 1) and v3 == "*":
        msg = msg + msg_7
    if ((float(v1) == 0 or float(v2) == 0) and (v3 == "*" or v3 == "+" or v3 == "-")):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)
while z == 1:
    memory_q = 1
    continue_calc = 1
    calc = input()
    x, operation, y = calc.split(" ")
    if y == 'M':
        y = memory
    if x == 'M':
        x = memory
    check (x, y, operation)
    try:
        x = float(x)
    except Exception:
        print(msg_1)
        print(msg_0)
        calc = input()
        x, operation, y = calc.split(" ")
        if y == 'M':
            y = float(memory)
        if x == 'M':
            x = float(memory)
        memory_q = 0
        continue_calc = 0
    try:
        y = float(y)
    except Exception:
        print(msg_1)
        print(msg_0)
        calc = input()
        x, operation, y = calc.split(" ")
        if y == 'M':
            y = float(memory)
        if x == 'M':
            x = float(memory)
        memory_q = 0
        continue_calc = 0
    try:
        var = dictionary.__contains__(operation)
        if var == True:
            z = 1
        else:
            print(msg_2)
            print(msg_0)
            memory_q = 0
            continue_calc = 0
    except Exception:
        print(msg_2)
        print(msg_0)
        calc = input()
        x, operation, y = calc.split(" ")
    if ((operation == "/") and (float(y) == 0.0)):
        print(msg_3)
        print(msg_0)
        memory_q = 0
        continue_calc = 0
    if ((operation == "/") and (float(y) != 0.0)):
        out = float(x) / float(y)
    elif operation == "+":
        out = float(x) + float(y)
    elif operation == "-":
        out = float(x) - float(y)
    elif operation == "*":
        out = float(x) * float(y)
    while memory_q == 1:
        print(out)
        print(msg_4)
        store = input()
        if store == 'y':
            out_digit = True
            msg_index = 0
            out_digit = is_one_digit(out)
            if out_digit == True:
                out_dig_ctr = 1
                msg_index = 10
                out_dig_ans = ""
                while out_dig_ctr == 1:
                    print(globals()['msg_' + str(msg_index)])
                    out_dig_ans = input()
                    if out_dig_ans == 'y':
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        elif msg_index >= 12:
                            out_dig_ctr = 0
                            memory = float(out)
                    elif out_dig_ans == 'n':
                        out_dig_ctr = 0
                    else:
                        out_dig_ctr = 1
                    memory_q = 0
            elif out_digit == False:
                memory = float(out)
                memory_q = 0
        elif store == 'n':
            memory_q = 0
        else:
            memory_q = 1
    while continue_calc == 1:
        print(msg_5)
        cont = input()
        if cont == 'y':
            continue_calc = 0
            print(msg_0)
            z = 1
        if cont == 'n':
            continue_calc = 0
            z = 0
