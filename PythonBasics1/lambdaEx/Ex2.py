#lambda arguments : expression
# def procced(p):
#     printWithSuffix(p)
#     x= 10;
#     printWithSuffix(p)
#     y=210;
#     printWithSuffix(p)
#     
# def printWithSuffix(p):
#     print("Mr/Mrs", p)


def procced(p):
    # funtion varibale
     res = lambda input : "Mr/Mrs." + input
     mul = lambda x,y : x*y
     print(res(p))
     x = 10
     print(res(p))
     y = 210
     print(res(p))
     print(mul(8,9))
    
procced("kumar")   
        
