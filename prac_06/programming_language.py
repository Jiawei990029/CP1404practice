"""
programming_language
Estimate: 10 minutes
Actual:   18 minutes
"""

class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name = "", typing = "", reflection = True, year = 0):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self, typing):
        """Determine whether typing is Dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False


