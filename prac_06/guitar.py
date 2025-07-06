"""
guitar
Estimate: 10 minutes
Actual:   30 minutes
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self, year):
        """Get the age of the guitar"""
        now_year = 2025
        age = now_year - year
        return age