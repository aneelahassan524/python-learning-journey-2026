def company (levels):
    roles = ["CEO","Manager","Team Lead","Developer"]
    if(levels>=len(roles)):
        return 0
    print(roles[levels])
    company(levels+1)
company(0)    