import scapy.all as scapy

def sniffing(interface):
    scapy.sniff(iface=interface,store=False,prn=process_packet)

def process_packet(packet):
    # print(packet.show())
    # print(packet.get_field('dst'))
    try:
        # print(packet.show2())
        # print(packet.dst)
        # print(packet.src)
        # print(packet.type)
        # print(packet.nextname)
        # print(packet.payload.layers())
        print(packet.show())
    except:
        pass

sniffing("wlo1")
