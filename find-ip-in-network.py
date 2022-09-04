import subprocess , ipaddress ,getmac

#net_ip = input("Enter a network address (ex: 192.168.0.0/24): ")
net_ip ="192.168.78.0/24"

# Create the network
ip = ipaddress.ip_network(net_ip)
all_hosts = list(ip.hosts())

info = subprocess.STARTUPINFO()
for i in range(10,20):
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    # -n = count of sent packets   -w = delay (ms)
    
    if "Request timed out" in output.decode('utf-8'):
        print("\n"+str(all_hosts[i]), "is Offline")
        print("----------------------------------------")
    else:
        print(str(all_hosts[i]), "is Online ---> ")
        out_put = subprocess.Popen(['arp', '-a', str(all_hosts[i])]).communicate()
        print("Host MAC is :",getmac.get_mac_address())

        print("----------------------------------------")
#------------------------------------------------------

















