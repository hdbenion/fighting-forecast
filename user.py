'''
User class to handle user predictions and scoring.
'''
from fight import Fight
class User:
    def __init__(self):
        self.predictions = []
    def make_prediction(self, fight_id, prediction):
        self.predictions.append((fight_id, prediction))
    def get_predictions(self):
        return self.predictions
    def calculate_score(self, fights):
        score = 0
        for prediction in self.predictions:
            fight_id, user_prediction = prediction
            for fight in fights:
                if fight.fight_id == fight_id:
                    if fight.get_outcome() == user_prediction:
                        # Increment the score based on the point value assigned to the correct prediction
                        # Implement the logic to calculate the score
                        break
            else:
                print("Fight not found!")
        return score
    def validate_credentials(self, username, password):
        # Implement the logic to validate user credentials
        # Return True if the credentials are valid, False otherwise
        return True  # Placeholder, replace with actual implementation
class UserMenu:
    def __init__(self, user):
        self.user = user
    def show_menu(self):
        # Implement the user menu functionality
        print("User menu")