class FootballPlayer:
    def __init__(self, player_data):
        """Initialize player with stats data"""
        self.id = player_data.get("id")
        self.name = player_data.get("name")
        self.firstName = player_data.get("firstName")
        self.lastName = player_data.get("lastName")
        self.dateOfBirth = player_data.get("dateOfBirth")
        self.nationality = player_data.get("nationality")
        self.position = player_data.get("position")
        self.shirtNumber = player_data.get("shirtNumber")

   

    def __str__(self):
        """Return a string representation of the player"""
        return f"{self.name} (ID: {self.id}) - firstName: {self.firstName}, lastName: {self.lastName}, dateOfBirth: {self.dateOfBirth}, nationality: {self.nationality}"

    