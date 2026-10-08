# !!! TOUCHEZ PAS À CE FICHIER LÀ. LE SERVER A SA PROPRE VERSION !!!

from dataclasses import dataclass

import numpy as np

__all__ = ["CenterlinePoint", "Controller", "TrackInfo"]


@dataclass(frozen=True)
class CenterlinePoint:
    """
    One point of the track's centerline, with its distance to each wall.
    Left and right are relative to the direction of travel. All distances
    are in meters.
    """

    x: float
    y: float
    # !!! TOUCHEZ PAS À CE FICHIER LÀ. LE SERVER A SA PROPRE VERSION !!!
    distance_wall_left: float
    distance_wall_right: float


@dataclass(frozen=True)
class TrackInfo:
    """
    You probably only ever care about the centerline.
    It is the same as the CSV we provide.
    """

    name: str
    track_length: float
    width: float
    # !!! TOUCHEZ PAS À CE FICHIER LÀ. LE SERVER A SA PROPRE VERSION !!!
    centerline: tuple[CenterlinePoint, ...] = ()


class Controller:
    """
    Base class for your controller.
    Coordinates are in meters, angles in radians, with yaw 0 along +x and
    positive counter-clockwise.
    """

    def reset(self, track_info: TrackInfo) -> None:
        """Called once before the first step, to initialize your state."""

    # !!! TOUCHEZ PAS À CE FICHIER LÀ. LE SERVER A SA PROPRE VERSION !!!
    def step(
        self,
        x: float,
        y: float,
        yaw: float,
        speed: float,
        steering_angle: float,
        laser_scan: np.ndarray,
    ) -> tuple[float, float]:
        """Return (target_speed, target_steering_angle) for this step.

        Receives:

        - `x`, `y`: the car's position, in m.
        - `yaw`: its heading, in rad.
        - `speed`: its speed along the heading, in m/s.
        - `steering_angle`: the front wheels' current angle, in rad,
          positive = left.
        - `laser_scan`: the full-circle scan, a numpy array of beam
          distances in m, one per beam. Beam 0 points straight ahead (along
          `yaw`); beam i is at yaw + i * 360 / len(laser_scan) degrees,
          counter-clockwise. A beam stops at the first wall or racing car
          in its path, and reads `np.inf` if it hits nothing: there is no
          max range.

        Returns:

        - `target_speed`, in m/s, clamped to [0, 30] (no reverse).
        - `target_steering_angle`, in rad, clamped to +/- 0.5, positive =
          left.
        """
        raise NotImplementedError


# !!! TOUCHEZ PAS À CE FICHIER LÀ. LE SERVER A SA PROPRE VERSION !!!
