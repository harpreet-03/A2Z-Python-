nums = [1,4,9,16,25,36,49,64,81,100]
x = 81
idx = 0
while(idx < len(nums) ):
  
    if(nums[idx] == x):
        print("element found at index: ", idx)
        break
    else:
        idx += 1