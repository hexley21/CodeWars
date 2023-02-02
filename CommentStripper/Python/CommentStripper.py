def strip_comments(strng: str, markers):
    lines = strng.split('\n')
    for i in markers:
        for j in lines:
            if i in j:
                index = lines.index(j)
                lines[index] = j[:j.find(i)].rstrip()
    return '\n'.join(lines)
