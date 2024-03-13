# Q. Given an array of integers and a number N, find the largest N elements in the array.
# Example:
# Input : 12,8,5,4,1,2,9
#         N = 2
# Output:[12,9]

n = 3
first = "8,12,4,5,1,2,9"
li = first.split(",")
li = [int(i) for i in li]
print(li)

for i in range(len(li)):
    if i == n:
        break
    for j in range(i + 1, len(li)):
        if li[i] < li[j]:
            li[i], li[j] = li[j], li[i]

print(li[:n])
