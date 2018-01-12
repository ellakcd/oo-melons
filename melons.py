import random
from datetime import date
import datetime


"""Classes for melon orders."""
class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
       self.species = species
       self.qty = qty
       self.shipped = False
       self.order_type = order_type
       self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        """"""

        cur_base = random.randint(5, 10)
        print 'day', date.weekday
        print 'hour', datetime.hour
        # date today required
        if date.weekday() <= 4 and datetime.hour >= 8 and datetime.hour <= 11:
            cur_base += 4


        return cur_base


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order for the government."""

    passed_inspection = False

    def __init__(self, species, qty):
        """Initialize"""
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0)


    def mark_inspection(self, passed):
        self.passed_inspection = passed

