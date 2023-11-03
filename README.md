# FTP-brute-force-attack-script

It is a Python script that attempts to perform a brute force attack on an FTP server. The main function of the code is to try different combinations of usernames (`users`) and passwords (`passwords`) to attempt to authenticate to an FTP server located at IP address `0.0.0.0`. The goal is to find valid username and password combinations to access the FTP server without authorization.

Here is the summary of the steps the code performs:

1. **Importing the `ftplib` module:** The code begins by importing the `ftplib` module, which provides functionality for interacting with FTP servers.

2. **Definition of the `attack` function:** The `attack` function is defined that takes three parameters: `ip` (the IP address of the FTP server), `user` (the username) and `password ` (the password). This function attempts to make an FTP connection to the server using the username and password provided. If the authentication is successful, the script prints the username and password that were used for authentication.

3. **Reading users and passwords from files:** The code opens two files, `users.txt` and `passwords.txt`, and reads the lines from these files in the `users` and `passwords` lists respectively . Each line in these files must contain a username or password.

4. **Nested loop to test combinations:** The code uses two nested loops to test all possible combinations of usernames and passwords. For each combination, it invokes the `attack` function to attempt to authenticate to the FTP server.

It is important to note that this type of activity (brute force attacks) is illegal and highly irresponsible if performed without the explicit consent of the owner of the target system. Performing this type of activity without permission can lead to serious legal consequences. Always make sure you have permission before performing security tests on any system or network.

# Server Code

If you need to create an FTP server for educational or development purposes, you can use the pyftpdlib module in Python. pyftpdlib is an FTP server library written in Python that allows you to easily create an FTP server. Here is a basic example of how you can create an FTP server using pyftpdlib:

First, make sure you have pyftpdlib installed. You can install it using pip:

pip install pyftpdlib

Then, you can create an FTP server with the following code:

python

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

Authorizer settings (users and permissions)
authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", "/directory/path", perm="elradfmw") # Permissions: read, write, delete, directory, list, rename, create directories

FTP handler configuration
        
handler = FTPHandler
handler.authorizer = authorizer

FTP server configuration and startup

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()

In this code, replace "user" and "password" with the username and password you want to use to access the FTP server. Also, replace "/directory/path" with the path of the directory you want to be the root directory of the FTP server.

Once you've saved the code to a file, for example ftp_server.py, run it with Python. The FTP server will start and be listening on port 21. You can connect to the server using an FTP client such as FileZilla or the ftp command on the command line and use the credentials you have configured to access and transfer files.

Please note that this is a basic example and you may need to adjust the settings based on your specific needs. Also, be sure to understand the security implications and set up the appropriate credentials and permissions to protect your FTP server.
