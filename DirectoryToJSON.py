import os
import json
import glob

def get_directory_tree(path):
    tree = {}
    total_size = 0

    search_pattern = os.path.join(path, "*")
    children = glob.glob(search_pattern, recursive=False)
    files = [child for child in children if os.path.isfile(child)]
    dirs = [child for child in children if os.path.isdir(child)]
    
    if files.count != 0:
        fileTree = {}
        for file in files:
            try:
                file_size = os.path.getsize(file)
                name = os.path.basename(file)
                total_size += file_size
                fileTree[name] = file_size
            except (PermissionError, FileNotFoundError) as e:
                fileTree[file] = f"Error: {e}"
        tree["files"] = fileTree
    
    if dirs.count != 0:
        dirTree = {}
        for dir in dirs:
            try:
                dir_tree, dir_size = get_directory_tree(dir)
                total_size += dir_size
                dir_name = os.path.basename(dir)
                dirTree[dir_name] = dir_tree
            except (PermissionError, FileNotFoundError) as e:
                dirTree[dir] = f"Error: {e}"
        tree["directories"] = dirTree
    
    return tree, total_size

def main():
    path = input("Entrez le chemin du dossier: ")
    if not os.path.exists(path):
        print("Le chemin spécifié n'existe pas.")
        return

    tree, total_size = get_directory_tree(path)
    output = {
        "tree": tree,
        "total_size": total_size
    }

    with open("directory_tree.json", "w") as f:
        json.dump(output, f, indent=4)

    print(f"Arborescence du dossier sauvegardée dans 'directory_tree.json'")

if __name__ == "__main__":
    main()
