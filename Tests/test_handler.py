import unittest
import lambda_function
from LambdaCode import lambda_function in the test handler.py
#from LambdaCode import lambda_function as lambdafunc

class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        event={'Country':'USA'}
        result = lambda_function.lambda_handler(event, None)
        #result = lambdafunc.lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello from '+event['Country'], result['body'])
        # event={'Country':'INDIA'}
        # result = lambda_function.lambda_handler(event, None)
        # print(result)
        # self.assertEqual(result['statusCode'], 200)
        # self.assertEqual(result['headers']['Content-Type'], 'application/json')
        # self.assertIn('Hello from '+event['Country'], result['body'])


if __name__ == '__main__':
    unittest.main()




# import unittest
# from cool_function import app as ct
# from hot_function import app as ht
# from snow_function import app as st

# class TestHandlerCase(unittest.TestCase):
#     def test_cooltest(self):
#         result =  ct.lambda_handler('', '')
#         self.assertEqual(result['statusCode'], 200)
#         self.assertEqual(result["body"],'this is cool test')
#         result1 =  ct.code()
#         self.assertEqual(result1, true)
#     def test_hottest(self):
#         result =  ht.lambda_handler('', '')
#         self.assertEqual(result['statusCode'], 200)
#         self.assertEqual(result["body"],'this is hot test')
#     def test_snowtest(self):
#         result =  st.lambda_handler('', '')
#         self.assertEqual(result['statusCode'], 200)
#         self.assertEqual(result["body"],'this is snow test')