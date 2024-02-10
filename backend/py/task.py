from dataclasses import dataclass


@dataclass
class File:
    id: int
    name: str
    categories: list [str]
    parent: int
    size: int


"""
Task 1
"""


def leafFiles(files: list [File]) -> list [str]:
    parent_id = []
    leaffile_name = []
    # Iterate the list, record all the parent file
    for file in files:
        if file.parent not in parent_id:
            parent_id.append (file.parent)
    # Iterate the list, obtain all files that is not a parent file of other file
    for file in files:
        if file.id not in parent_id:
            leaffile_name.append (file.name)
    return leaffile_name


"""
Task 2
"""


def kLargestCategories(files: list [File], k: int) -> list [str]:
    Categories = {}
    # Get count for all categories
    for file in files:
        for category in file.categories:
            if category in Categories:
                Categories [category] += 1
            else:
                Categories [category] = 1
    # Get the k largest categories
    if k >= len (Categories):
        return [item [0] for item in Categories]
    # Sort items by count in descending order, by name alphabetically
    sorted_Categories = sorted (Categories.items (), key = lambda x: (-x [1], x [0]))

    # Get names of the two most common items
    k_largest_Categories = [item [0] for item in sorted_Categories [:k]]
    return k_largest_Categories


"""
Task 3
"""

# Use a recursive method to obtain the size of each file
def calculate_total_size(file_id,files: list [File])-> int:
    total_size = 0
    for file in files:
        if file.parent == file_id:
            total_size += file.size + calculate_total_size (file.id,files)
    return total_size

def largestFileSize(files: list [File]) -> int:
    max_size = 0
    for file in files:
        total_size = calculate_total_size (file.id,files)
        max_size = max (max_size, total_size)
    return max_size



if __name__ == '__main__':
    testFiles = [
        File (1, "Document.txt", ["Documents"], 3, 1024),
        File (2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File (3, "Folder", ["Folder"], -1, 0),
        File (5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File (8, "Backup.zip", ["Backup"], 233, 8192),
        File (13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File (21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File (34, "Folder2", ["Folder"], 3, 0),
        File (55, "Code.py", ["Programming"], -1, 1536),
        File (89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File (144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File (233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted (leafFiles (testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]
    assert kLargestCategories (testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
