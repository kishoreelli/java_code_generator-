# put the code in a file named "dto_generator.py"

class DtoGenerator:
    def generate_dto(self,class_name, fields):
        # add the import for the @JsonProperty annotation
        dto_class = "import com.fasterxml.jackson.annotation.JsonProperty;\n\n"

        # generate the class header
        dto_class += "public class {} {{\n".format(class_name)

        # generate the fields
        for field in fields:
            dto_class += "    private String {};\n".format(field)

        # generate the getters and setters
        for field in fields:
            # generate the setter
            dto_class += "    public void set{}(String {}) {{\n".format(field.capitalize(), field)
            dto_class += "        this.{} = {};\n".format(field, field)
            dto_class += "    }\n"

            # generate the getter
            dto_class += "    public String get{}() {{\n".format(field.capitalize())
            dto_class += "        return this.{};\n".format(field)
            dto_class += "    }\n"

        # add the @JsonProperty annotations to the getters
        for field in fields:
            dto_class = dto_class.replace("public String get{}()".format(field.capitalize()),
                                          "@JsonProperty(\"{}\")\n    public String get{}()".format(field,
                                                                                                    field.capitalize()))

        # close the class
        dto_class += "}\n"

        # return the generated DTO class
        return dto_class

### test the DtoGenerator class
# class_name = "UserDTO"
# fields = ["id", "name", "email"]
#
# dto_generator = DtoGenerator()
# dto_class = dto_generator.generate_dto(class_name, fields)
#
# print(dto_class)
