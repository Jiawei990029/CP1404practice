"""
project
Estimate: 30 minutes
Actual:   20 minutes
"""
from datetime import datetime

class Project:

    def __init__(self, name="", date="", priority=0, cost=0.0, percentage=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __str__(self):
        return f"{self.name}, start: {self.date}, priority {self.priority}, estimate: ${self.cost:.2f}, completion: {self.percentage}%"

    def __repr__(self):
        return f"{self.name}, start: {self.date}, priority {self.priority}, estimate: ${self.cost:.2f}, completion: {self.percentage}%"

    def __lt__(self, other):
        return self.percentage < other.percentage

    @property
    def compare_data(self):
        return datetime.strptime(self.date, "%d/%m/%Y")
