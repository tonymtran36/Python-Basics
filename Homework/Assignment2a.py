def palindrome(num, strs):
    list = []
    for i in range(num):
        strs[i] = ''.join([strs[i].lower() for x in strs[i] if strs[i].isalpha()])
        if (strs[i]==strs[i][::-1]):
            list.append("y")
        else:
            list.append("n")
    return list


print("Hello World"[8])

print("thinker"[2:5])

print("hello"[1])

print("Sammy"[2:])

print("Sammy"[::-1])

print(set("Missippi"))

x = "malayalam"
print(x)
print(x[::-1])
print(x == x[::-1])


list = ["Stars", "O, a kak Uwakov lil vo kawu kakao!", "some men interpret nine memos"]
print(palindrome(3, list))
