import os
import shutil
import sys
import subprocess

#########################
## EDIT VARIABLES HERE ##
#########################

gitCloneSSH="git@gitlab.com:Kinetic-Solutions/python-test.git"
gitProjectSlug="python-test"

#########################
## BEGINNING OF SCRIPT ##
#########################

startDir = os.getcwd()
user = subprocess.check_output('whoami', shell=True).strip().decode('ascii')
ssh_path = os.path.join(f"/{user}",".ssh")
ssh_key_path = os.path.join(ssh_path,"gitlab_key")

# Create id for SSH key
os.makedirs(os.path.expanduser(ssh_path), exist_ok=True)
with open(os.path.expanduser(ssh_key_path), 'w') as ssh_key:
    ssh_key.write('''-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdz
c2gtcnNhAAAAAwEAAQAAAQEAkOgOk3dXKXa2DjMN2BTDbIr6RYCIE7DFEocmQTx7
AZUwGwdB0d/W9NC9qXc2UIB/1LM1cUa4qNK+Er9Zo4cmV45Nc7/tDoTOxIDRSH+O
eI7UH6+CHIN/etD8n5nbGjg6g3u2ypBZ79uvKD2mjHiIcrM05DLHqkk25NYMOW6T
F8j+nrxVcU1KU5IPZcammw+2bigRt8kiy2fHjypH60wNS17sMW9BbIZ1Tpe17NgS
NAQa5Z43Fr1bdsvA81oq2s07HVzy8+i1/OphR3TP1etzFIAaxUICa4+gzZLXR3vZ
Popi3ivQtvVzVCQA5CkOuABTasXa49bLalaJM+B7msaPtwAAA9CbfQ/Tm30P0wAA
AAdzc2gtcnNhAAABAQCQ6A6Td1cpdrYOMw3YFMNsivpFgIgTsMUShyZBPHsBlTAb
B0HR39b00L2pdzZQgH/UszVxRrio0r4Sv1mjhyZXjk1zv+0OhM7EgNFIf454jtQf
r4Icg3960PyfmdsaODqDe7bKkFnv268oPaaMeIhyszTkMseqSTbk1gw5bpMXyP6e
vFVxTUpTkg9lxqabD7ZuKBG3ySLLZ8ePKkfrTA1LXuwxb0FshnVOl7Xs2BI0BBrl
njcWvVt2y8DzWirazTsdXPLz6LX86mFHdM/V63MUgBrFQgJrj6DNktdHe9k+imLe
K9C29XNUJADkKQ64AFNqxdrj1stqVokz4Huaxo+3AAAAAwEAAQAAAQAGLg9pFJ7g
AtMS2fSOMZyABZFU431qMZDGEIN+JsEsORubG30gIUa+nCRqlM35MvHAtX/i+9wm
Pw6iKAz/n2TwOP5uoFHQ27MhyEikqeP+mkDLtSV8Z9NI/p63g81HWfyM3PrXur5L
L3hR5Ac1WHKhSalIzi2bwpGXwtU0odWeHwDcYhLVtze854BSmyKU+O2P2TCmTUER
MO0pNFWcX6jSI9QTvdGBgseVhYpZl8Lp6HjXFibs2wuOvBTu8inesr7F1kHVeFAy
APzPDp/PwG4bX0qEzBroFhQdH58MBLdVIjXU3FCQa9VQ3yVkt7hQpyDhZjuKJzIF
VAEyZHIEgu/RAAAAgB0CvzxzOoeKRmoO9CfrvfViHlttQf43rbo5ZRF3QMdYTFYo
L5MPjpwU4OUDR+0PjH6z08OL/aMVsoX2ERU8BoJeTAOevFRJYScAC6Tnhrk1rZLI
ldM/UQH/lJpbefk6mJ8nGM90nRQZeMx0CCl3ZHGhZMRz3MFjf9bnTm4GhDa+AAAA
gQDO9ZfK8weuWzjDeYlT5LjayDOGoAJcqRv7G4P6xKn/xFQpaE2bO57BQOYGOMFV
nPt5gOr5dVtXiuPaxqjR280h+NSlz9PlknCjeNsYX0Lli7x0zZak5jRLuzpOHtgf
GGBVb425y70Xh3pAO1HfR4NdpPT+5bhOx3fXohYLbzCJ/wAAAIEAsz5CvxYgeQ/1
KmPolUo2wHdEF13x4UvJtKA1qPP1M1+ZEz4yHPSz8fEykXdC7eWVnSEDqFWjjrQo
xtj3+2bPPIkZDAs/EZm4aFj03OPn2yGA4zwIFWue6LMdQpL/7aM6ubXc4gC1OQV/
3uW9K47ym2ofLRui0lGIo/o9Eu70ykkAAAAQcnNhLWtleS0yMDIzMDQxMwECAwQF
BgcICQoL
-----END OPENSSH PRIVATE KEY-----\n''')
    
# Change file permission
os.system(f'chmod 600 {ssh_key_path}')

# Start SSH agent and add SSH key to agent
os.system(f'eval $(ssh-agent) && ssh-add {ssh_key_path}')

# add host key to known hosts file
hostPath = os.path.join(ssh_path,"hostPath")
print (hostPath)
host = 'gitlab.com,172.65.251.78 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFSMqzJeV9rUzU4kWitGjeR4PWSa29SPqJ1fVkhtj3Hw9xjLVXVYrU9QlYWrOLXBpQ6KWjbjTDTdDkoohFzgbEY=\n'
os.system(f'chmod +r {hostPath}')
with open(hostPath, 'a+') as f:
    if host not in f.read():
        f.write(host)
        data = f.read()
        print ("HOSTS:\n",data)
        print (f"Appended public key to Known_Hosts.")
    elif host in f.read():
        print (f"Known_Hosts already contains public key.")
# Create the git directory if it doesn't exist
if not os.path.exists('git'):
    os.mkdir('git')

# Change directory to /git
os.chdir('git')

# Clone the git repository if it doesn't exist
if not os.path.exists(gitProjectSlug):
    os.system(f"git clone {gitCloneSSH}")

# Change directory to the cloned repository
if os.path.exists(gitProjectSlug):
    os.chdir(gitProjectSlug)

    # Define the main branch as the current branch
    if os.popen('git branch').read().strip() != '* main':
        os.system('git branch -M main')

    # Sync the local repository with the remote if it exists
    os.system('yes | git pull origin main')

# Define the path to our local git project directory
gitPath=os.path.join("git",gitProjectSlug)

os.system('ls')
