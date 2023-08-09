class Fraction:

    def __init__(self,numerator,denominator):
        if denominator==0:
            raise ValueError("Denominator can't be equal zero.Please,try again.")
        self.numerator=numerator
        self.denominator=denominator


    def __add__(self,other): #addition
        if other==None or not isinstance(other,Fraction):
            raise TypeError("Unexpected type")
        
        common_denominator=self.denominator*other.denominator
        common_numerator=(self.denominator*other.numerator)+ (other.denominator*self.numerator)
        return Fraction(common_numerator,common_denominator)

    def __sub__(self,other):#subtraction
        if other==None or not isinstance(other,Fraction):
            raise TypeError("Unexpected type")
        common_denominator=self.denominator*other.denominator
        common_numerator=(self.denominator*other.numerator) - (other.denominator*self.numerator)
        return Fraction(common_numerator,common_denominator)
    
    def __mul__(self,other):#multiplying
        if other==None or not isinstance(other,Fraction):
            raise TypeError("Unexpected type")
        
        common_denominator=self.denominator * other.denominator
        common_numerator=self.numerator * other.numerator
        return Fraction(common_numerator,common_denominator)
    
    def __truediv__(self,other):
        if other==None or not isinstance(other,Fraction):
            if other.denominator==0:
                raise ZeroDivisionError("You can't divide by 0")
            raise TypeError("Unexpected type")
        
        common_denominator=self.denominator*other.numerator
        common_numerator=self.numerator*other.denominator
        return Fraction(common_numerator,common_denominator)
        

        



    def __eq__(self,other):# equals
        if other==None or not isinstance(other,Fraction):
            return False
        return self.numerator/self.denominator==other.numerator/other.denominator
    
    
    def __ne__(self,other):#not equals
        return not self.__eq__(other)
    
    
    def __lt__(self,other):#less than 
        if other==None or not isinstance(other,Fraction):
            raise TypeError("Expected Fraction .")
        else:
            return self.numerator/self.denominator < other.numerator/other.denominator
        
    def __gt__(self,other):#greater than 
        if other==None or not isinstance(other,Fraction):
            raise TypeError("Expected Fraction .")
        else:
            return self.numerator/self.denominator > other.numerator/other.denominator 
        
     #or
    
    # def __gt__(self,other):
    #     return not self.__lt__(other) 

    
    def __le__(self,other):#less than or equals
        if other==None or not isinstance(other,Fraction):
            raise TypeError("Expected Fraction .")
        else:
            return self.numerator/self.denominator <= other.numerator/other.denominator
        
    #or

    # def __le__(self,other):
    #     return self.__lt__(other) or self.__eq__(other)
        
    def __ge__(self,other):# greater than or equals
        if other==None or not isinstance(other,Fraction):
            raise TypeError("Expected Fraction .")
        else:
            return self.numerator/self.denominator >= other.numerator/other.denominator
        
     #or
    
    # def __ge__(self,other):
    #     return not self.__le__(other) 

if __name__=='__main__':
    fraction_1=Fraction(1,2)
    fraction_2=Fraction(1,4)

    result=fraction_1==fraction_2
    print(result)

    result_2=fraction_1>=fraction_2
    print(result_2)

    result_3=fraction_1 + fraction_2 == Fraction(3, 4)
    print(result_3)