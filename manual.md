# Boxing Prediction Challenge User Manual

## Introduction

Welcome to the Boxing Prediction Challenge! This software allows users to showcase their fight foresight by predicting the outcome of upcoming boxing bouts. Admins have the power to add up to 25 fights for prediction, and the results are updated by them. Users can choose a winner and method of victory from options like UD (Unanimous Decision), MD (Majority Decision), SD (Split Decision), KO (Knockout), TKO (Technical Knockout), or Draw. Admins can assign point values to each correct prediction, making it even more exciting and rewarding.

## Installation

To use the Boxing Prediction Challenge, you need to have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

Once you have Python installed, you can install the required dependencies by running the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

This will install the necessary dependencies, including numpy, pandas, and tkinter.

## Usage

To start the Boxing Prediction Challenge, navigate to the project directory in your terminal or command prompt and run the following command:

```
python main.py
```

This will launch the user interface for the Boxing Prediction Challenge.

### Admin Login

If you are an admin, click on the "Admin Login" button. You will be prompted to enter your admin username and password. Once you have entered the credentials, you will have access to the admin menu.

### User Login

If you are a user, click on the "User Login" button. You will be prompted to enter your username and password. Once you have entered the credentials, you will have access to the user menu.

### Admin Menu

The admin menu allows you to perform various tasks related to the Boxing Prediction Challenge. Here are the available options:

1. Add fight: Add a new fight for prediction. You will be prompted to enter the fight ID, fighter 1, and fighter 2.

2. Update fight outcome: Update the outcome of a fight. You will be prompted to enter the fight ID and the outcome (UD, MD, SD, KO, TKO, or DRAW).

3. Assign points: Assign points to a user for a correct prediction. You will be prompted to enter the fight ID, the user's prediction, and the point value.

4. Exit: Exit the admin menu.

### User Menu

The user menu allows you to make predictions and view your score. Here are the available options:

1. Make prediction: Make a prediction for a fight. You will be prompted to enter the fight ID and your prediction (UD, MD, SD, KO, TKO, or DRAW).

2. View score: View your current score based on your predictions.

3. Exit: Exit the user menu.

## Conclusion

Congratulations! You are now ready to use the Boxing Prediction Challenge. Enjoy showcasing your fight foresight and have an adrenaline-packed experience in the world of boxing predictions!