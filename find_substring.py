


def longest_common_subst_dp(value1: str, value2: str):
    """ find the first longest common substring in value1 and value2 strings using dynamic programming
     Returns
       - the longest common substring  """
    
    # dyn prog table. Every dynamic programming solution involves a table
    dptable = []
    result = ""

    #substr max length
    subMaxLength = 0
    #substr last position in value2
    subLastPos = 0

    for i, char1 in enumerate(value2):
        row = []
        for j, char2 in enumerate(value1):
            if char1 == char2:
                prevCell = dptable[i-1][j-1] if i >=1 and j >= 1 else 0
                cell = prevCell + 1
                row.append(cell)
                if subMaxLength < cell:
                    subMaxLength = cell
                    subLastPos = j
            else:
                row.append(0)
        dptable.append(row)

    if subMaxLength > 0:
        result = value1[subLastPos-subMaxLength+1:subLastPos+1]

    return result