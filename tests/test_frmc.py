import unittest
from statistics import median
from frmcalc import FRMCalc


class FRMCalcTest(unittest.TestCase):

    def setUp(self):
        """Set up initial values"""
        self.calculator = FRMCalc()

    def test_annual_donor_growth(self):
        """Test the annual_donor_growth() method"""
        year0 = 500
        year1 = 600
        expected = year1 - year0
        self.assertEqual(expected, self.calculator.annual_donor_growth(year0, year1))

        year0 = 600
        year1 = 570
        expected = 570 - 600
        self.assertEqual(expected, self.calculator.annual_donor_growth(year0, year1))

    def test_annual_donor_growth_bad_data(self):
        """Test that annual_donor_growth() raises TypeError when passed bad data"""
        year0 = "twelve"
        year1= "xxx"
        with self.assertRaises(TypeError):
            self.calculator.annual_donor_growth(year0, year1)

    def test_annual_donor_growth_float_passed(self):
        """Test that annual_donor_growth() handles floats passed instead of ints"""
        year0 = 22.5
        year1= 10
        with self.assertRaisesRegex(TypeError, 'float'):
            self.calculator.annual_donor_growth(year0, year1)

    def test_second_gift_conversation_rate(self):
        """Test the second_gift_conversion_rate method"""
        year0 = 500
        second_gift = 300
        expected = second_gift / year0
        self.assertEqual(expected, self.calculator.second_gift_conversion_rate(year0, second_gift))

        year0 = 600
        second_gift = 200
        expected = second_gift / year0
        self.assertEqual(expected, self.calculator.second_gift_conversion_rate(year0, second_gift))

    def test_second_gift_conversion_rate_bad_data(self):
        """Test that second_gift_covnersion_rate() raises TypeError when passed bad data"""
        year0 = 500
        second_gift = "David"
        with self.assertRaises(TypeError):
            self.calculator.second_gift_conversion_rate(year0, second_gift)

    def test_second_gift_conversion_rate_float_passed(self):
        """Test that second_gift_conversion_rate() handles a float passed as argument"""
        year0 = 600
        second_gift = 200.6
        with self.assertRaisesRegex(TypeError, 'float'):
            self.calculator.second_gift_conversion_rate(year0, second_gift)

    def test_net_cost_per_donor_acquired(self):
        """Test the net_cost_per_donor_acquired method"""
        cost = 50000
        income = 34000
        donors_acquired = 500

        expected = (income - cost) / donors_acquired
        self.assertEqual(expected, self.calculator.net_cost_per_donor_acquired(cost, income, donors_acquired))

    def test_net_cost_per_donor_acquired_bad_data(self):
        """Test that net_cost_per_donor_acquired() raises TypeError when passed bad data"""
        cost = "Jason"
        income = 34000
        donors_acquired = 500

        with self.assertRaises(TypeError):
            self.calculator.net_cost_per_donor_acquired(cost, income, donors_acquired)

    def test_attrition_rate(self):
        """Test the attrition_rate method"""
        year0 = 500
        year1 = 300

        expected = 100 - (year1 / year0)
        self.assertEqual(expected, self.calculator.attrition_rate(year0, year1))

    def test_attrition_rate_bad_data(self):
        """Test attrition_rate method raises TypeError when passed bad data"""
        year0 = "John"
        year1 = 300

        with self.assertRaises(TypeError):
            self.calculator.attrition_rate(year0, year1)

    def test_renewal_rate(self):
        """Test renewal_rate"""
        year0 = 500
        year1 = 300

        expected = year1 / year0
        self.assertEqual(expected, self.calculator.renewal_rate(year0, year1))

    def test_renewal_rate_bad_data(self):
        """Test renewal_rate() raises TypeError when passed bad data"""
        year0 = "One Hundred"
        year1 = 300

        with self.assertRaises(TypeError):
            self.calculator.renewal_rate(year0, year1)

    def test_average_gift(self):
        """Test average_gift method"""
        income = 21786.99
        gifts = 239

        expected = income / gifts
        self.assertEqual(expected, self.calculator.average_gift(income, gifts))

    def test_average_gift_bad_data(self):
        """Test average_gift method  raises TypeError when passed bad data"""
        income = 21786
        gifts = "Tom"

        with self.assertRaises(TypeError):
            self.calculator.average_gift(income, gifts)

    def test_average_gift_float_passed_for_gifts(self):
        """Test average_gift method with a float passed for gift parameter"""
        income = 21786.98
        gifts = 239.5

        with self.assertRaisesRegex(TypeError, 'float'):
            self.calculator.average_gift(income, gifts)

    def test_median_gift(self):
        """Test median_gift method"""
        gifts = [10, 15, 10, 10, 10, 25, 12, 17.50, 100, 1000, 50, 5, 5, 5, 24, 13, 9, 22.50,]

        expected = median(gifts)
        self.assertEqual(expected, self.calculator.median_gift(gifts))

    def test_median_gift_bad_data(self):
        """Test median_gift method with one bad value"""
        gifts = [10, 15, 10, 10, 10, 25, 12, 17.50, "John", 1000, 50, 5, 5, 5, 24, 13, 9, 22.50,]

        with self.assertRaises(TypeError):
            self.calculator.median_gift(gifts)

    def test_cost_to_raise_dollar(self):
        """Test cost_to_raise_dollar method"""
        cost = 50000
        income = 129245.45

        expected = cost / income
        self.assertEqual(expected, self.calculator.cost_to_raise_dollar(cost, income))

    def test_cost_to_raise_dollar_bad_data(self):
        """Test cost_to_raise_dollar method with bad data passed"""
        cost = 50000
        income = "Frank"

        with self.assertRaises(TypeError):
            self.calculator.cost_to_raise_dollar(cost, income)

    def test_net_income(self):
        """Test net_income method"""
        cost = 45989.76
        income = 267787.98

        expected = income - cost
        self.assertEqual(expected, self.calculator.net_income(cost, income))

    def test_return_on_investment(self):
        """Test return_on_investment method"""
        cost = 45989.76
        income = 267787.98

        expected = (income - cost) / cost
        self.assertEqual(expected, self.calculator.return_on_investment(cost, income))

    def test_return_on_investment_bad_data(self):
        """Test return_on_investment method throws TypeError with bad data"""
        cost = "Hospital"
        income = 267787.98

        with self.assertRaises(TypeError):
            self.calculator.return_on_investment(cost, income)

    def test_long_term_value(self):
        """Test long_term_value method"""
        data = [
            {
                "year": 2015,
                "donors": 6856,
                "gifts": 10912,
                "revenue": 3002975,
            },
            {
                "year": 2016,
                "donors": 5000,
                "gifts": 19227,
                "revenue": 4877466,
            },
            {
                "year": 2017,
                "donors": 4000,
                "gifts": 26553,
                "revenue": 7051333,
            }
        ]

        expected = {
            2015: (data[0]["gifts"] / data[0]["donors"])  * (data[0]["revenue"] / data[0]["gifts"]),
            2016: (data[1]["gifts"] / data[1]["donors"])  * (data[1]["revenue"] / data[1]["gifts"]),
            2017: (data[2]["gifts"] / data[2]["donors"])  * (data[2]["revenue"] / data[2]["gifts"]),
        }

        self.assertEqual(expected, self.calculator.long_term_value(data))

    def test_long_term_value_bad_data(self):
        """Test long_term_value method throws TypeError with bad data"""
        data = [
            {
                "donors": "Twelve",
                "gifts": 10912,
                "revenue": 3002975,
            },
            {
                "donors": 5000,
                "gifts": 19227,
                "revenue": 4877466,
            },
            {
                "donors": "Jason",
                "gifts": 26553,
                "revenue": 7051333,
            }
        ]

        with self.assertRaises(TypeError):
            self.calculator.long_term_value(data)


if __name__ == '__main__':
    unittest.main()
