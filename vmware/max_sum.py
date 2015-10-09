'''
Created on Oct 4, 2015

@author: ljiang
'''
def largeSubarray(list):
    max_val = list[0]
    return_vals = (0, 0)
    for i in xrange(len(list)):
        if list[i] > 0:
            break
        elif list[i] < 0 and list[i] > max_val:
            max_val = list[i]
            return_vals = (i, i)
    else:
        return return_vals
            
    max_sum = 0
    cur_sum = 0
    cur_i = 0
    start_i = 0
    end_i = 0
    for i, val in enumerate(list):
        if cur_sum+val > 0:
            cur_sum += val
        else:
            cur_sum = 0
            cur_i = i+1
        if cur_sum > max_sum:
            start_i = cur_i
            end_i= i
            max_sum = cur_sum
    return (start_i, end_i)

def largeSubarray_2(list):
    current_sum = list[0]
    start_i = 0
    end_i = 0
    max_sum = list[0]
    current_i = 0
    for i, val in enumerate(list[1:]):
        if val == 0:
            end_i = i
            continue
        if current_sum + val > val:
            current_sum += val
        else:
            current_sum = val
            current_i = i
        if max_sum < current_sum:
            max_sum = current_sum
            start_i = current_i
            end_i = i
    if list[0] == 0:
        return start_i, end_i+1
    return start_i+1, end_i+1

print largeSubarray_2([-1,0,0,1])

print largeSubarray([-1,5,-4,-2,6,5,-4,3,-8,9])
print largeSubarray([-3,-2,-1])
print largeSubarray([0,0,0])

print largeSubarray_2([-1,5,-4,-2,6,5,-4,3,-8,9])
print largeSubarray_2([-3,-2,-1])
print largeSubarray_2([-3,-2,-1,5])
print largeSubarray_2([-3,-2,-1, -5])
print largeSubarray_2([0,0,0])
print largeSubarray_2([0,1,2])

