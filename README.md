# ![RPICoin](https://www.rpicoin.com/assets/img/logo/rpicoind.png) RPICoin $RPI Guide

**This guide is for deplying a RPICoin Masternode on a Linux VPS**

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
1. Download the [wallet](https://github.com/rpicoin/rpicore/releases) and extract it.
1. Start and Close the wallet. (creates the folder structure)
1. Download [bootstrap.zip](https://explorer.rpicoin.com/bootstrap.zip) bootstrap file.
1. Extract the zip file to `%appdata%/RPICoin/` folder. Override existing files!

1. Start the wallet and wait for the sync. (Might take a few hours depending on the amount of connections, the speed of your server / desktop and internet connection.)
	
## 2. Masternode Setup <a href="https://www.youtube.com/watch?v=-Lt-ifQxS-w" target="_blank"><img src="https://i.imgur.com/SY3eO38.png"></a>

### 2.1 Send the coins to your wallet
1. Open Console (Help => Debug window => Console)
1. Create a new address. `getaccountaddress <Choose any name for your masternode>`
1. Send exactly 10.000.000 (10M) coins to this address. (One transaction, pay attention to the fee)
1. Wait for the conformation.
1. Save the transaction id, index `getmasternodeoutputs`, and generate and save a new masternode private key `createmasternodekey`.
1. You can optionaly encrypt the wallet (Settings => Encypt wallet) for security reasons. Do not forget the password or you lose the coins that you have.
1. Backup `%appdata%/rpicoin/wallet.dat` file. This contains your coins. DO NOT LOSE IT!

### 2.2 VPS setup
1. Register on [vultr](https://www.vultr.com/?ref=).
1. Send some money (10$ is enough for two months) to your account to deploy a server. (1 server cost 5$/mo, you can pay with bitcoin)
1. Deploy a new server.
    - Server Type: Ubuntu 16.04  
    - Server Size: 5$/mo, 1GB memory (This server is capable to run 3 masternodes. One masternode need 300-400Mb memory)

### 2.3 Automatic Masternode Setup
1. Download [putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
1. Start putty and login as root user. (Root password and server ip address is in vultr overview tab)
1. Paste this command and answer the questions:
```
wget https://raw.githubusercontent.com/tuxmd/rpicoin/scripts/synx.py && python synx.py
```

### 2.4 Add masternode on the desktop wallet

1. Open wallet, wait for sync, unlock wallet
1. Go Masternodes tab
1. Click create
	- Set a name: Masternode1
	- Set the VPS ip and the port: [Ip:Port]
	- Set the generated private key: step 2.1.5
	- Click Add and after click Start
	- Wait 1 day to start receiving coins. Check your the masternode address here: [https://explorer.rpicoin.com/](https://explorer.rpicoin.com/)
	- Note: You can't edit the masternodes config in the wallet but you can edit the file. `%appdata%/rpicoin/masternode.conf`.

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
		- [telegram](https://t.me/RPICoin)

	
