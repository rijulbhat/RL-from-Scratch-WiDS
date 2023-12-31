action = ["Up", "Down", "Left", "Right"]

def check(i, k):
    if(k < 0 or k > 15):
        return i
    else:
        return k

def truth_val(i):
    if i == 5 or i == 7 or i == 11 or i == 12 or i == 15:
        return True
    return False

for i in range(16):

    if(i == 5 or i == 7 or i == 11 or i == 12):
        print(i , ": {")
        print('\t"Up" : [')
        print("\t\t(", 1, ",", i, ",", 0, ",", True, "),")
        print("\t],")
        print('\t"Down" : [')
        print("\t\t(", 1, ",", i, ",", 0, ",", True, "),")
        print("\t],")
        print('\t"Left" : [')
        print("\t\t(", 1, ",", i, ",", 0, ",", True, "),")
        print("\t],")
        print('\t"Right" : [')
        print("\t\t(", 1, ",", i, ",", 0, ",", True, "),")
        print("\t],")
        print("},")        

    elif i == 15:
        print(i , ": {")
        print('\t"Up" : [')
        print("\t\t(", 1, ",", i, ",", 1, ",", True, "),")
        print("\t],")
        print('\t"Down" : [')
        print("\t\t(", 1, ",", i, ",", 1, ",", True, "),")
        print("\t],")
        print('\t"Left" : [')
        print("\t\t(", 1, ",", i, ",", 1, ",", True, "),")
        print("\t],")
        print('\t"Right" : [')
        print("\t\t(", 1, ",", i, ",", 1, ",", True, "),")
        print("\t],")
        print("}")        


    else:
        print(i , ": {")
        print('\t"Up" : [')
        print("\t\t(", 1/3, ",", check(i, i-4), ",", 0, ",", truth_val(i), "),")
        print("\t\t(", 1/3, ",", check(i, i+1), ",", 0, ",", truth_val(i), "),")
        print("\t\t(", 1/3, ",", check(i, i-1), ",", 0, ",", truth_val(i), "),")
        print("\t],")
        print('\t"Down" : [')
        print("\t\t(", 1/3, ",", check(i, i+4), ",", 0, ",", truth_val(i), "),")
        print("\t\t(", 1/3, ",", check(i, i+1), ",", 0, ",", truth_val(i), "),")
        print("\t\t(", 1/3, ",", check(i, i-1), ",", 0, ",", truth_val(i), "),")
        print("\t],")
        print('\t"Left" : [')
        print("\t\t(", 1/3, ",", check(i, i+4), ",", 0, ",", truth_val(i), "),")
        print("\t\t(", 1/3, ",", check(i, i-4), ",", 0, ",", truth_val(i), "),")
        print("\t\t(", 1/3, ",", check(i, i-1), ",", 0, ",", truth_val(i), "),")
        print("\t],")
        print('\t"Right" : [')
        print("\t\t(", 1/3, ",", check(i, i+4), ",", 0, ",", truth_val(i), "),")
        print("\t\t(", 1/3, ",", check(i, i+1), ",", 0, ",", truth_val(i), "),")
        print("\t\t(", 1/3, ",", check(i, i-4), ",", 0, ",", truth_val(i), "),")
        print("\t]")
        print("},")