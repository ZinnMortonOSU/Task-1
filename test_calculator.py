import unittest
import calculator

class TestCaseCalculator(unittest.TestCase):
    def test_Multiply(self):
        #Positive multiplication
        self.assertEqual(calculator.multiply(5,2), 10)
        #Multiplying positive by 0
        self.assertEqual(calculator.multiply(5,0), 0)
        #Multiplyng negative * positive
        self.assertEqual(calculator.multiply(-5,1), -5)
        #Multiplying negative by 0
        self.assertEqual(calculator.multiply(-5,0), 0)
        #Multiplying two negatives
        self.assertEqual(calculator.multiply(-5,-2), 10)
        #Multiplying decimals
        self.assertEqual(calculator.multiply(5.5,3), 16.5)

    def test_Divide(self):
        #Dividing positives
        self.assertEqual(calculator.divide(10,2), 5)
        #0 as numerator
        self.assertEqual(calculator.divide(0,2), 0)
        #Negative numerator
        self.assertEqual(calculator.divide(-10,2), -5)
        #Negative denominator
        self.assertEqual(calculator.divide(10,-2), -5)
        #Two negatives
        self.assertEqual(calculator.divide(-10,-2), 5)
        #Decimal denominator
        self.assertEqual(calculator.divide(10,2.5), 4)
        #Two decimals
        self.assertEqual(calculator.divide(12.5,0.5), 25)
        #Divide by 0
        try:
            calculator.divide(10,0)
        except:
            pass
        else:
            self.fail("Division by 0 test failed")

    def test_Addition(self):
        #Adding two positives
        self.assertEqual(calculator.add(5,2), 7)
        #Adding positive + negative
        self.assertEqual(calculator.add(5,-2), 3)
        #Adding two negatives
        self.assertEqual(calculator.add(-5,-2), -7)
        #Adding positive with 0
        self.assertEqual(calculator.add(5,0), 5)
        #Adding negative with 0
        self.assertEqual(calculator.add(-5,0), -5)
        #Adding postive decimals
        self.assertEqual(calculator.add(5.25,2.5), 7.75)
        #Adding positive decimal + negative
        self.assertEqual(calculator.add(5.5,-2), 3.5)

    def test_Subtraction(self):
        #Subtracting two positives
        self.assertEqual(calculator.subtract(5,2), 3)
        #Subtracting to 0
        self.assertEqual(calculator.subtract(5,5), 0)
        #Subtracting into negatives
        self.assertEqual(calculator.subtract(5,6), -1)
        #Subtracting negative
        self.assertEqual(calculator.subtract(5,-2), 7)
        #Subtracting from negative
        self.assertEqual(calculator.subtract(-5,2), -7)
        #Subtracting two negatives
        self.assertEqual(calculator.subtract(-5,-2), -3)
        #Subtracting decimals
        self.assertEqual(calculator.subtract(5.5,2), 3.5)

if __name__ == '__main__':
    unittest.main(verbosity=2)