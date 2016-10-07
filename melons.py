import random
import cs1graphics as cg
import datetime
"""This file should have our order classes in it."""


class TooManyMelonsError(ValueError):
    """ Value Error"""



class AbstractMelonOrder(object):

    def __init__(self, species, qty, tax, order_type):
        self.species = species
        if qty > 100:
            raise TooManyMelonsError('You have entered %s melons. Do not exceed 100' % (qty))
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type
        self.order_datetime = datetime.datetime.now()

    def get_total(self):
        base_price = self.get_base_price()

        if self.species.lower() == "christmas":
            base_price *= 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        return total


    def mark_shipped(self):
        """Set shipped to true."""
        self.shipped = True

    def get_base_price(self):
        base_price = random.randint(5, 9)
        hour = self.order_datetime.time().hour
        day = self.order_datetime.date().weekday()
        if hour >= 8 and hour < 11 and day < 5:
            base_price += 4

        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, 0.08, 'domestic')

  
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, 0.17, 'international')
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

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, 0, 'government')
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed

icon = cg.Canvas()
icon.setWidth(300)
icon.setHeight(300)
icon.setBackgroundColor("black")
sq_border = cg.Square(280, cg.Point(150, 150))
sq_border.setBorderWidth(5)
sq_border.setBorderColor('white')
icon.add(sq_border)