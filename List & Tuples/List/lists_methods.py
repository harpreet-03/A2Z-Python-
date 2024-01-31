listt = [2,1,3]

# add one element at the wnd
listt.append(4)
print(listt)
# [2,1,3,4]


print('\n')


#sorts in ascending order
listt.sort()
print(listt)
#[1, 2, 3, 4]


print('\n')


#sorts in descending order
listt.sort(reverse=True)
print(listt)
#[4, 3, 2, 1]


print('\n')


#reverse list
listt.reverse() 
print(listt)
#[1,2,3,4]


print('\n')


#insert element at the index
listt.insert(1,5)
print(listt)
#[1, 5, 2, 3, 4]
print('\n')



#removes first occurrence of element
listt.remove(1)
print(listt)

#[5, 2, 3, 4]

print('\n')

#removes ele from ind
idx = 2
listt.pop(idx)
#[5, 2, 4]


print(listt)
