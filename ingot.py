n=int(input())
dim=input().split()
b=int(dim[0])
w=int(dim[1])

lst=input().split()
lst=[int(i) for i in lst]
print(lst)

def max_area_histogram(histogram): 
	stack = list() 
	max_area = 0 
	index = 0
	while index < len(histogram): 
		if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
			stack.append(index) 
			index += 1
		else: 
			top_of_stack = stack.pop() 
			area = (histogram[top_of_stack] *
				((index - stack[-1] - 1) 
				if stack else index)) 
			max_area = max(max_area, area) 
	while stack: 
		top_of_stack = stack.pop() 
		area = (histogram[top_of_stack] *
			((index - stack[-1] - 1) 
				if stack else index)) 
		max_area = max(max_area, area) 
	return max_area 

area= max_area_histogram(lst) 
print(str((sum(lst)-area)*b*w))
