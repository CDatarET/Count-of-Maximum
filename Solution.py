# cook your dish here
cases = int(input())
for c in range(cases):
    l = int(input())
    strInp = input()
    nums = [int(x) for x in strInp.split()]
    
    count = {}
    
    for i in range(l):
        if nums[i] not in count:
            count.update({nums[i]: 1})
        else:
            count.update({nums[i]:count[nums[i]] + 1})
            
    
    sort = dict(sorted(count.items()))
    maxKey = max(sort, key=sort.get)
    
    print(maxKey , count[maxKey])
