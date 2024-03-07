from scapy.all import * 
from optparse import OptionParser
def get_user_input():
	my_object=OptionParser()
	my_object.add_option("-i","--ip",dest="Ip_Address",help="""Enter your IP range """,)
	(girilen_deger,gelmeyen)=my_object.parse_args()
	return girilen_deger.Ip_Address
def send_Arp_packet(ip):
	eth=Ether()
	arp=ARP()
	eth.dst="ff:ff:ff:ff:ff:ff"
	arp.pdst=ip
	combind_packet=eth/arp
	ans,unans= srp(combind_packet,timeout=0.5,verbose=False)
	print(f"{'IP ADDRESS':<15}{'MAC ADDRESS':<20}")
	print("=" * 35)
	for send, recv in ans:
	    print(f"{recv.psrc:<15}{recv.src:<20}")


user_input=get_user_input()

if not user_input:
	print("Eter your ip range -h or --help ")
	
else:

	send_Arp_packet(user_imput)