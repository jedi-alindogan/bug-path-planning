import matplotlib.pyplot as plt
from obstacles import Obstacle

class Map:
    def __init__(self, xbounds, ybounds, title):
        self.xlim = xbounds
        self.ylim = ybounds
        self.title = title

    def initMap(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(self.xlim[0], self.xlim[1])
        ax.set_ylim(self.ylim[0], self.ylim[1])
        ax.set_aspect('equal', adjustable='box')
        plt.title(self.title)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(False)
        return fig, ax

    def drawObstacles(self, ax, obstacles):
        for obstacle in obstacles:
            vertices = obstacle.getVertices()
            xs, ys = zip(*vertices)
            ax.fill(xs, ys, facecolor='black', edgecolor='black')

    def drawPath(self, ax, path):
        xs, ys = zip(*path)
        ax.plot(xs, ys, linestyle='-', marker=None, color='r')

    def drawMap(self, path, obstacles, save_path='map.png'):
        fig, ax = self.initMap()
        if obstacles:
            self.drawObstacles(ax, obstacles)
        if path:
            self.drawPath(ax, path)
        self.saveMap(fig, save_path)
        return fig, ax

    def saveMap(self, fig, save_path='map.png'):
        fig.savefig(save_path)
        plt.close(fig)
