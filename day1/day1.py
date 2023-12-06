def part1():
    inputs = open("input1.txt", "r").read().split("\n")
    sum = 0
    for i in inputs:
        i = ''.join(filter(str.isdigit, i))
        if len(i) == 0:
            continue
        num = str(i[0]) + str(i[-1])
        print(num)
        sum += int(num)
    return sum

alpha = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
def string_to_num(input_s):
    # Using the dictionary, goes through each number and replaces it within the string
    #using two pointers, starting and ending of a word
    p0, p1 = 0, 0
    output = ''
    while p1 < len(input_s):
        #if we stumble across a digit, then starting pointer moves up
        if input_s[p1].isdigit():
            output += input_s[p1]
            p0 = p1+1
        #if the word we are assembling is in the string, then starting pointer moves up
        if input_s[p0:p1+1] in alpha:
            output += str(alpha[input_s[p0:p1+1]])
            p0 = p1
        #
        elif (p1 - p0) > 2:            
            for a, value in alpha.items():
                if a in input_s[p0:p1+1]:
                    output += str(value)
                    p0 = p1
                    break    
        p1 += 1       
    return (output) if output else ''


def part2():
    inputs = open("input2.txt" , "r").read().split("\n")
    sum = 0
    for i in inputs:
        n = string_to_num(i)
        if n == '':
            continue
        sum += int(n[0]+ n[-1])
    return sum
        
# print(string_to_num("onse2three4five"))
print(part2())



# print(part1())