# Enter cipher here:
x = "WFUOOYG"
y = "UCWWPYW"

result11 = ""
result12 = ""
result13 = ""
result14 = ""

def calculate_mod(letter1, letter2, result_letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index1 = alphabet.index(letter1)
    index2 = alphabet.index(letter2)
    index_result = alphabet.index(result_letter)

    diff = (index_result - index1 + index2) % 26
    return alphabet[diff]

# The most common first letters in Croatian
inputs1 = ['S', 'P', 'N', 'D']
# The most common second letters in Croatian
inputs2 = ['A', 'E', 'I', 'O', 'U', 'R']

inputs3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z']
results1 = []
results2 = []
results3 = []

# 1st letter
for i in range(len(inputs1)):
    results = calculate_mod(x[0], y[0], inputs1[i])
    results1.append(results)

# 2nd letter 
for i in range(len(inputs2)):
    results = calculate_mod(x[1], y[1], inputs2[i])
    results2.append(results)

# 3rd letter
for i in range(len(inputs3)):
    results = calculate_mod(x[2], y[2], inputs3[i])
    results3.append(results)

# Possible combinations of the first 3 letters in Croatian
for i in range(4):
    for j in range(6):
        for k in range (22):
            elements_to_check = inputs1[i] + inputs2[j] + inputs3[k] + results1[i] + results2[j] + results3[k]
            if any(element in "QWXY" for element in elements_to_check):  
                continue
            elif (inputs1[i] == inputs2[j] or inputs2[j] == inputs3[k] or results1[i] == results2[j] or results2[j] == results3[k]):
                continue
            else:          
                print(inputs1[i] + inputs2[j] + inputs3[k])
                print(results1[i] + results2[j] + results3[k])
                print()

# Other letters
for j in range (3, len(x)):
    ordinal_suffix = {1: "st", 2: "nd", 3: "rd"}.get(j+1 if 10 <= (j+1) % 100 <= 20 else (j+1) % 10, "th")
    print(f"{j+1}{ordinal_suffix} letter")
    for k in range (22):
        print (inputs3[k] + " & " + calculate_mod(x[j], y[j], inputs3[k]))
    print()

# Check your solution here
solution1 = "PREGLED"
solution2 = ""
for i in range (len(solution1)):
    solution2 += chr(ord(y[i]) - ord(x[i]) + ord(solution1[i]))
print(solution2)

