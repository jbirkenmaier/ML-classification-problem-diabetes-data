def read_data(name_of_file):
    data=[]
    with open('%s'%name_of_file) as datafile:
        attributes = datafile.readline().split()
        for line in datafile:
            data.append(line.replace('\n', '').split(','))
        return data

        
        

    
