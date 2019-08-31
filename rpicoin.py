#! /usr/bin/env python
from subprocess import Popen,PIPE,STDOUT
import collections
import os
import sys
import time
import math
import os
from urllib2 import urlopen

SERVER_IP = urlopen('https://api.ipify.org/').read()
NODE_LIST = urlopen('https://pastebin.com/raw/haX0XxCA').read()
BOOTSTRAP_URL = "https://explorer.rpicoin.com/downloads/bootstrap.dat"
WALLET_URL = "https://github.com/rpicoin/rpicore/releases/download/v0.4.1/rpicoin-0.4.1-x86_64-linux-gnu.tar.gz"
MN_DAEMON = "rpicoind"
MN_CLI = "rpicoin-cli"
MN_LFOLDER = ".rpicoin"

DEFAULT_COLOR = "\x1b[0m"
PRIVATE_KEYS = []

def print_info(message):
    BLUE = '\033[94m'
    print(BLUE + "[*] " + str(message) + DEFAULT_COLOR)
    time.sleep(1)

def print_warning(message):
    YELLOW = '\033[93m'
    print(YELLOW + "[*] " + str(message) + DEFAULT_COLOR)
    time.sleep(1)

def print_error(message):
    RED = '\033[91m'
    print(RED + "[*] " + str(message) + DEFAULT_COLOR)
    time.sleep(0.5)

def get_terminal_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return w, h
    
def remove_lines(lines):
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    for l in lines:
        sys.stdout.write(CURSOR_UP_ONE + '\r' + ERASE_LINE)
        sys.stdout.flush()

def run_command(command):
    out = Popen(command, stderr=STDOUT, stdout=PIPE, shell=True)
    lines = []
    
    while True:
        line = out.stdout.readline()
        if (line == ""):
            break
        
        # remove previous lines     
        remove_lines(lines)
        
        w, h = get_terminal_size()
        lines.append(line.strip().encode('string_escape')[:w-3] + "\n")
        if(len(lines) >= 10):
            del lines[0]

        # print lines again
        for l in lines:
            sys.stdout.write('\r')
            sys.stdout.write(l)
        sys.stdout.flush()

    remove_lines(lines) 
    out.wait()


def print_welcome():
    os.system('clear')
    print("                                                     ")
    print(" :::====  :::====  ::: :::===== :::====  ::: :::= ===")
    print(" :::  === :::  === ::: :::      :::  === ::: :::=====")
    print(" =======  =======  === ===      ===  === === ========")
    print(" === ===  ===      === ===      ===  === === === ====")
    print(" ===  === ===      ===  =======  ======  === ===  ===")
    print("")
    print_info("RPICOIN Master Node Installer Script v041")

def update_system():
    print_info("Updating the system...").0
    run_command("apt-get update")
    run_command("apt-get upgrade -y")

def chech_root():
    print_info("Check root privileges")
    user = os.getuid()
    if user != 0:
        print_error("This program requires root privileges.  Run as root user.")
        sys.exit(-1)

def install_wallet():
    print_info("Allocating swap...")
    run_command("fallocate -l 3G /swapfile")
    run_command("chmod 600 /swapfile")
    run_command("mkswap /swapfile")
    run_command("swapon /swapfile")
    f = open('/etc/fstab','r+b')
    line = '/swapfile   none    swap    sw    0   0 \n'
    lines = f.readlines()
    if (lines[-1] != line):
        f.write(line)
        f.close()

    print_info("Installing required build dependencies...")
    run_command("apt-get --assume-yes install git unzip") 

    is_install = True
    if os.path.isfile('/usr/local/bin/rpioind'):
        print_warning('Wallet already installed on the system')
        is_install = False

    if is_install:
        print_info("Downloading the wallet...")
        run_command("wget {} -O /tmp/wallet.zip".format(WALLET_URL ))
        print_info("Installing wallet...")
        run_command("cd /tmp && unzip -u wallet.zip")
        run_command("find /tmp -name {} -exec cp {{}} /usr/local/bin \;".format(MN_DAEMON))
        run_command("find /tmp -name {} -exec cp {{}} /usr/local/bin \;".format(MN_CLI))
        run_command("chmod +x /usr/local/bin/{} /usr/local/bin/{}".format(MN_DAEMON, MN_CLI))

def autostart_masternode(user):
    job = "@reboot /usr/local/bin/rpicoind\n"
    
    p = Popen("crontab -l -u {} 2> /dev/null".format(user), stderr=STDOUT, stdout=PIPE, shell=True)
    p.wait()
    lines = p.stdout.readlines()
    if job not in lines:
        print_info("Cron job doesn't exist yet, adding it to crontab")
        lines.append(job)
        p = Popen('echo "{}" | crontab -u {} -'.format(''.join(lines), user), stderr=STDOUT, stdout=PIPE, shell=True)
        p.wait()

def setup_masternode():
    print_info("Setting up first masternode")
    run_command("useradd --create-home -G sudo mn1")

    print_info("Open your desktop wallet config file (%appdata%/rpicoin/rpicoin.conf) and copy your rpc username and password! If it is not there create one! E.g.:\n\trpcuser=[SomeUserName]\n\trpcpassword=[DifficultAndLongPassword]")
    global rpc_username
    global rpc_password
    rpc_username = raw_input("rpcuser: ")
    rpc_password = raw_input("rpcpassword: ")

    print_info("Open your wallet console (Help => Debug window => Console) and create a new masternode private key: createmasternodekey")
    masternode_priv_key = raw_input("masternodeprivkey: ")
    PRIVATE_KEYS.append(masternode_priv_key)
    
    config = """rpcuser={}
rpcpassword={}
rpcallowip=127.0.0.1
rpcport=18002
port=18001
server=1
listen=1
daemon=1
logtimestamps=1
mnconflock=1
masternode=1
masternodeaddr={}:25992
masternodeprivkey={}
maxconnections=128
{}""".format(rpc_username, rpc_password, SERVER_IP, masternode_priv_key, NODE_LIST)

    print_info("Saving config file...")
    run_command('su - mn1 -c "{}" '.format("mkdir -p /home/mn1/.rpicoin/ && touch /home/mn1/.rpicoin/rpicoin.conf"))
    f = open('/home/mn1/.rpicoin/rpicoin.conf', 'w')
    f.write(config)
    f.close()

    print_info("Downloading bootstrap...")
    run_command("apt-get --assume-yes install megatools")
    filename = "blockchain.rar"
    run_command('su - mn1 -c "{}" '.format("cd && megadl '{}' --path {} 2>/dev/null".format(BOOTSTRAP_URL, filename)))
    
    print_info("Unzipping the file...")
    run_command("apt-get --assume-yes install unrar")
    run_command('su - mn1 -c "{}" '.format("cd && unrar x -o+ {} {}".format(filename, MN_LFOLDER)))

    #run_command('rm /home/mn1/.rpicoin/peers.dat') 
    autostart_masternode('mn1')
    os.system('su - mn1 -c "{}" '.format('rpicoind -daemon'))
    print_warning("Masternode started - running & syncing in the background...")

def porologe():

    mn_base_data = """
Alias: Masternode{}
IP: {}
Private key: {}
Transaction ID: [5k desposit transaction id. 'masternode outputs']
Transaction index: [5k desposit transaction index. 'masternode outputs']
--------------------------------------------------
"""

    mn_data = ""
    for idx, val in enumerate(PRIVATE_KEYS):
        mn_data += mn_base_data.format(idx+1, SERVER_IP + ":" + str(25992 + idx), val)

    imp = """Vs lbh sbhaq gur thvqr naq guvf fpevcg hfrshy pbafvqre gb fhccbeg zr.\n\tFLAK: FAbTfY8Rw7QhLpk5i2Ll1UsKxZbMMzmRlz\n\tOGP: 33PeQClZcpjWSlZGprIZGYWLYE8mOFfaJz\n\tRGU: 0k9n794240o456O8qQ5593n7r8q7NR92s4pn4Q9Q2s\n"""
    print('')
    print_info(
"""Masternodes setup finished!
\tWait until masternode is fully synced. To check the progress login the 
\tmasternode account (su mn1) and run
\tthe 'rpicoin-cli getinfo' to get actual block number. Go to
\thttps://explorer.rpicoin.com/ website to check the latest block number. After the
\tsyncronization is done add your masternode to your desktop (controller) wallet.
Data:""" + mn_data)

    print_warning(imp.decode('rot13').decode('unicode-escape'))

def main():
    print_welcome()
    chech_root()
    update_system()
    install_wallet()
    setup_masternode()
    porologe()

if __name__ == "__main__":
    main()
