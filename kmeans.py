from __future__ import annotations
import numpy as np
from sklearn.base import ClusterMixin
from typing import Union, List


def minkowski_distance(a: np.array, b: np.array, p: Union[int, float] = 2) -> float:
    """
    Computes the minkowski distance between point a and b for the given parameter p
    :param a: n-dimensional point
    :param b: n-dimensional point
    :param p: paramter p as scalar | Default: 2 (for euclidean distance)
    :return: distance as float
    """
    return np.power(np.sum(np.power(np.abs(a - b), p)), 1 / p)


class KMeans(ClusterMixin):

    def __init__(self,
                 num_cluster: int,
                 n_iter: int = 10,
                 distance: callable = minkowski_distance,
                 verbose: bool = False,
                 random_state: int = 42):

        self.num_cluster = num_cluster
        self.n_iter = n_iter
        self.distance = distance
        self.verbose = verbose
        self.random_state = random_state

    def fit(self, X: np.ndarray) -> KMeans:
        """
        The model is fitted n_iter times
        and then the state with minimal inertia is chosen.
        :param X:
        :return:
        """
        models: List[KMeans] = []
        orig_random_state = self.random_state
        for iteration in range(self.n_iter):
            self.random_state += iteration
            model = self.__fit(X)
            models.append(model)
            if self.verbose:
                print(f'Iteration {iteration} | Inertia: {model.inertia__}')
        best_model = min(models, key=lambda x: x.inertia__)

        # update instance state with values of best models
        self.__dict__.update(best_model.__dict__)
        self.random_state = orig_random_state
        return self

    def __fit(self, X: np.ndarray) -> KMeans:
        """
        Fits the instance with given data.
        :param X:
        :return:
        """
        centroids = self.__init_cluster(X)

        last_centroids = np.zeros_like(centroids)
        cluster = np.array([])
        while not np.equal(last_centroids, centroids).all():
            last_centroids = centroids.copy()
            cluster = self.__build_cluster(X, centroids)
            centroids = self.__recompute_centroids(cluster)

        self.cluster__ = cluster
        self.centroids___ = centroids
        self.inertia__ = self.__compute_inertia()

        return self

    def __compute_inertia(self):
        """
        Computes the inertia if the instance is fitted
        :return:
        """
        inertia_values = []
        for cluster, centroid in zip(self.cluster__, self.centroids___):
            inertia_values.extend([self.distance(point, centroid) ** 2 for point in cluster])
        return np.mean(inertia_values)

    def __init_cluster(self, X: np.ndarray) -> np.array:
        """
        Picks num_cluster * 2 random points from data and computes their pairwise means
        to build the initial centroids.
        :param X: feature matrix (n_samples, n_features)
        :return: np.array containing the centroids (num_cluster, n_features)
        """
        np.random.seed(self.random_state)
        points = X[np.random.choice(X.shape[0], self.num_cluster * 2, replace=False), :]
        centroids = []
        for index in range(1, points.shape[0]):
            if index % 2 != 0:
                point_a = points[index - 1]
                point_b = points[index]
                mean = np.mean([point_a, point_b], axis=0)
                centroids.append(mean)
        # print(f'Initial picked centroids:\n{np.asarray(centroids)}')
        return np.asarray(centroids)

    def __build_cluster(self, X: np.ndarray, centroids: np.ndarray) -> List[np.ndarray]:
        """
        Builds clusters around in X from the passed centroids.
        :param X:
        :param centroids:
        :return:
        """
        cluster = [[] for _ in range(centroids.shape[0])]
        for point in X:
            cluster_ind = np.argmin([self.distance(point, centroid) for centroid in centroids])
            cluster[cluster_ind.item()].append(point)
        cluster = [np.asarray(i) for i in cluster]
        return cluster

    def __recompute_centroids(self, cluster: List[np.ndarray]) -> np.ndarray:
        return np.array([np.mean(clu, axis=0) for clu in cluster])


if __name__ == '__main__':

    from sklearn.datasets import make_blobs, make_moons
    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt

    centers = [[1, 1], [-1, -1], [1, -1]]
    X_blobs, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                                      random_state=0)

    X_blobs = StandardScaler().fit_transform(X_blobs)

    clu1 = KMeans(num_cluster=3, verbose=True)

    clu1.fit(X_blobs)
    fig, axs = plt.subplots(2, figsize=(15, 15))
    for ind, (cluster, centroid) in enumerate(zip(clu1.cluster__, clu1.centroids___)):
        axs[0].scatter(cluster[:, 0], cluster[:, 1])  # , label=f'Cluster {ind}')
        axs[0].scatter(centroid[0], centroid[1], marker='X', label=f'Centroid of cluster {ind}')

    clu2 = KMeans(num_cluster=2, verbose=True)

    X_moons, labels_true = make_moons(n_samples=750)

    clu2.fit(X_moons)
    for ind, (cluster, centroid) in enumerate(zip(clu2.cluster__, clu2.centroids___)):
        axs[1].scatter(cluster[:, 0], cluster[:, 1])  # label=f'Cluster {ind}')
        axs[1].scatter(centroid[0], centroid[1], marker='X', label=f'Centroid of cluster {ind}')

    fig.legend()
    fig.tight_layout()
    fig.show()
