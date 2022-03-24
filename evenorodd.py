import unittest
def check_even_or_Odd(x):
    if x %2==0:
        return "even"
    else:
        return "odd"
class MyEvenorOddApp(unittest.TestCase):
    def test_case_even_or_Odd1(self):
        result=check_even_or_Odd(2)
        self.assertEqual("even",result)

    def test_case_even_or_Odd2(self):
        result=check_even_or_Odd(5)
        self.assertEqual("odd",result)

if __name__=="__main__":
    unittest.main()
