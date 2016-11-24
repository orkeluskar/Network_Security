# TLS MITM Attack using Gratuitous ARP messages

This attack is done using following tools:

1. ssltrip by moxie marlinspike
2. scapy code to send gratuitous arp messages and poison ARP Cache


Gratuitous arp messages help poison ARP cache which makes attacker as man in the middle between server and victim.

After that, the sslstrip is used to listen over communication between victim and server.

If the user uses a server with http page for normal content and https for secure/login credentials.

Then this sslstrip helps to strip down that https secure version of server to http and gives that to the victim.

Result?
It will be used to capture login/credit card credentials of the user.