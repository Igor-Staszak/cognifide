import sys
file = open(sys.argv[1:], 'r')
content = file.readlines()
text1 = []
text2 = []

for i in range(len(content)):
    if(content[i].__contains__('host')):
        text1.append(content[i].lower())

for j in range(len(text1)):
    for l in range(j+1, len(text1)):
        if text1[j] == text1 [l] and text1[j] not in text2:
            text2.append(text1[j])

print("Reapeated names (in lower case): ", text2)
