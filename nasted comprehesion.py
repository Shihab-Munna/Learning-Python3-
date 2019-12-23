identity_matrix =[]

identity_matrix = [ [ 1 if item_idx == row_idx else 0 for item_idx in range(0, 3) ] for row_idx in range(0, 3) ]

print(*identity_matrix,sep="\n")
