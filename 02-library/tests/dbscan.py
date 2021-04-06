from .sim import euclidean_dist


class DBC():

    def __init__(self,dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def _get_epsilon_neighborhoon(self, P):
        Neighborhood = []
        for point in range(len(self.dataset)):
            if euclidean_dist(self.dataset[point], self.dataset[P])<=epsilon:
                Neighborhood.append(point)
        return Neighborhood

    def _explore_PNeighborhood(self, assignments, assignment, P, PNeighborhood):
        assignments[P] = assignment

        while PNeighborhood:
            NextP = PNeighborhood.pop()

            if assignments[NextP] == -1:
                # must be a border point
                assignments[NextP] = assignment
            if assignments[NextP] == 0:
                # means we have never meet this point before
                assignments[NextP] = assignment
                NextPNeighborhood = self._get_epsilon_neighborhoon(NextP)

                if len(NextPNeighborhood) >= self.min_pts:
                    # core point
                    PNeighborhood += NextPNeighborhood

        return assignments

    def dbscan(self):
        assignments = [0 for _ in range(len(self.dataset))]
        assignment = 0 # cluster label

        for P in range(len(self.dataset)):
            if assignments[P] != 0:
                continue # skip this point and continue the for loop

            PNeighborhood = self._get_epsilon_neighborhoon(P)

            if Len(PNeighborhood) >= self.min_pts:
                # core points found, the we should explore its neighbors
                assignment+=1
                assignments = self._explore_PNeighborhood(assignments, assignment, P, PNeighborhood)
            else:
                # could be either border or noise
                assignments[P] = -1

        return assignments