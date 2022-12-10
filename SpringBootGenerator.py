import os


class SpringBootGenerator:
    def __init__(self, class_name, package_name):
        self.controller_name = None
        self.class_name = class_name
        self.package_name = package_name

    def generate_class(self):
        class_string = f"package {self.package_name};\n\n"
        class_string += f"import org.springframework.boot.SpringApplication;\n"
        class_string += f"import org.springframework.boot.autoconfigure.SpringBootApplication;\n\n"
        class_string += f"@SpringBootApplication\n"
        class_string += f"public class {self.class_name} {{\n\n"
        class_string += f"  public static void main(String[] args) {{\n"
        class_string += f"    SpringApplication.run({self.class_name}.class, args);\n"
        class_string += f"  }}\n"
        class_string += "}\n"
        return class_string

    def generate_controller(self, controller_name, method_map):
        self.controller_name = controller_name
        controller_string = f"package {self.package_name};\n\n"
        controller_string += f"import org.springframework.web.bind.annotation.RestController;\n"
        controller_string += f"import org.springframework.web.bind.annotation.RequestMapping;\n"
        controller_string += f"import org.springframework.web.bind.annotation.RequestMethod;\n\n"
        controller_string += f"@Controller\n"
        controller_string += f"public class {controller_name} {{\n\n"

        for method_name, http_method in method_map.items():
            controller_string += f"  @RequestMapping(\"/{method_name}\", method = RequestMethod.{http_method})\n"
            controller_string += f"  public String {method_name}() {{\n"
            controller_string += f"    return \"Hello from {method_name}!\";\n"
            controller_string += f"  }}\n\n"

        controller_string += "}\n"
        return controller_string

# test the SpringBootGenerator class
# generator = SpringBootGenerator("MyClass", "com.example.app")
# class_file = generator.generate_class()
# print(class_file)
#
# method_map = {"sayHello": "GET", "sayGoodbye": "POST"}
# controller_file = generator.generate_controller("MyController", method_map)
# print(controller_file)
