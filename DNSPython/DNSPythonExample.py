import dns
import dns.resolver
import dns.query
import dns.zone
import dns.name
import dns, reversename
import sys

if len(sys.argv) != 2:
    print("[-] usage python DNSPythonExample.py <domain_name>")
    sys.exit()
domain = sys.argv[1]
ansA, ansMX, ansNS, ansAAAA = (dns.resolver.query(domain, 'A'),
                               dns.resolver.query(domain, 'MX'),
                               dns.resolver.query(domain, 'NS'),
                               dns.resolver.query(domain, 'AAAA'))
print("email servers")
print("-------------")
print(ansMX.response.to_text())

print("\name nservers")
print("-------------")
print(ansNS.response.to_text())

print("\naddresses IPV4")
print("-------------")
print(ansA.response.to_text())

print("\naddresses IPV6")
print("-------------")
print(ansAAAA.response.to_text())
