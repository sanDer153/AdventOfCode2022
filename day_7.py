

class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.directories = {"..": parent}
        if parent is None:
            self.directories = {"..": self}
        self.files = dict()
        self.size = None
        self.size_correct = False

    def get_directories(self):
        return self.directories

    def is_size_correct(self):
        return self.size_correct

    def get_size(self):
        return self.size

    def add_directory(self, name):
        if name not in self.directories.keys():
            self.directories[name] = Dir(name, self)
            return self.directories[name]
        return None

    def add_file(self, name, size):
        if name not in self.files.keys():
            self.files[name] = File(name, size)
            return self.files[name]
        return None

    def calc_size(self):
        child_dirs = set(self.directories.values()).difference({self.directories[".."]})
        if all(d.is_size_correct() for d in child_dirs):
            self.size = sum(d.get_size() for d in child_dirs) + sum(f.get_size() for f in self.files.values())
            self.size_correct = True
            return self.size
        return None
        

class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


def first_star():
    root = Dir("/", None)
    current_dir = None
    dirs_pre_size = [root]
    solution = 0
    with open("day_7_input") as f:
        for line in f:
            l = line.strip("\n").split(" ")
            if l[0] == "$":
                if l[1] == "cd":
                    if l[2] == "/":
                        current_dir = root
                    else:
                        current_dir = current_dir.get_directories()[l[2]]
            elif l[0] == "dir":
                directory = current_dir.add_directory(l[1])
                if directory != None:
                    dirs_pre_size.append(directory)
            else:
                current_dir.add_file(l[1], int(l[0]))

    while(len(dirs_pre_size) != 0):
        _dirs_pre_size = list()
        for d in dirs_pre_size:
            d.calc_size()
            if d.is_size_correct():
                if d.get_size() <= 100000:
                    solution += d.get_size()
            else:
                _dirs_pre_size.append(d)
        dirs_pre_size = _dirs_pre_size

    print(solution)

def second_star():
    root = Dir("/", None)
    current_dir = None
    dirs_pre_size = [root]
    calculated_dirs = []
    with open("day_7_input") as f:
        for line in f:
            l = line.strip("\n").split(" ")
            if l[0] == "$":
                if l[1] == "cd":
                    if l[2] == "/":
                        current_dir = root
                    else:
                        current_dir = current_dir.get_directories()[l[2]]
            elif l[0] == "dir":
                directory = current_dir.add_directory(l[1])
                if directory != None:
                    dirs_pre_size.append(directory)
            else:
                current_dir.add_file(l[1], int(l[0]))

    while(len(dirs_pre_size) != 0):
        _dirs_pre_size = list()
        for d in dirs_pre_size:
            d.calc_size()
            if d.is_size_correct():
                calculated_dirs.append(d)
            else:
                _dirs_pre_size.append(d)
        dirs_pre_size = _dirs_pre_size

    space_to_clear = 30000000 - (70000000 - root.get_size())
    solution = min(d.get_size() for d in calculated_dirs if d.get_size() >= space_to_clear)
    print(solution)

first_star()
second_star()