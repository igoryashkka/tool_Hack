import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface" , dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m","--mac" , dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] erorr it is not interface")
    elif not options.new_mac:
        parser.error("[-] erorr it is not mac")
    return options

def change_mac(interface,new_mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether", new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface]).decode('utf-8')
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
       return mac_address_search_result.group(0)
    else:
       print("i could not read MAC address")



options = get_arguments()
currnet_mac = get_current_mac(options.interface)

print("Current MAC " + str(currnet_mac))
change_mac(options.interface,options.new_mac)

currnet_mac = get_current_mac(options.interface)

if currnet_mac == options.new_mac: 
   print("MAC Address was update to " + currnet_mac)
else:
   print("MAC Address did not update ")
   