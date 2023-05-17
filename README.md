# MAQCheck
This is a simple script that can be used to remotely authenticate to an LDAP server to check the value of the Machine Account Quota for a given domain.

## Dependencies

'''
pip3 install -r requirements.txt
'''

## Usage

'''
usage: maqcheck.py [-h] --username USERNAME --password PASSWORD --domain DOMAIN

Script to check for the MAQ - Machine Account Quota

options:
  -h, --help            show this help message and exit
  --username USERNAME, -u USERNAME
                        Username
  --password PASSWORD, -p PASSWORD
                        Password
  --domain DOMAIN, -d DOMAIN
                        Domain
'''
