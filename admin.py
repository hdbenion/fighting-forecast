'''
Admin class to handle the administration tasks.
'''
from fight import Fight
from constants import FIGHT_OUTCOMES
class Admin:
    def __init__(self):
        self.fights = []
    def add_fight(self, fight_id, fighter1, fighter2):
        fight = Fight(fight_id, fighter1, fighter2)
        self.fights.append(fight)
    def update_outcome(self, fight_id, outcome):
        for fight in self.fights:
            if fight.fight_id == fight_id:
                fight.set_outcome(outcome)
                break
        else:
            print("Fight not found!")
    def assign_points(self, fight_id, prediction, point_value):
        for fight in self.fights:
            if fight.fight_id == fight_id:
                if fight.get_outcome() == prediction:
                    # Assign points to the user who made the correct prediction
                    # Implement the logic to assign points
                    break
        else:
            print("Fight not found!")
    def validate_credentials(self, username, password):
        # Implement the logic to validate admin credentials
        # Return True if the credentials are valid, False otherwise
        return True  # Placeholder, replace with actual implementation
class AdminMenu:
    def __init__(self, admin):
        self.admin = admin
    def show_menu(self):
        # Implement the admin menu functionality
        print("Admin menu")
        while True:
            print("1. Add fight")
            print("2. Update fight outcome")
            print("3. Assign points")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_fight()
            elif choice == "2":
                self.update_outcome()
            elif choice == "3":
                self.assign_points()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
    def add_fight(self):
        fight_id = input("Enter fight ID: ")
        fighter1 = input("Enter fighter 1: ")
        fighter2 = input("Enter fighter 2: ")
        self.admin.add_fight(fight_id, fighter1, fighter2)
        print("Fight added successfully!")
    def update_outcome(self):
        fight_id = input("Enter fight ID: ")
        outcome = input("Enter outcome (UD, MD, SD, KO, TKO, DRAW): ")
        if outcome not in FIGHT_OUTCOMES:
            print("Invalid outcome. Please try again.")
            return
        self.admin.update_outcome(fight_id, outcome)
        print("Outcome updated successfully!")
    def assign_points(self):
        fight_id = input("Enter fight ID: ")
        prediction = input("Enter prediction (UD, MD, SD, KO, TKO, DRAW): ")
        point_value = input("Enter point value: ")
        if prediction not in FIGHT_OUTCOMES:
            print("Invalid prediction. Please try again.")
            return
        self.admin.assign_points(fight_id, prediction, point_value)
        print("Points assigned successfully!")