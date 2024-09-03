#!/usr/bin/env python3


import mujoco
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

"""
This module is used to visualize different mujoco experiments.

"""
class Viz:
    def __init__(self, d : mujoco.MjData = None):
        """
        Args:
            d: MjData Mujoco data
        """

        self.d : mujoco.MjData = d
        self._trajectory_x: List = []
        self._trajectory_y: List = []
        self._trajectory_z: List = []
        self._err_x: List = []
        self._err_y: List = []
        self._err_z: List = []
        self.errFig= plt.figure()
        self.aX = self.errFig.add_subplot(311)
        self.aY = self.errFig.add_subplot(312)
        self.aZ = self.errFig.add_subplot(313)

    def record_trajectory_sim(self, track: str, depth : int = 500):
        """
        Records the trajectory for the given depth ammount, and once the depth
        is reached the trajectory will clear

        Args:
            track: Object to track
            depth: length of the history
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

        Args:
            points: Points of object in space to track
            depth: length of the history
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

    def record_errors(self, errors, depth : int = 500):
        """
        Records the errors of the blimp for expected location

        Args:
            errors: Position difference between expected vs current
            depth: Howmany erros to record
        """
        if len(self._err_x) < depth:
            self._err_x.append(errors[0])
        else:
            self._err_x = self._err_x[10:]
        if len(self._err_y) < depth:
            self._err_y.append(errors[1])
        else:
            self._err_y = self._err_y[10:]
        if len(self._err_z) < depth:
            self._err_z.append(errors[2])
        else:
            self._err_z = self._err_z[10:]

    def plot_error(self,i, fileName: str = "errFigure.png"):
        self.aX.plot(self._err_x)
        self.aY.plot(self._err_y)
        self.aZ.plot(self._err_z)
        # ax.scatter(self._trajectory_x, self._trajectory_y, self._trajectory_z)
        # ax.set_xlabel("X - meters")
        # ax.set_ylabel("Y - meters")
        # ax.set_title("Trajectory of the blimp")
        # plt.savefig(fileName)

    def amimate_error(self, fileName: str = "animation.mp4"):
        anim = FuncAnimation(self.errFig, self.plot_error, interval = 5)
        anim.save(fileName)
        
