class Band:

    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):
        members_str = ", ".join(f"{member.name} ({member.instruments})" for member in self.members)
        return f"{self.name} ({members_str})"

    def add(self, musician):
        self.members.append(musician)

    def play(self):
        result = []
        for member in self.members:
            result.append(member.play())
        return "\n".join(result)