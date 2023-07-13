import logging
import random

from typing import Union, Dict, Optional

from pd.data_lab.config.distribution import CenterSpreadConfig, EnumDistribution, MinMaxConfigInt, MinMaxConfigFloat

import paralleldomain.data_lab as data_lab
from paralleldomain.data_lab.generators.ego_agent import AgentType, EgoAgentGeneratorParameters
from paralleldomain.data_lab.generators.parked_vehicle import ParkedVehicleGeneratorParameters
from paralleldomain.data_lab.generators.position_request import (
    LaneSpawnPolicy,
    LocationRelativePositionRequest,
    PositionRequest,
)
from paralleldomain.data_lab.generators.random_pedestrian import RandomPedestrianGeneratorParameters
from paralleldomain.data_lab.generators.traffic import TrafficGeneratorParameters
from paralleldomain.model.annotation import SemanticSegmentation2D, InstanceSegmentation2D, Depth
from paralleldomain.utilities.logging import setup_loggers
from paralleldomain.utilities.transformation import Transformation

setup_loggers(logger_names=["__main__", "paralleldomain", "pd"])
logging.getLogger("pd").setLevel(logging.CRITICAL)

FOV = 70


def build_sensor_rig():
    sensor_rig = data_lab.SensorRig(
        sensor_configs=[
            data_lab.SensorConfig.create_camera_sensor(
                name="Front",
                width=1920,
                height=1080,
                field_of_view_degrees=FOV,
                pose=Transformation.from_euler_angles(
                    angles=[0.0, 0.0, 0.0], order="xyz", degrees=True, translation=[0.0, 0.0, 2.0]
                ),
                annotation_types=[SemanticSegmentation2D, InstanceSegmentation2D, Depth],
            )
        ]
    )

    return sensor_rig


def build_empty_scenario(
    location_name: str = "SF_GrantAndCalifornia", 
    location_version: str = "local", 
    ego_lane_type: Union[str, Dict[str, float]] = "Drivable",
    sensor_rig: Optional[data_lab.SensorRig] = None,
    seed: int = None
):
    if seed is None:
        seed = random.randint(1, 1_000_000)

    if isinstance(ego_lane_type, str):
        ego_lane_type = {ego_lane_type: 1.0}
    
    if sensor_rig is None:
        sensor_rig = build_sensor_rig()

    print(f"Using random seed {seed} on {location_name}")

    # Create scenario
    scenario = data_lab.Scenario(sensor_rig=sensor_rig)
    scenario.random_seed = seed

    # Set location
    scenario.set_location(data_lab.Location(name=location_name, version=location_version))

    # Set weather variables and time of day
    scenario.environment.time_of_day.set_category_weight(data_lab.TimeOfDays.Day, 0.9)
    scenario.environment.time_of_day.set_category_weight(data_lab.TimeOfDays.Dusk, 0.1)
    scenario.environment.clouds.set_uniform_distribution(min_value=0.0, max_value=0.3)
    scenario.environment.rain.set_constant_value(0.0)
    scenario.environment.fog.set_constant_value(0.0)
    scenario.environment.wetness.set_uniform_distribution(min_value=0.1, max_value=0.2)

    # Place ourselves in the world
    scenario.add_ego(
        generator=EgoAgentGeneratorParameters(
            agent_type=AgentType.VEHICLE,
            position_request=PositionRequest(
                lane_spawn_policy=LaneSpawnPolicy(
                    lane_type=EnumDistribution(
                        probabilities=ego_lane_type,
                    )
                )
            ),
        ),
    )

    return scenario


def build_demo_scenario(
    location_name: str = "SF_GrantAndCalifornia", 
    location_version: str = "local", 
    ego_lane_type: Union[str, Dict[str, float]] = "Drivable",
    sensor_rig: Optional[data_lab.SensorRig] = None,
    seed: int = None,
    traffic_density: float = 0.7
):

    # Load environment and ego vehicle
    scenario = build_empty_scenario(
        location_name=location_name, 
        location_version=location_version,
        ego_lane_type=ego_lane_type,
        sensor_rig=sensor_rig,
        seed=seed
    )

    # Place parked vehicles in the scene
    scenario.add_agents(
        generator=ParkedVehicleGeneratorParameters(
            spawn_probability=CenterSpreadConfig(center=0.5, spread=0.1),
            position_request=PositionRequest(
                location_relative_position_request=LocationRelativePositionRequest(
                    agent_tags=["EGO"],
                    max_spawn_radius=150.0,
                )
            ),
        )
    )

    # Place traffic in the scene
    scenario.add_agents(
        generator=TrafficGeneratorParameters(
            spawn_probability=traffic_density,
            position_request=PositionRequest(
                location_relative_position_request=LocationRelativePositionRequest(
                    agent_tags=["EGO"],
                    max_spawn_radius=150.0,
                )
            ),
        )
    )

    # Place random pedestrians in the scene
    scenario.add_agents(
        generator=RandomPedestrianGeneratorParameters(
            position_request=PositionRequest(
                location_relative_position_request=LocationRelativePositionRequest(
                    agent_tags=["EGO"],
                    max_spawn_radius=100.0
                )
            ),
            num_of_pedestrians_range=MinMaxConfigInt(min=10, max=60),
            speed_range=MinMaxConfigFloat(min=0.5, max=1.1)
        )
    )

    return scenario
