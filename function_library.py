def read_data(name_of_file):
    with open('%s'%name_of_file) as datafile:
        attributes = datafile.readline().split()
        print(attributes)
        

    
