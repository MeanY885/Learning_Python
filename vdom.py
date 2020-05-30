from netmiko import Netmiko
print('Before Connection')
host = input("Enter Firewall IP/Hostname:")
connection = Netmiko(host=(host), port ='22', username='*', password='*', device_type='fortinet')
enter_vdom_config_mode = connection.send_config_set('config global')
edit_vdom = connection.send_config_set('get system vdom-property | grep name:')
print(edit_vdom)