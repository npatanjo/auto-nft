# auto-nft
This repository contains a script that will automatically deploy a smart contract for you and (WIP) mint an nft

# Dependencies 
### Mac
- Homebrew - 
  If Homebrew is not installed visit this website: https://brew.sh/ <br />
- nodejs (requires Homebrew) - 
  'brew install nodejs` <br />
- python3 - 
  Your machine most likeley has python3 installed. You can check by typing `python3 --version` into your terminal. If the output is not a version, python is not installed. You can install python3 with `brew install python3` <br />
- git - To install git: `brew install git`

# Pre-Installation
- Create an Alchemy account at https://www.alchemy.com/
- Click on "Create app" and name it something like "myNft"
- Keep this page open; you will need it later
---
- Navigate to your Ether wallet. If you do not have one, make one.
- Find your private Key, You will need this later

# Installation
- Open up a new terminal shell.
- Make sure you are in your home directory, type `cd` and press enter. This will automatically place you in your home directory.
- From your home directory clone this repo with `git clone https://github.com/npatanjo-student/auto-nft.git`
- You will then want to cd into the directory you cloned: `cd auto-nft`
- Next you will want to manualy enter information into the .env file. (We will be entering this information manually for security purposes. You do not want this information to show up on your command line history) 
- First type `cd -al` to confirm the .env file exists.
- Open this file with your favorite text editor ex: vim, nvim, emacs, nano. If you are a beginner, I suggest nano. `nano .env`
- In the "" next to API_URL cp the url from Alchemy --> myNFT app --> view key --> http
- In the "" next to PRIVATE_KEY cp your private key from your ether wallet
- Your .env should look something like this: <br /> 
```
API_URL="<API KEY>"
PRIVATE_KEY="<PRIVATE WALLET KEY>"
```
- Now write this file and quit. (You are almost done!)
- Next we want to make sure you can run the script. Type `chmod a+x make_contract.py`
- Finally we run the script and let the magic happen. type `./make_contract.py`



