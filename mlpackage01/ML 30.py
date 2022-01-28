#RULE-1: Lists are mutable
#----------------------------
a = ["Noida", "Delhi", "Lucknow", "Goa", "Kanpur"]                  # This is list
#     0         1          2        3        4
a[3] = "UK"
print( a  )
a.append("Patna")
print( a  )

del a[1]
print( a )

a.insert(0, "Varanasi")
print( a )