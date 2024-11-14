class FootballPlayer:
    def __init__(self, player_data):
        """Initialize player with stats data"""
        self.player_id = player_data.get("player_id")
        self.name = player_data.get("name")
        self.goals = player_data.get("goals")
        self.assists = player_data.get("assists")
        self.appearances = player_data.get("appearances")
        self.age = player_data.get("age")

    def is_valid(self):
        """Validate if the player's stats are valid based on some criteria"""
        if not self.player_id or not self.name:
            return False
        
        if not (0 <= self.goals <= 1000):
            return False
        
        if not (0 <= self.assists <= 1000):
            return False
        
        if not (0 <= self.appearances <= 1000):
            return False
        
        if not (18 <= self.age <= 50):
            return False
        
        return True

    def __str__(self):
        """Return a string representation of the player"""
        return f"{self.name} (ID: {self.player_id}) - Goals: {self.goals}, Assists: {self.assists}, Appearances: {self.appearances}, Age: {self.age}"

    def update_stats(self, goals=None, assists=None, appearances=None, age=None):
        """Update the player's statistics"""
        if goals is not None:
            self.goals = goals
        if assists is not None:
            self.assists = assists
        if appearances is not None:
            self.appearances = appearances
        if age is not None:
            self.age = age

    def to_dict(self):
        """Convert player data to a dictionary for easier manipulation or storage"""
        return {
            "player_id": self.player_id,
            "name": self.name,
            "goals": self.goals,
            "assists": self.assists,
            "appearances": self.appearances,
            "age": self.age
        }