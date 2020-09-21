from statistics import median
from typing import List, Set, Dict, Tuple, Optional
from decimal import Decimal


class FRMCalc:
    """FRMCalc class calculates essential funraising metrics."""

    def annual_donor_growth(self, year0: int, year1: int) -> int:
        """Annual donor growth: year1 - year0."""

        # Check that args are proper data types
        if not isinstance(year0, int):
            raise TypeError("Bad argument type: integer expected for argument \"year0\", " + str(type(year0)) + " received.")

        if not isinstance(year1, int):
            raise TypeError("Bad argument type: integer expected for argument \"year1\", " + str(type(year1)) + " received.")

        return year1 - year0

    def second_gift_conversion_rate(self, acquired: int, second_gift: int) -> float:
        """Second gift conversion rate: donors acquired in x year who gave second gift / donors acquired in x year."""

        # Check that args are proper data types
        if not isinstance(acquired, int):
            raise TypeError("Bad argument type: integer expected for argument \"acquired\", " + str(type(acquired)) + " received.")

        if not isinstance(second_gift, int):
            raise TypeError("Bad argument type: integer expected for argument \"second_gift\", " + str(type(second_gift)) + " received.")

        return second_gift / acquired

    def net_cost_per_donor_acquired(self, cost: float, income: float, acquired: int) -> float:
        """Net cost per donor acquired: net income (income - cost) / number of acquired donors."""

        if acquired == 0:
            return None

        # Check that args are proper data types
        if not (isinstance(cost, float) or isinstance(cost, int) or isinstance(cost, Decimal)):
            raise TypeError("Bad argument type: integer or float expected for argument \"cost\", " + str(type(cost)) + " received.")

        if not (isinstance(income, float) or isinstance(income, int) or isinstance(income, Decimal)):
            raise TypeError("Bad argument type: integer or float expected for argument \"income\", " + str(type(income)) + " received.")

        if not isinstance(acquired, int):
            raise TypeError("Bad argument type: integer expected for argument \"acquired\", " + str(type(acquired)) + " received.")

        return Decimal((income - cost) / acquired).quantize(Decimal('0.01'))


    def attrition_rate(self, year0: int, year1: int) -> float:
        """Attrition rate: 1 - (donors in year1 who gave in year0 / donors in year0)."""

        if year0 == 0:
            return None

        # Check that args are proper data types
        if not isinstance(year0, int):
            raise TypeError("Bad argument type: integer expected for argument \"year0\", " + str(type(year0)) + " received.")

        if not isinstance(year1, int):
            raise TypeError("Bad argument type: integer expected for argument \"year1\", " + str(type(year1)) + " received.")

        return 1 - (year1 / year0)

    def renewal_rate(self, year0: int, year1: int) -> float:
        """Renewal rate: donors from year0 who give again in year1."""

        if year0 == 0:
            return None

        # Check that args are proper data types
        if not isinstance(year0, int):
            raise TypeError("Bad argument type: integer expected for argument \"year0\", " + str(type(year0)) + " received.")

        if not isinstance(year1, int):
            raise TypeError("Bad argument type: integer expected for argument \"year1\", " + str(type(year1)) + " received.")

        return year1 / year0

    def average_gift(self, income: float, gifts: int) -> Decimal:
        """Average gift: income / gifts."""

        # Check that args are proper data types
        if not (isinstance(income, int) or isinstance(income, float) or isinstance(income, Decimal)):
            raise TypeError("Bad argument type: integer or float expected for argument \"income\", " + str(type(income)) + " received.")

        if not isinstance(gifts, int):
            raise TypeError("Bad argument type: integer expected for argument \"gifts\", " + str(type(gifts)) + " received.")

        return Decimal(income / gifts).quantize(Decimal('0.01'))

    def median_gift(self, gifts: List[float]) -> Decimal:
        """Median gift: median gift from list of gifts."""
        try:
            return Decimal(median(gifts)).quantize(Decimal('0.01'))
        except TypeError:
            raise

    def cost_to_raise_dollar(self, cost: float, income: float) -> float:
        """Cost to raise a dollar: fundraising cost / income."""

        # Check that args are proper data types
        if not (isinstance(cost, int) or isinstance(cost, float) or isinstance(cost, Decimal)):
            raise TypeError("Bad argument type: integer or float expected for argument \"cost\", " + str(type(cost)) + " received.")

        if not (isinstance(income, int) or isinstance(income, float) or isinstance(income, Decimal)):
            raise TypeError("Bad argument type: integer or float expected for argument \"income\", " + str(type(income)) + " received.")

        return Decimal(cost / income).quantize(Decimal('0.01'))

    def net_income(self, cost: float, income: float) -> float:
        """Net income: income - cost."""

        # Check that args are proper data types
        if not (isinstance(cost, int) or isinstance(cost, float) or isinstance(cost, Decimal)):
            raise TypeError("Bad argument type: integer or float expected for argument \"cost\", " + str(type(cost)) + " received.")

        if not (isinstance(income, int) or isinstance(income, float) or isinstance(income, Decimal)):
            raise TypeError("Bad argument type: integer or float expected for argument \"income\", " + str(type(income)) + " received.")

        return Decimal(income - cost).quantize(Decimal('0.01'))

    def return_on_investment(self, cost: float, income: float) -> float:
        """Return on investment: net income (income - cost) / cost."""

        if cost == 0:
            return None

        # Check that args are proper data types
        if not (isinstance(cost, int) or isinstance(cost, float) or isinstance(cost, Decimal)):
            raise TypeError("Bad argument type: integer or float expected for argument \"cost\", " + str(type(cost)) + " received.")

        if not (isinstance(income, int) or isinstance(income, float) or isinstance(income, Decimal)):
            raise TypeError("Bad argument type: integer or float expected for argument \"income\", " + str(type(income)) + " received.")

        return Decimal((income - cost) / cost).quantize(Decimal('0.01'))

    def long_term_value(self, data: List[Dict]) -> Dict:
        """Long-term value: for each period, the average value of gifts from donors acquired in period0."""
        calculated = {}

        for period in data:
            try:
                value = (Decimal(period["gifts"] / period["donors"]) * (Decimal(period["revenue"]) / Decimal(period["gifts"]))).quantize(Decimal('0.01'))
            except ZeroDivisionError:
                value = None

            calculated[period['year']] = value

        return calculated
