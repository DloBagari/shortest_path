from AQP import APQ
class Shortest:
    def __init__(self, graph, start):
        self.__start = start
        self.__graph = graph
        self.__queue  = APQ()
        self.__path = {}
        self.__visited = set()
        self.__closed = set()

    def short_to_all(self):
        q = self.__queue
        g = self.__graph
        target = g.get_vertex_by_label(self.__start)
        if target:
            self.__path[target] = (None, 0)
            q.add(0,target)
        while len(self.__queue):
            element = q.getMin()
            vertex = element.getValue()
            for edge in g.get_edges(vertex):
                opposite = edge.opposite(vertex)
                if opposite in  self.__closed:
                    continue
                new_cost = element.getKey() + edge.getElement()
                if opposite in self.__visited and new_cost < self.__path[opposite][1]:
                        self.__path[opposite] = (vertex, new_cost)
                        q.update(opposite, new_cost)
                else:
                    q.add(new_cost, opposite)
                    self.__path[opposite] = (vertex, new_cost)
                    self.__visited.add(opposite)
            self.__closed.add(vertex)
            
    def display(self):
        for vertex in self.__path:
            if self.__path[vertex][0] is not None:
                preceding = self.__path[vertex][0]
                path = [vertex]
                while preceding:
                    path.append(preceding)
                    preceding = self.__path[preceding][0]
                path.reverse()
                print("From %-3s To %-3s\n  Cost:%-4s\n  Length:%d\n  Path:<>\n" %\
                      (str(path[0]),str(vertex),self.__path[vertex][1],
                       len(path) -1))#,", ".join(str(i) for i in path)))
    def show(self):
        print(self.__path) 
        


                    
                    
                    
                        
                
            
