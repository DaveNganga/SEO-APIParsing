import unittest
from StyleguineaPig import print_factors
from apis import spotipy_client, response_to_accesstoken, track_information


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(print_factors(25), [1])

    def test_function2(self):
        output = spotipy_client()
        self.assertTrue((output is not None), 'Auth. response collected')

    def test_function3(self):
        output_one = spotipy_client()
        output_two = response_to_accesstoken(output_one)
        self.assertTrue((output_two is not None), 'Access Token obtained')
        
    def test_function4(self):
        output_one = spotipy_client()
        output_two = response_to_accesstoken(output_one)
        output_three = track_information(output_two)
        self.assertTrue((output_three is not None), 'Track info collected')

        
if __name__ == '__main__':
    unittest.main()
