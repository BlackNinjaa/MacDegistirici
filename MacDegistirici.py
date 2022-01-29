import subprocess

interface_address = input("Arayuzu giriniz: ")
mac_address = input("Lutfen yeni Mac Adresini Giriniz: ")


subprocess.call(["ifconfig",interface_address,"down"])
subprocess.call(["ifconfig",interface_address,"hw","ether",mac_address])
subprocess.call(["ifconfig",interface_address,"up"])
print("Yeni Mac Adresiniz : ",mac_address)