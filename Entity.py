class Field:
    def __init__(self, name, datatype):
        self.name = name
        self.type = datatype


class Entity:
    def __init__(self, class_name, fields):
        self.class_name = class_name
        self.fields = fields

    def generate_entity_class(self):
        # Generate the entity class code
        class_code = f"import javax.persistence.Entity;\n\n"
        class_code += f"@Entity\npublic class {self.class_name} {{\n"

        # Generate the field declarations
        for field in self.fields:
            class_code += f"  private {field.type} {field.name};\n"

        # Generate the getters and setters
        for field in self.fields:
            # Generate the getter
            class_code += f"  public {field.type} get{field.name.capitalize()}() {{\n"
            class_code += f"    return this.{field.name};\n"
            class_code += "  }\n\n"

            # Generate the setter
            class_code += f"  public void set{field.name.capitalize()}({field.type} {field.name}) {{\n"
            class_code += f"    this.{field.name} = {field.name};\n"
            class_code += "  }\n"

        # Close the class
        class_code += "}\n"

        return class_code

    def generate_repository(self):
        # Generate the repository code
        repository_code = f"import java.util.List;\nimport org.springframework.data.repository.CrudRepository;\n\n"
        repository_code += f"@Repository\npublic interface {self.class_name}Repository extends CrudRepository<{self.class_name}, Long> {{\n"

        # Add the finder methods
        for field in self.fields:
            repository_code += f"  List<{self.class_name}> findBy{field.name.capitalize()}({field.type} {field.name});\n"

        # Close the repository
        repository_code += "}\n"

        return repository_code

# test the Entity class
# fields = [Field("id", "long"), Field("name", "String")]
# my_entity = Entity("Person", fields)
# print(my_entity.generate_entity_class())
# print(my_entity.generate_repository())
