def find(string, substring):
    for i in range(len(string) - len(substring) + 1):
        fragment = string[i:i + len(substring)]
        if fragment == substring:
            return i

    return -1


print(find("ATCGTAG", "TAG"))
print(find("ATCGTAG", "XYZ"))