#RULE-2:Tuple is immutable
#----------------------------
tu = ('Python', 'Java','J2ee', 'Android', 'Hadoop' )
print( type(tu) , tu  )
#tu[3] = "RDBMS"    #This line is error
print("tu.index('android')= ", tu.index('Android') )  #3
print(" 'Hadoop' in tu = " ,  'Hadoop' in tu  )
print(" 'Crysta' in tu = " ,  'Crysta' in tu  )
