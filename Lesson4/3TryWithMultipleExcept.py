try:
    variable1 = "It's just a string"
    variable2 = 2
    variable3 = variable1 + variable2
    print(variable3)
except TypeError:
    print("Error occured becasue of Type Casting")    
except Exception:
    print("Exception error occured")
except :
    print("default error occured")        