# Example file to test the pycw7_ansible library

from pycw7_ansible.comware import COM7
from pycw7_ansible.features.vlan import Vlan

HOST_IP = "10.100.73.119"
USERNAME = "ped"
PASSWORD = "Admin@1234"
PORT = 830

def main():
    args = dict(
        host=HOST_IP,
        username=USERNAME,
        password=PASSWORD,
        port=PORT
    )

    device = COM7(**args)

    try:
        device.open()
        print("Connection established!")

        vlan1 = Vlan(device, "1")
        config = vlan1.get_config()
        print("VLAN 1 configuration:")
        print(config)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
