ATM Simulation System (Python + MySQL)

This project is a command-line based ATM Simulation System developed using Python and MySQL. It demonstrates how database connectivity can be integrated with Python to build a simple banking application that performs essential financial operations.

The system allows users to register, log in securely, and manage their bank accounts through a menu-driven interface. During registration, users provide details such as name, mobile number, email, user ID, password, and opening balance. Basic validation is implemented for mobile number format and password confirmation to ensure data accuracy.

Once registered, users can sign in using their credentials. After successful authentication, they gain access to core banking functionalities including depositing money, withdrawing funds, and viewing account details. All transactions are updated in real time within the MySQL database, ensuring persistent data storage.

The application automatically creates the required database and table (if they do not already exist), making it easy to set up and run. It uses the mysql.connector module to establish the database connection and execute SQL queries for data management.

Key Features

User Registration and Login System

Deposit and Withdrawal Operations

Balance Display Functionality

Automatic Database and Table Creation

Persistent Data Storage using MySQL

This project is designed for educational purposes to understand Python-MySQL integration, database handling, and basic banking logic implementation. While it provides core ATM functionalities, it does not include advanced security features such as password hashing or protection against SQL injection.


----------------------------------------
For audio sound and voice translator:
pip install deep translator  gtts playsound==1.2.2










ATM Simulation System built using Python and MySQL. It features user registration, login authentication, deposit, withdrawal, and balance display. Uses a menu-driven interface with real-time database updates. Ideal for learning Python-MySQL integration and basic banking operations.
-----------------------
