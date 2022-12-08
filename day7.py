with open('day7_input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

class Node:
    def __init__(self, name, type, size=None, parent=None):
        assert type in ['file', 'dir'], "'type' must be either 'file' or 'dir'"
        self.name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.dir_children = None
        self.file_children = None

    def get_subdir(self, dirname):
        found_dir = None
        if self.dir_children is not None:
            for dir in self.dir_children:
                if dir.name == dirname:
                    found_dir = dir
                    break
        return found_dir

    def get_filechild(self, fname):
        found_file = None
        if self.file_children is not None:
            for file in self.file_children:
                if file.name == fname:
                    found_file = file
                    break
        return found_file

    def add_child(self, node):
        if node.type == 'file':
            if self.file_children is None:
                self.file_children = []
            self.file_children.append(node)
        else:
            if self.dir_children is None:
                self.dir_children = []
            self.dir_children.append(node)

    def get_size(self):
        if self.type == 'file':
            return self.size
        else:
            if self.size is None:
                mysize = 0
                if self.file_children is not None:
                    for file in self.file_children:
                        mysize += file.get_size()
                if self.dir_children is not None:
                    for dir in self.dir_children:
                        mysize += dir.get_size()
                self.size = mysize
            return self.size

    def get_subfolders_lessthan(self, maxsize):
        if self.type == 'file':
            print("Why would you call this on a file??")
            return None

        folder_size_list = []
        mysize = self.get_size()
        if mysize <= maxsize:
            folder_size_list.append(mysize)

        if self.dir_children is not None:
            for subdir in self.dir_children:
                folder_size_list.extend(subdir.get_subfolders_lessthan(maxsize))
        
        return folder_size_list

    def get_subfolders_greaterthan(self, minsize):
        if self.type == 'file':
            print("Why would you call this on a file??")
            return None

        folder_size_list = []
        mysize = self.get_size()
        if mysize >= minsize:
            folder_size_list.append(mysize)

        if self.dir_children is not None:
            for subdir in self.dir_children:
                folder_size_list.extend(subdir.get_subfolders_greaterthan(minsize))
        
        return folder_size_list

# Populate the File System data structure
root = Node('/', 'dir')
current_loc = root

i = 0
while i < len(data):
    parts = data[i].split()
    if len(parts) == 3:  # It's a 'cd' command
        dname = parts[2]
        if dname == '/':
            current_loc = root
        elif dname == '..':
            current_loc = current_loc.parent
        else:
            subdir = current_loc.get_subdir(dname)
            if subdir is None:
                subdir = Node(dname, 'dir', parent=current_loc)
                current_loc.add_child(subdir)
            current_loc = subdir
        i += 1
 
    else:  # It's an 'ls' command block             
        while data[i+1][0] != '$':
            i += 1
            parts = data[i].split()
            if parts[0].isnumeric():   # This is a file type
                fname = parts[1]
                fsize = int(parts[0])
                fnode = current_loc.get_filechild(fname)       # Existence checks to handle repeated calls to 'ls' in the same folder
                if fnode is None:
                    fnode = Node(fname, 'file', size=fsize, parent=current_loc)
                    current_loc.add_child(fnode)
            elif parts[0] == 'dir':
                dname = parts[1]
                subdir = current_loc.get_subdir(dname)
                if subdir is None:
                    subdir = Node(dname, 'dir', parent=current_loc)
                    current_loc.add_child(subdir)                    
            else:
                print("Something has gone terribly wrong")
            if i+1 == len(data):
                break
        i += 1

# Part 1
size_limit = 100000
small_folders = root.get_subfolders_lessthan(size_limit)
print(f"The size of my small folders totals to: {sum(small_folders)} ")

# Part 2
root_size = root.get_size()
free = 70000000 - root_size
min_delete_amount = 30000000 - free
large_folders = root.get_subfolders_greaterthan(min_delete_amount)
large_folders.sort()
print(f"The smallest single directory I can delete to free up enough space is size {large_folders[0]}")
