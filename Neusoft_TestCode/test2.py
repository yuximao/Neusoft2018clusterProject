from scipy.stats import ttest_rel

a = [3,5,4,6,5,5,4,5,3,6,7,8,7,6,7,8,8,9,9,8,7,7,6,7,8]
b = [7,8,6,7,8,9,6,6,7,8,8,7,9,10,9,9,8,8,4,4,5,6,9,8,12]
t,p=ttest_rel(a,b)
print(t)
print(p)