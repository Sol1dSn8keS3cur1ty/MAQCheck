import ldap3
import argparse

def derive_target_dn(domain):
    dc_list = ['DC=' + dc for dc in domain.split('.')]
    target_dn = ','.join(dc_list)
    return target_dn

def authenticate(username, password, domain):
    target_dn = derive_target_dn(domain)
    user = "{}\\{}".format(domain, username)
    server = ldap3.Server(domain)
    connection = ldap3.Connection(server=server, user=user, password=password, authentication=ldap3.NTLM)
    connection.bind()
    connection.search(target_dn, "(objectClass=*)", attributes=['ms-DS-MachineAccountQuota'])
    print(connection.entries[0])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to check for the MAQ - Machine Account Quota')

    parser.add_argument('--username', '-u', required=True, help='Username')
    parser.add_argument('--password', '-p', required=True, help='Password')
    parser.add_argument('--domain', '-d', required=True, help='Domain')

    args = parser.parse_args()

    authenticate(args.username, args.password, args.domain)
