def addMyMsg(fun): 
  
    # Nested function 
    def addWelcome(site_name): 
        return "Welcome to " + fun(site_name) 
  
    # Decorator returns a function 
    return addWelcome 
  
@addMyMsg
def site(site_name): 
    return site_name; 

print(site("kumar")) 
print(site("shyam"))
print(site("ram"))

