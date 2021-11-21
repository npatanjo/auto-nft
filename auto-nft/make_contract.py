#! /usr/bin/python3

import os

os.system("npm init -y")
os.system("npm install --save-dev hardhat")

print("Please Select: Create an empty hardhat.config.js")
os.system("npx hardhat")

os.system("npm install @openzeppelin/contracts")
os.system("npm install dotenv --save")

os.system("npm install --save-dev @nomiclabs/hardhat-ethers 'ethers@^5.0.0'")

os.system("npx hardhat compile")

os.system("npx hardhat run scripts/deploy.js --network ropsten")



