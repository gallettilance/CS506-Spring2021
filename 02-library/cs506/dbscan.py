from .sim import euclidean_dist

class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def _get_epsilon_neighborhood(self, P):
        Neighborhood = []
        for point in range(len(self.dataset)):
            if euclidean_dist(self.dataset[point], self.dataset[P]) <= self.epsilon:
                Neighborhood.append(point)
        return Neighborhood


    def _explore_PNeighborhood(self, assignments, assignment, P, PNeighborhood):
        assignments[P] = assignment

        while PNeighborhood:
            NextP = PNeighborhood.pop()

            if assignments[NextP] == -1:
                # now we know it's a border point
                assignments[NextP] = assignment

            if assignments[NextP] == 0:
                # means we haven't seen this point before
                assignments[NextP] = assignment
                NextPNeighborhood = self._get_epsilon_neighborhood(NextP)

                if len(NextPNeighborhood) >= self.min_pts:
                    # core point
                    PNeighborhood += NextPNeighborhood

        return assignments


    def dbscan(self):
        assignments = [0 for _ in range(len(self.dataset))]
        assignment = 0

        for P in range(len(self.dataset)):
            if assignments[P] != 0:
                continue

            PNeighborhood = self._get_epsilon_neighborhood(P)

            if len(PNeighborhood) >= self.min_pts:
                # core point!
                assignment += 1
                assignments = self._explore_PNeighborhood(assignments, assignment, P, PNeighborhood)
            else:
                # could be either border or noise
                assignments[P] = -1

        return assignments