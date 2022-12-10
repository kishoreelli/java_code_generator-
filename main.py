# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from DtoGenerator import DtoGenerator
from Entity import Entity, Field
from FileWriter import FileWriter
from SpringBootGenerator import SpringBootGenerator
from SpringBootRestController import SpringBootRestController


def sbClassControlerEntityGeneroter():
    file = FileWriter("com.jva.est")
    generator = SpringBootGenerator("MySpringBootClass", "com.example.app")
    class_file = generator.generate_class()
    print(class_file)

    method_map = {"sayHello": "GET", "sayGoodbye": "POST"}
    controller_file = generator.generate_controller("MyController", method_map)
    print(controller_file)

    fields = [Field("id", "long"), Field("name", "String")]
    my_entity = Entity("Person", fields)
    print(my_entity.generate_entity_class())
    print(my_entity.generate_repository())

    controller = SpringBootRestController()
    package_name = "com.example.controller"
    class_name = "MyController"
    methods = [
        ("/foo", "fooMethod", "Get"),
        ("/bar", "barMethod", "Post"),
        ("/baz", "bazMethod", "Put"),
    ]
    generated_class = controller.generate_controller(package_name, class_name, methods)
    print("********************************************************************************")
    print(generated_class)
    print("********************************************************************************")

    generateDtos()


def generateDtos():
    class_name = "UserDTO"
    fields = ["id", "name", "email"]

    dto_generator = DtoGenerator()
    dto_class = dto_generator.generate_dto(class_name, fields)
    file = FileWriter("com.jva.est/test")
    file.write_to_file("class_name", dto_class)
    print(dto_class)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sbClassControlerEntityGeneroter()
