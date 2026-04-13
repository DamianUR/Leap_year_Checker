print("Enter a year below:")
x=int(input())
if x%100==0 and x%400==0:
	print(x,'is a leap year')
if x%100!=0 and x%4==0:
	print(x,'is a leap year')
else:
	print(x,'is not a leap year')

# @authur: Udoriwlela Ratshikhopha