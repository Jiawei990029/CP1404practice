"""
guitar
Estimate: 10 minutes
Actual:   20 minutes
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, year):
        """Get the age of the guitar."""
        now_year = 2025
        age = now_year - year
        return age

    def is_vintage(self, age):
        """Determine if a guitar is vintage."""
        if age >= 50:
            return True
        else:
            return False