def readInEdgesASCII (filename):
    try:
        edge_file = open(filename, 'r')
        num_edges = int(edge_file.readline().rstrip())
        edge_list = list()

        for line in edge_file:
            edge = line.split(' ')
            edge_list.append((int(edge[0]), int(edge[1])))

        edge_file.close()

        return edge_list

    except IOError:
        print "Could not open file " + filename + "."
        return False
    except TypeError:
        print "Could not read number of edges or edge values from file " + filename + "."
        return False
