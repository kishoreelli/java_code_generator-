import os


class FileWriter:
    def __init__(self, package_name):
        self.package_name = package_name

    def write_to_file(self, class_name, class_string):
        os.makedirs(self.package_name, exist_ok=True)

        with open(f"{self.package_name}/{class_name}.java", "w") as f:
            f.write(class_string)
