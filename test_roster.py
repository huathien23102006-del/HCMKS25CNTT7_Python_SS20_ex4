import unittest

from main import calculate_actual_pay



class TestPayroll(unittest.TestCase):


    def test_active_salary(self):

        player = {

            "status": "Active",
            "salary": 5000

        }


        self.assertEqual(

            calculate_actual_pay(player),

            5000

        )



    def test_benched_salary(self):

        player = {

            "status": "Benched",
            "salary": 6000

        }


        self.assertEqual(

            calculate_actual_pay(player),

            3000

        )



if __name__ == "__main__":

    unittest.main()