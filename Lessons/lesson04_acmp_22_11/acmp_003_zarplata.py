s1, s2, s3 = map(int, input().split())
min_s=0
max_s=0

if s1 < s2:
    min_s = s1      
else:
    min_s = s2 

if s1>s2:
    max_s=s1
else: max_s=s2        

if s3 < min_s:
    min_s = s3      
if s3 > max_s:
    max_s = s3    

print(max_s-min_s)