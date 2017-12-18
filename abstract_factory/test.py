from abstract_factory import *

os = 'MacOS'
if os == 'MacOS':
    specific_factory = SpecificFactoryMacOS()
else:
    specific_factory = SpecificFactoryWin()

print(specific_factory.create_product_a())
print(specific_factory.create_product_b())
