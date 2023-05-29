#!/bin/env/python3.11
"""
    @module app.py
    @date 20230529
    @description checks for a three-digit integer and its armstrong number status.
"""
class ArmstrongNumber:
    def __init__( self ):
        self.currentNumber = None
        self.numberAsString = str()
    def context( self ):
        print( "an Armstrong number is an integer of three digits." )
        print( "the sum of cubes of the digits must equal the original integer." )
    def getNumber( self ): 
        return self.currentNumber
    def getNumberAsString( self ):
        return self.numberAsString
    def setNumberAsString( self, number ):
        self.numberAsString = str( number )
    def setNumber( self, number ): 
        self.currentNumber = number
    def inputNumber( self ):
        try:
            inputtingNumber = True
            while inputtingNumber:
                number = int( input ( "> enter the number to be checked: " ) )
                threeDigits = ( number >= 100 and number <= 999 )
                if not threeDigits:
                    print( "please enter an integer that is three digits" )
                else:
                    print( "valid integer to check." )
                    inputtingNumbers = False
                    self.setNumber( number )
                    break
        except Exception:
            print( "an exception has occured." )
    def convertNumberToString( self, aNumber ):
        numberAsString = str( aNumber )
        self.setNumberAsString( numberAsString )
    def compare( self, yourNumber, numberString ):
        print( f"checking if { yourNumber } is an armstrong number.." )
        temp = 0
        for numString in numberString:
            print( f"{ numString } ** 3 = { int( numString )  ** 3 }" )
            number = int( numString )
            temp += number**3
        print( f"\t\t{ temp }" )
        if yourNumber == temp:
            print( f"{ yourNumber } is an armstrong number!" )
        else:
            print( f"{ yourNumber } is not an armstrong number." )

if __name__ == "__main__":
    armstrong = ArmstrongNumber()
    armstrong.inputNumber()
    armstrong.convertNumberToString( armstrong.getNumber() )
    armstrong.compare( armstrong.getNumber(), armstrong.getNumberAsString() )
