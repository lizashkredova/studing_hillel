class Context_manager:
    def __init__(self, file):
        self.file_ = open(file, 'w')

    def __enter__(self):
        return self.file_

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file_.close()

with Context_manager("text.txt") as file:
    file.write("Hi, user")