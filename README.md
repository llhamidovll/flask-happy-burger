
# HungryBurger app Documentation

## Table of Contents

1. introduction
2. Getting Started
   - prerequisites
   - installation
3. Usage
   - running the Application
   - accessing the Application
4. Features
   - login and registrations
   - Place orders
   - orderHistory
   - payment methods
   - update payment method
5. file structure
6. database Schema 
7. Customization
8. Technologies Used

## Introduction

HungryBurger ist a Flask-bases web application. Users can register, log in, order burgers, examine order history, and manage payment methods on the Flask-based HuppyBurger Website. Users can engage with the application's user-friendly and intuitive UI.

## Getting Started

### Prerequisites

- Python 3.7 or a higher version
- SQLite or another database system 

### Installation

1. Clone the repository:

   git clone https://github.com/llhamidovll/flask-happy-burger/tree/main 

2. Enter the project directory by clicking there:

   cd meal-ordering-website

3. Install required packages:

   pip install -r requirements.txt

## Usage

### Running the Application

To run the flask application, execute the following command:

python app.py


### How to access the application? 

Open a web browser and navigate to `http://localhost:5000` to access the HappyBurger Website.

## Features

### Registration and Login

Clients can register for a new account by putting their unique username and password. When registered, users can log in using login data.

### Placing Orders

The logged-in users can select an item (meal) by clicking on the meal.

### Order History
 
Users can see all the orders; they have put before. The orders would be listed.

### Payment Methods

It allows users to add their payment method through the payment page.

### Updating Payment Method

This allows the user to update his existing method of payment through the update payment page.

## File Structure

- `app.py`: The main Flask application file.
- `database.db`: SQLite database file.
- `requirements.txt`: List of required Python packages.
- `static/`: Directory containing static files (images, CSS, etc.).
- `templates/`: Directory containing HTML templates.

## Database Schema

The app uses SQLite with the following tables:

- `users`: Stores user information.
- `orders`: Stores order history.
- `payments`: Stores user payment methods.

## Customization

You can customize the appearance, styling, and layout of the website by modifying the HTML templates and CSS files in the `templates/` and `static/` directories, respectively.

## Technologies Used

- Python
- Flask
- SQLite
- Bootstrap
- CSS
-HTML

