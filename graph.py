from shortest import Shortest
class Graph:
    def __init__(self):
        self.__structure = {}
        self.__labels = {}

    def __iter__(self):
        return iter(self.__structure)

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self.__structure:
            vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += str(e) + ' '
        return hstr + vstr + estr
    __repr__ = __str__
    
    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self.__structure:
            for w in self.__structure[v]:
                #to avoid duplicates, only return if v is the first vertex
                if self.__structure[v][w].start() == v:
                    edgelist.append(self.__structure[v][w])
        return edgelist 
        

    def add_vertex(self, element):
        vertex = self.__Vertex(element)
        self.__labels[element] = vertex
        self.__structure[vertex] = {}
        return vertex

    def add_edge(self, vertex, adjacent, element,oneway = False):
        if not(vertex in self.__structure and adjacent in self.__structure)\
           or vertex == adjacent:
            return None
        edge = self.__Edge(vertex, adjacent, element)
        self.__structure[vertex][adjacent] = edge
        if  not oneway :
            self.__structure[adjacent][vertex] = edge
        return edge
    
    def get_vertex_by_label(self, element):   
        return self.__labels.get(element, None)

    def get_edges(self, v):
        """ Return a list of all edges incident on v. """
        if v in self.__structure:
            edgelist = []
            for w in self.__structure[v]:
                edgelist.append(self.__structure[v][w])
            return edgelist
        return None
    
    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self.__structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self.__structure:
            num += len(self.__structure[v]) 
        return num //2


    class __Vertex :
        def __init__(self, element):
            self.__element = element
            self.__adjacent = {}

        def add_adjacent(self, element, edge):
            self.__adjancet[element] = edge

        def __iter__(self):
            return iter(self.__adjacent)

        def __str__(self):
            return str(self.__element)

        def __eq__(self, other):
            return self.getElement() == other.getElement()

        def __hash__(self):
            return hash(self.__element)

        def getElement(self):
            return self.__element

        __repr__ = __str__


    class __Edge:

        def __init__(self, vertex, adjacent, element):
            self.__vertices = (vertex, adjacent)
            self.__element = element

        def start(self):
            return self.__vertices[0]

        def end(self):
            return self.__vertices[1]
    
        def opposite(self, vertex):
            """ Return the opposite vertex to v in this edge. """
            if self.__vertices[0] == vertex:
                return self.__vertices[1]
            elif self.__vertices[1] == vertex:
                return self.__vertices[0]
            else:
                return None
        
        def getElement(self):
            return self.__element

        

        def __str__(self):
            return "'(%s -- %s): %s'"%(str(self.__vertices[0]),
                                     str(self.__vertices[1]),
                                     str(self.__element))
        __repr__ = __str__

        



import re       
def readFile(filename):
    pat_match_node = re.compile(r"id[:\s]+(\d+)")
    From = r"from[:\s]+(?P<from>(\d+))"
    to = r"to[:\s]+(?P<to>(\d+))"
    length = r"length[:\s]+(?P<length>(\d+))"
    oneway = r"oneway[:\s]+(?P<oneway>(false|true))"
    pat_match_edge = re.compile("|".join([From,to,length,oneway]))
    with open(filename, "r") as f:
        line = f.readline().strip()
        while line:
            if line == "Node":
                line = f.readline().strip() 
                element = pat_match_node.match(line)
                if element:     
                    yield element.group(1)
                line = f.readline().strip()
            elif line == "Edge":
                line = f.readline().strip()
                edge = {}
                for _ in range(4):
                    match = pat_match_edge.match(line)
                    if match:
                        edge[match.lastgroup] = match.group(match.lastgroup)
                    line = f.readline().strip()
                yield edge

if __name__ == "__main__":
    g = Graph()
    for i in readFile("g2.txt"):
        if type(i) == dict:
            From = g.get_vertex_by_label(int(i["from"]))
            to = g.get_vertex_by_label(int(i["to"]))
            length = int(i["length"])
            oneway = i["oneway"] != "false" 
            if not(From is None or to is None or length is None):
                g.add_edge(From, to, length, oneway)
        else:
            g.add_vertex(int(i))
    sh = Shortest(g, 1)
    sh.short_to_all()
    sh.display()
    
                    
                
                
                
                


    
    
