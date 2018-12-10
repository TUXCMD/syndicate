# ![Syndicate](https://raw.githubusercontent.com/u3mur4/syndicate/master/logo.png) Syndicate Guide

**Do not forget step 4. It really means a lot to me. Thanks!**

Use this instruction and the youtube video to install the wallet, fix wallet issues and setup one/multiple masternode(s).
This guide is for the creation of separate Controller Wallet & Masternode.
For Security reasons, THIS IS THE PREFERRED way to run a Masternode. By running your Masternode in this way you are protecting
your coins in your private wallet, and are not required to have your local wallet running after the Masternode has been started successfully.
Your coins will be safe if the masternode server gets hacked.

## Table of Content
* [1. Desktop Wallet Preparation](#1-desktop-wallet-preparation-)
* [2. Masternode Setup](#2-masternode-setup-)
	* [2.1 Send the coins to your wallet](#21-send-the-coins-to-your-wallet)
	* [2.2 VPS setup](#22-vps-setup)
	* [2.3 Automatic Masternode Setup](#23-automatic-masternode-setup)
	* [2.4 Add masternode on the desktop wallet](#24-add-masternode-on-the-desktop-wallet)
* [3. FAQ](#3-faq)
* [4. The last and the most important step](#4-the-last-and-the-most-important-step)

## 1. Desktop Wallet Preparation <a href="https://www.youtube.com/watch?v=CtnJlrl-kU0" target="_blank"><img src="https://i.imgur.com/SY3eO38.png"></a>

### 1.1 Setup the wallet
1. Download the [wallet](https://github.com/SyndicateLtd/SyndicateQt/releases) and extract it.
1. Start and Close the wallet. (creates the folder structure)
1. Download [bootstrap.rar](https://mega.nz/#!5jYHDYJJ!Az4x8AQB6sqVgrS8R3HvR8k66CvJI8k-kzFP8Ua8zts) bootstrap file.
1. Extract the zip file to `%appdata%/Syndicate/` folder. Override existing files!
1. Add the following content to the `%appdata%/Syndicate/Syndicate.conf` file or use [this](https://pastebin.com/raw/haX0XxCA) file that contains a lot of active nodes.

    ```
    addnode=45.63.41.34:25992
    addnode=83.84.150.52:25992
    addnode=159.69.159.234:25992
    addnode=149.202.53.1:25992
    addnode=45.77.178.74:25992
    addnode=172.104.131.234:25992
    addnode=149.28.196.72:25992
    addnode=209.250.236.93:25992
    addnode=45.32.236.18:25992
    addnode=37.157.192.86:25992
    addnode=95.179.167.245:25992
    addnode=66.115.129.149:25992
    addnode=45.76.32.38:25992
    addnode=103.70.30.33:25992
    addnode=207.148.67.196:25992
    addnode=104.238.189.76:25992
    ```

1. Start the wallet and wait for the sync. (30min to 1h depending on the number of the connections)
	
## 2. Masternode Setup <a href="https://www.youtube.com/watch?v=-Lt-ifQxS-w" target="_blank"><img src="https://i.imgur.com/SY3eO38.png"></a>

### 2.1 Send the coins to your wallet
1. Open Console (Help => Debug window => Console)
1. Create a new address. `getnewaddress Masternode1`
1. Send exactly 5000 coins to this address. (One transaction, pay attention to the fee)
1. Wait for the conformation.
1. Save the transaction id, index `masternode outputs`, and generate and save a new masternode private key `masternode genkey`.
1. You can optionaly encrypt the wallet (Settings => Encypt wallet) for security reasons. Do not forget the password or you lose the coins that you have.
1. Backup `%appdata%/Syndicate/wallet.dat` file. This contains your coins. DO NOT LOSE IT!

### 2.2 VPS setup
1. Register on [vultr](https://www.vultr.com/?ref=7205683).
1. Send some money (10$ is enough for two months) to your account to deploy a server. (1 server cost 5$/mo, you can pay with bitcoin)
1. Deploy a new server.
    - Server Type: Ubuntu 16.04  
    - Server Size: 5$/mo, 1GB memory (This server is capable to run 3 masternodes. One masternode need 300-400Mb memory)

### 2.3 Automatic Masternode Setup
1. Download [putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
1. Start putty and login as root user. (Root password and server ip address is in vultr overview tab)
1. Paste this command and answer the questions:
```
wget https://raw.githubusercontent.com/u3mur4/syndicate/master/synx.py && python synx.py
```

### 2.4 Add masternode on the desktop wallet

1. Open wallet, wait for sync, unlock wallet
1. Go Masternodes tab
1. Click create
	- Set a name: Masternode1
	- Set the VPS ip and the port: [Ip:Port]
	- Set the generated private key: step 2.1.5
	- Click Add and after click Start
	- Wait 1 day to start receiving coins. Check your the masternode address here: [http://explorer.synx.online/](http://explorer.synx.online/)
	- Note: You can't edit the masternodes config in the wallet but you can edit the file. `%appdata%/Syndicate/masternode.conf`.

## 3. FAQ

1. What if I restart the server?
	- The script setup a cron job so the masternode automaticly starts every time when the vps turns on.
1. How to get masternode profit?
	- Enable coin controll feature (Settings => Options => Display => Display coin controll feature)
	- Go send tab
	- Select from the input button only the 5 coin lines
	- Click OK
	- You can send selected amount to an address.
	- Note: DO NOT EVER Transfer synx from that original 5k deposit or you'll break your Masternode.
1. What is the password for the mn1 account?
	- There is no default password. When you create a user it does not have a password yet, so you cannot login with that username until you create a password. There is one other way to act as a new user without its password. As root type `su - mn1`
	- You need to set a password for the user. Use the passwd command: `passwd mn1`
1. I get the following error: "Could not allocate vin"
	- Make sure your wallet fully synced and UNLOCKED.
1. How many masternodes can I run using one IP/server?
	- One masternode per ip.
1. My wallet says my masternodes are not running.
	- The wallet will tell you its not running sometimes when it is. If you still receving the masternode rewards then everything is fine.
1. I got stuck. Can you help me?
	- Try to get help from the cummunity
		- [telegram](https://t.me/syndicateLTD )

## 4. The last and the most important step

**Send a small amount of coin if you found this instruction (yt video and setup script) helpful.**

| Coin | Address  |
| -----| ---------|
| SYNX | SNoGsL8Ej7DuYcx5v2Yy1HfXkMoZZmzEym  |
| BTC  | 33CrDPyMpcwJFyMTceVMTLJYLR8zBSsnWm  |
| ETH  | 0x9a794240b456B8dD5593a7e8d7AE92f4ca4D9D2f |

	
