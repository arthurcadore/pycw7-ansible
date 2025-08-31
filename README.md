# Python Comware7 Ansible Library

Python library for integrating **Ansible** with the **CW7** system, enabling automation of inventory and device orchestration.  

## Installation

### Create a new virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install the package

```bash
pip install pycw7-ansible
```

## Usage

### Import Libraries

First of all, import the libraries of comware 7 connection and vlan features.
```python
>>> from pycw7_ansible.comware import COM7
>>> from pycw7_ansible.features.vlan import Vlan
```

### Open Connection

To open a connection, you need to create a dictionary with the device parameters and pass it to the COM7 class, then call the open method, as shown below:

```python
>>> HOST_IP = "10.100.73.119"
>>> USERNAME = "ped"
>>> PASSWORD = "Admin@1234"
>>> PORT = 830
>>> args = dict(host=HOST_IP, username=USERNAME, password=PASSWORD, port=PORT)
>>> device = COM7(**args)
>>> device.open()
<ncclient.manager.Manager object at 0x7c5536f51d60>
```

### Getting Example Configuration

To get the configuration of a feature, you need to create an instance of the feature class and call the get_config method, as shown below:

```python
>>> vlan1 = Vlan(device, "1")
>>> config = vlan1.get_config()
>>> print(config)
{'vlanid': '1', 'name': 'VLAN 0001', 'descr': 'VLAN-1-MANAGEMENT'}
```

