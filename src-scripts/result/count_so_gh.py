"""
Export clone_pairs thar flow SO->GitHub direction

"""

import csv

siamese_filtered_clone_pairs_file = 'Online-Clone-Pairs-Filterd-Online-Clones.csv'
# file header
# serial_no, rank, so_snippet_path, so_start, so_end, git_snippet_path, git_start, git_end, classification, note

so_map = set()
git_map = set()

with open(siamese_filtered_clone_pairs_file) as csvfile:
    count = 0
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        so_snippet_path = row[2]  # .split("_")[0]
        so_map.add(so_snippet_path)
        git_snippet_owner_repo = row[5].split("/")
        git_repo_path = git_snippet_owner_repo[0].split("__")
        path = git_repo_path[0] + "/" + git_repo_path[1]
        git_map.add(path)

print(len(so_map))
print(len(git_map))
print(git_map)
