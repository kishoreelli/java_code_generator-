class SpringBootRestController:
    def generate_controller(self, package_name, class_name, methods):
        controller_class = f"package {package_name}\n\n"
        controller_class += "import org.springframework.web.bind.annotation.RestController\n"
        controller_class += "@RestController\n"
        controller_class += f"public class {class_name} {{\n\n"

        for url, method_name, http_method in methods:
            controller_class += f"    @{http_method}Mapping(\"{url}\")\n"
            controller_class += f"    public ResponseEntity<MyResponse> {method_name}(@RequestBody MyRequest request) {{\n"
            controller_class += "        // Process the request and generate a response\n"
            controller_class += "        MyResponse response = new MyResponse(request.getInput1(), request.getInput2());\n"
            controller_class += "        return ResponseEntity.ok(response);\n"
            controller_class += "    }\n\n"
            controller_class += "}\n"
        return controller_class


# # Test SpringBootRestController Class
# controller = SpringBootRestController()
# package_name = "com.example.controller"
# class_name = "MyController"
#
# methods = [
#     ("/foo", "fooMethod", "Get"),
#     ("/bar", "barMethod", "Post"),
#     ("/baz", "bazMethod", "Put"),
# ]
# generated_class = controller.generate_controller(package_name, class_name, methods)
# print(generated_class)
