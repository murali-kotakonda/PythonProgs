a = False

try:
     while not a:   
        f_n = input("Enter file name")
        i_f = open(f_n, 'r')
except:
        print("Input file not found")
        
        
print("Bye")
