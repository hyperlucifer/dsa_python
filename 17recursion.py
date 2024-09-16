'''
def = function calling itself 



'''
# def add(n):
#     if n==1:
#         return 1
#     else:
#         s=n+add(n-1)
#         return s
# e=add(5)   
# print(e)
# def fac(n):
#     if n==1:
#         return 1
#     else:
#         f=n*fac(n-1)
#         return f
    
# h=fac(5)
# print(h)

def tab(n,r=1):
    if r>10:
        return
    print(f"{n} {r} {n*r}")
    tab(n,r+1)
    
tab(2)
        