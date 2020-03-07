try:
    variable1 = "It's just a string! "
    variable2 = "2"
    variable3 = variable1 + variable2
    print(variable3)
except TypeError:
    print("Error occured becasue of Type Casting") 
else:
    print("If no error occured than executes ELSE block") 
finally:
    print("Let's execute following lines IRRESPECTIVE either Runtime Occured or Not")