A = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for i in range(1, 11):
    for buchstabe in A:
        print('"', end="")
        print(buchstabe+str(i), end="")
        print('"', end=",")
        #print('" "', end=",")
        # print('"', end="")
        # print(buchstabe+str(i), end="")
        # print('"', end=",")

# "A1","A3","A5","A7","A9","J1","J3","J5","F3","G10","B1","B3","B5","B7","B9","C1","C3","C5","C7","C9","D1","D3","D5","E1","F3","F4","G9","G10","H1","I1","I3","I5","J1","J3","J5"
