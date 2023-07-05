class Numbers:
    def even():
        a=int(input("Enter starting number"))
        b=int(input("Enter ending number"))
        for i in range(a,b+1):
            if i%2==0:
                print (i,end=" ")
   
    def odd():
        a=int(input("Enter starting number"))
        b=int(input("Enter ending number"))
        for i in range(a,b+1):
            if i%2==1:
                print (i,end=" ")
print("\t\t------EVEN NUMBERS------")
Numbers.even()    
print("\t\t------ODD NUMBERS------")
Numbers.odd()