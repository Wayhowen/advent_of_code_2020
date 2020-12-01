class FileReader:
    def __init__(self):
        pass

    def read_file(self, filename):
        with open(filename, "r") as file:
            if "txt" in filename:
                result = [int(num.strip()) for num in file.readlines()]
            elif "json" in filename:
                pass
        return result