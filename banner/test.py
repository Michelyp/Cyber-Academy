import dns
import dns.reversename
domain = dns.reversename.from_address('172.217.14.195')
print(domain)
