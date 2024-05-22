#!/usr/bin/env python3


import mujoco
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
This module is used to visualize different mujoco experiments.

"""
class Viz:
    def __init__(self, d : mujoco.MjData = None):
        """
        @params MjData Mujoco data
        """

        self.d : mujoco.MjData = d
        self._trajectory_x: List = []
        self._trajectory_y: List = []
        self._trajectory_z: List = []



    def record_trajectory_sim(self, track: str, depth : int = 500):
        """
        Records the trajectory for the given depth ammount, and once the depth
        is reached the trajectory will clear

        @param track Object to track
        @param depth length of the history
        """

        if len(self._trajectory_x) < depth:
            self._trajectory_x.append(self.d.geom(track).xpos[0])
        else:
            self._trajectory_x = self._trajectory_x[10:]
        if len(self._trajectory_y) < depth:
            self._trajectory_y.append(self.d.geom(track).xpos[0])
        else:
            self._trajectory_y = self._trajectory_y[10:]
        if len(self._trajectory_z) < depth:
            self._trajectory_z.append(self.d.geom(track).xpos[0])
        else:
            self._trajectory_z = self._trajectory_z[10:]

    def record_trajectory_real(self, points: tuple, depth : int = 500):
        """
        Records the trajectory for the given depth ammount, and once the depth
        is reached the trajectory will clear

        @param points Points of object in space to track
        @param depth length of the history
        """

        if len(self._trajectory_x) < depth:
            self._trajectory_x.append(points[0])
        else:
            self._trajectory_x = self._trajectory_x[10:]
        if len(self._trajectory_y) < depth:
            self._trajectory_y.append(points[1])
        else:
            self._trajectory_y = self._trajectory_y[10:]
        if len(self._trajectory_z) < depth:
            self._trajectory_z.append(points[2])
        else:
            self._trajectory_z = self._trajectory_z[10:]


    def plot_trajectory(self, fileName: str = "fig.png"):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self._trajectory_x, self._trajectory_y, self._trajectory_z)
        ax.set_xlabel("X - meters")
        ax.set_ylabel("Y - meters")
        ax.set_title("Trajectory of the blimp")
        plt.savefig(fileName)
