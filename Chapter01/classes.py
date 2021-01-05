# intro to classes

class router(object):
    def __init__(self, name, interface_number, vendor):
        self.name = name
        self.interface_number = interface_number
        self.vendor = vendor

r1 = router('SF01-R1', 64, 'cisco')
r2 = router('LAX-R2', 32, 'juniper')


print(f'first device: name = {r1.name}, interface_number = {r1.interface_number}, vendor = {r1.vendor}')

print(f'second device: name = {r2.name},\
                      interface_number = {r2.interface_number},\
                      vendor = {r2.vendor}')