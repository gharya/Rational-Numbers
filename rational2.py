# -*- coding: utf-8 -*-
"""
Defining a Rational number class

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: YOUR NAME HERE
"""
__version__ = 1

class Rational:
    
    '''
    Initialize a new Rational object with value iNum/iDen stored in hidden __numerator and
    __denominator variables.  Calls the reduce() method to put the fraction in lowest terms.
    '''
    def __init__(self, iNum, iDen):
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()
        
    def getNumerator(self):
        return self.__numerator
    
    def getDenominator(self):
        return self.__denominator
    
    def setNumerator(self, n):
        self.__numerator = n
        
    def setDenominator(self, d):
        self.__denominator = d
        
    def isValid(self):
        return self.__denominator != 0
    
    def add(self, num2):
        numerator2 = num2.getNumerator()
        denominator2 = num2.getDenominator()
        GCD = self.gcd(self.__denominator, denominator2)
        LCM = (self.__denominator * denominator2) / GCD
        newNum = ((self.__numerator / self.__denominator) * LCM) + ((num2.getNumerator() / num2.getDenominator()) * LCM)
        newDenom = LCM
        r = Rational(newNum, newDenom)
        r.reduce()
        return r
    
    def sub(self, num2):
        numerator2 = num2.getNumerator()
        denominator2 = num2.getDenominator()
        GCD = self.gcd(self.__denominator, denominator2)
        LCM = (self.__denominator * denominator2) / GCD
        newNum = ((self.__numerator / self.__denominator) * LCM) - ((num2.getNumerator() / num2.getDenominator()) * LCM)
        newDenom = LCM
        r = Rational(newNum, newDenom)
        r.reduce()
        return r
    def mult(self, num2):
        newNum = ((self.__numerator / self.__denominator) * LCM) - ((num2.getNumerator() / num2.getDenominator()) * LCM)
        newDenom = LCM
        r = Rational(newNum, newDenom)
        r.reduce()
        return r
    
    def div(self, num2):
        newNum = ((self.__numerator / self.__denominator) * LCM) - ((num2.getNumerator() / num2.getDenominator()) * LCM)
        newDenom = LCM
        r = Rational(newNum, newDenom)
        r.reduce()
        return r
    
    
    
    ################################
    #    HELPER FUNCTIONS BELOW    #
    ################################
    '''
    Reduces the Rational to lowest terms
      - Checks if both the numerator and denominator are negative; if so, makes both positive
      - Calls gcf() to find the greatest common factor between the numerator and denominator, and
        continues to divide by that gcf until the greatest common factor is 1
    '''
    def reduce(self):
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while (common != 1):
            common = self.gcf()
            self.__numerator /= common
            self.__denominator /= common
    
    '''
    Determines the greatest common factor between the numerator and denominator
      - Starts checking numbers counting downward from the smaller of the numerator,denominator pair
      - When it finds a number divisble by both, it breaks the loop and returns that number
      - The smallest number that can be returned is 1
    '''
    def gcf(self):
        common_factor = 1
        for i in range(min(abs(int(self.__numerator)), abs(int(self.__denominator))), 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                 common_factor = i
                 break
        return common_factor
    
    def gcd(self, num1, num2):
        common_factor = 1
        for i in range(min(abs(int(num1)), abs(int(num2))), 1, -1):
            if num1 % i == 0 and num2 % i == 0:
                common_factor = i
                break
            return common_factor
    '''
    Returns a string representation of the Rational, e.g. "1/8"
    '''
    def __str__(self):
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))
    
    '''
    Determines if two Rationals are exactly equal to each other (same numerator and same
    denominator, no consideration of reducing the numbers)
    '''
    def __eq__(self, r2):
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator
    
    ################################
    #     END HELPER FUNCTIONS     #
    ################################    
    
    
    
    
    
    
def main():
    print("Passed Test 1." if test1() else "Failed Test 1.")
    print("Passed Test 2." if test1() else "Failed Test 2.")
    print("Passed Test 3." if test1() else "Failed Test 3.")
    print("Passed Test 4." if test1() else "Failed Test 4.")
    print("Passed Test 5." if test1() else "Failed Test 5.")
    print("Passed Test 6." if test1() else "Failed Test 6.")

###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for getNumerator()
def test1():
    r = Rational(12, 15)
    return r.getNumerator() == 4

def test2():
    r = Rational(12, 15)
    return r.getDenominator() == 5

def testN():
    r1 = Rational(12, 15)
    r2 = Rational(13, 20)
    r = r1.add(r2)
    return r.getNumerator() == 29 and r.getDenominator() == 20


    
###############################################################    
    
if __name__ == "__main__":
    main()    