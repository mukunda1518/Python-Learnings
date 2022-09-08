# Bundling of related properties and actions together is called
# We can achieve encapsulation by Classes

class Mobile:  # Class is a blue print

    def __init__(self, model, camera):    # Properties AS Attributes
        self.model = model
        self.camera = camera


    # Instance method - It contains self as first argument

    def make_call(self, number):  # Actions are methods
        print("Calling....{}".format(number))

    def get_model(self):
        print(self.model)

    def update_model(self, model):
        self.model = model



mobile_obj = Mobile("Galaxy M51", "64 MP")
print(mobile_obj)
mobile_obj.make_call(12345677890)

mobile_obj1 = Mobile("Redmi Note7", "32 MP")
print(type(mobile_obj1))
print(id(mobile_obj))
print(id(mobile_obj1))
print(mobile_obj.model)    # Accessing the attributes

mobile_obj1.get_model()

# it is recommended to update attributes through methods

mobile_obj1.update_model("Galaxy G7")
mobile_obj1.get_model()


