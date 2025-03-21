import matplotlib.pyplot as plt
from obstacles import Obstacle

class Map:
    def __init__(self, xbounds, ybounds, title = "", obstacles = None):
        self.setObstacles(obstacles)
        self.xlim = xbounds
        self.ylim = ybounds

    def initPlot(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(self.xlim[0], self.xlim[1])
        ax.set_ylim(self.ylim[0], self.ylim[1])
        ax.set_aspect('equal', adjustable='box')
        plt.title("TEST")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(False)
        return fig, ax
    
    def getObstacles(self):
        return self.obstacles
    
    def setObstacles(self, obstacles):
        self.obstacles = obstacles

    def drawObstacles(self, ax, obstacles):
        for obstacle in obstacles:
            vertices = obstacle.getVertices()
            xs, ys = zip(*vertices)
            ax.fill(xs, ys, facecolor='black', edgecolor='black')

    def drawTrajectories(self, ax, trajectories):
        xs, ys = zip(*trajectories)
        ax.plot(xs, ys, linestyle='-', marker=None, color='r')

    def drawMap(self, trajectories=None, obstacles=None, save_path='map.png'):
        fig, ax = self.initPlot()
        if obstacles:
            self.drawObstacles(ax, obstacles)
        if trajectories:
            self.drawTrajectories(ax, trajectories)
        self.saveMap(fig, save_path)
        return fig, ax

    def saveMap(self, fig, save_path='map.png'):
        fig.savefig(save_path)
        plt.close(fig)
