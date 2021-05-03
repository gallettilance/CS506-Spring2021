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
        # this method explore all the neighbors of neighbors of neighbors of neighbors...that should be assigned to the same cluster as point P 
        # (passed in as a parameter). We first assign P to the current label: assignment
        assignments[P] = assignment

        # this while condition is true as long as there are still items in the PNeighborhood array. We will treat PNeighborhood as a queue (FIFO), because
        # we anticipate to offer assignments to other points further away from the P that are not directly within the Epsilon neighborhood of P. Think of 
        # PNeighborhood as containing points that should belong to the same cluster as P. Every single point in PNeighborhood should have their clsuter assignment be P
        while PNeighborhood:
            # we pop one by one the elements in PNeighbors, store it as NextP, and processes it
            NextP = PNeighborhood.pop()

            # if the point is assigned -1, then it is either a border point or a noise point. However, since we invoked this function from a core point, for NextP to be
            # in the queue PNeighborhood, it must be within the epsilon neighborhood of P, or epsilon neighborhood of a point that's assigned to the same cluster as P. 
            # therefore, it s a border point and we give it the assignment the same as P
            if assignments[NextP] == -1:
                # now we know it's a border point
                assignments[NextP] = assignment

            # If a point is 0, it means that it hasn't been visited yet. We first assigns it to the same cluster as P (since it is in the PNeighborhood queue), then we
            # check how many neighbors it has. If it has more than min_pts number of neighbors, then it is a core point on its own. Since it is a core point, all points in
            # its epsilon neighborhood should be assigned the same cluster as itself, which means that all points in its epsilon neighborhood should be assigned to the same
            # cluster as P. Therefore, we add the neighbors of this point to our queue for addition later. Notice that we make an assignment no matter what, which means
            # everything in the queue PNeighborhood will be assigned, because they should be
            if assignments[NextP] == 0:
                # means we haven't seen this point before
                assignments[NextP] = assignment
                NextPNeighborhood = self._get_epsilon_neighborhood(NextP)

                if len(NextPNeighborhood) >= self.min_pts:
                    # core point
                    PNeighborhood += NextPNeighborhood

        return assignments


    def dbscan(self):
        # assignments contains the current assignment for all the points
        # initialize to 0 to represent unvisited
        assignments = [0 for _ in range(len(self.dataset))]
        # assignment is the current label, or the current cluster that a point would be assigned to
        # initialize to 0 to represent unvisited, will be incremented to on the first iteration
        # 1 will be the label of the first cluster
        assignment = 0

        # we would like to represent point by their indices in the dataset. the loop variable P contains the index of the current point
        # being processed
        for P in range(len(self.dataset)):
            # if the assignment of the current point P is not 0, meaning that it has been assigned to some clusters, then don't recompute
            # continue ends the current iteration of the for loop and moves on to the next one
            # if you recompute it for a point that's already been assigned, there would be two scenarios. In the first scenario, it's a 
            # border or a noise point (corresponding to the else part below), in which case nothing would go wrong. However, if you've
            # encountered a core point whose cluster is already assigned because it it close to another core point, then the if part below
            # would increment the "assignment" variable (or the current label) by 1, and thus removing it from the cluster. Since we structured
            # our _explore_PNeighborhood such that it only recognizes assignment values of -1 and 0, meaning that it doesn't know how to
            # handle the cases where the value has already been seen, it would just assign the newly modified core point to the newly incremented
            # new cluster without exploring its neighbors. The code would break. 
            # We don't want to handle the case where the value has been seen, because it's extra unnecessary work. Thus, this method is more 
            # efficient. If we constructed in the other way, we run the risk of getting into an infinite loop, where points in an old cluster 
            # keeps on getting incremented to new labels, and the entire cluster changes with it 
            if assignments[P] != 0:
                continue
            
            # Pneighborhood calls the _get_epsilon_neighborhood(P) method to return a list of points within its epsilon neighborhood, identified 
            # by their index in the array                    
            PNeighborhood = self._get_epsilon_neighborhood(P)

            # the if statement checked if the point is a core point by checking the number of points in its epsilon neighbor
            if len(PNeighborhood) >= self.min_pts:
                # if we've reached here, then the point is indeed a core point. Since we used 0 to represent unvisited values, increment
                # by 1 to initialize the first cluster. If this code is reached again in the future, it means that a _explore_PNeighbors has terminated
                # and we've just finished assigning points to one cluster. Now the algorithm is moving onto a second cluster.
                assignment += 1
                # after updating the current label, we have not assigned the new label to any points (not even the point itself). A better way to assign
                # is to visit all of the points in the current point's epsilon neighborhood. All points in its epsilon neighborhood should be assigned 
                # to the same cluster as the current point. Also, for all the points in the epsilon neighborhood of the current point, all of the points in 
                # their epsilon neighborhood should be assigned to the same cluster as current point as well
                # based on this logic, we set the assignments variable (which contains the assignment of each point to clusters) to the return value of 
                # another helper method. We pass in the current assignments, and the current label (the assignment variable without s), the index of the current
                # point (as an identifier of which current point we're working on), and the list of neighbors in its epsilon neighborhood
                assignments = self._explore_PNeighborhood(assignments, assignment, P, PNeighborhood)
            
            # when a point's PNeighborhood is less than min_pts, it means that it doesn't qualify for the conditions that identifies
            # a point to be a core point. Therefore, it is either a border point or a noise point
            # we don't figure which one it is here. This is because within the _explore_PNeighborhood helper method, we would check
            # whether we've encountered a point that got assigned -1. Since _explore_PNeighborhood can only be triggered by the if statements
            # of a core point, then that non-deterministic point (border or noise) will have to be a border point, because it resides within
            # the epsilon neighborhood of a core point.
            else:
                assignments[P] = -1

        return assignments