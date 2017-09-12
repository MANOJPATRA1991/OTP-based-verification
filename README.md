# OTP-based-verification

## Installation and Test requirements

This project is built and tested on Windows 10 OS.

1. Create a new project folder.
2. Clone the repository to that folder.
3. **cd** into the project folder and run `vagrant up` from command prompt.
4. Once done, run the command `vagrant ssh`.
5. On the vagrant command line, `cd /vagrant`.
6. Install python-pip with `sudo apt-get install python-pip`.
7. Install flask with `sudo pip install flask`.
8. Install postgresql with `sudo apt-get install postgresql postgresql-contrib`
9. Log in as superuser **postgres** with `sudo su - postgres`.
10. Run the command `psql` to get the psql command line.
11. Run the following commands in the psql command line:
    ```
    CREATE DATABASE users;
    CREATE DATABASE mobileusers;
    CREATE USER dbuser;
    ALTER ROLE dbuser WITH PASSWORD 'users';
    GRANT ALL PRIVILEGES ON DATABASE mobileusers TO dbuser;
    GRANT ALL PRIVILEGES ON DATABASE users TO dbuser;
    ```
12. Exit psql command line with Ctrl+Z and `logout`.
13. Be sure that you have logged out by checking the shell. It should display
    `vagrant@vagrant:/vagrant$` instead of `postgres@vagrant:~$`.
14. Install SQLAlchemy with `sudo pip install sqlalchemy`.
15. Install psycopg2 with `sudo pip install psycopg2`.
16. Install twilio with `sudo pip install twilio`.
17. Create your own Twilio account and get the following information:
	1. TWILIO_ACCOUNT_SID
    2. TWILIO_AUTH_TOKEN
    3. TWILIO_NUMBER
    Update config.py with the above information.
18. Install flask_mail with `sudo pip install flask_mail`.
18. Run the program with `python run.py` from within the respective project directories(i.e., OTP-based-verification and Email-Verification-System) separately.