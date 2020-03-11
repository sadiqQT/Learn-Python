# In this program we are learning if - else condition by using equal operator ==
x = 5
y = 10
try:
    if x == y:
        print(f"1st integer variable {x} has same value as 2nd integer variable {y}")
        print("this line is also a part of if condition block !")
    else:
        print(f"both {x} and {y} variables have different value")
        print("noticed i'm also the part of else condition block !")

except Exception:
    print("Exception error occured")
finally:
    print("Test for condional logic executed successfully!")