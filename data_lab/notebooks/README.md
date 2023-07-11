# Data Lab Educational Notebooks

![Reactor scene](./images/reactor_intro_scooter.png)
*Example Reactor Output*
<br><br>
This series of notebooks gives a guided tour through the functionality of Data Lab, building on concepts along the way by starting simple and working up to more complex usage. 

First, we review the process of configuring and rendering a basic driving scenario, which establishes the general structure of all Data Lab scripts. Then, we explore changing the environment and generator parameters to change the nature of the scene as we create parking and debris scenarios. Next, we get our first experience with custom simulation agents, placing a geometric primitive into the scene and inpainting it using Reactor's generative AI. After this, we cover making data for pedestrian edge cases, lane line detection, and road sign classification. We close out the land-based demonstrations with a case study on improving stroller detection using Reactor and some advanced simulation tricks.

Next, we take to the skies in drone scenes by taking simulation control of the ego agent. First we look at simulating the ego with a stored flight path, which may be obtained from real drone flight logs. Next, we interpolate between two points to generate a custom flight path, and relate this path to another airborne object to the scene. 

Finally we will look at calculating statistics on our generated data, and how these statistics can affect model training.
<br><br>

![Parking scene](./images/parking_scene.png)
*Example Parking Scene*

---

## Outline

1. [Data Lab Overview](./1_data_lab_overview.ipynb)
    - In this notebook we familiarize ourselves with the anatomy of a Data Lab script by generating a basic driving scenario.
2. [Parking scene](./2_parking.ipynb)
    - This notebook explores modifying agent and environment parameters to create parking scenes with a variety of parking space styles.
3. [Debris](./4_debris.ipynb)
    - We gain experience querying the asset library for interesting objects and scattering them in the scene using a debris generator.
4. [Intro to Reactor](./3_reactor_intro.ipynb)
    - We get our first glimpse at placing custom simulation agents, placing a geometric primitive in the scene and inpainting it using textual prompts and Reactor
5. [Pedestrian Behaviors](./5_pedestrians.ipynb)
    - We explore the possibilities of pedestrian control and the edge cases they can generate data for.
6. [Lane Lines](./6_lane_lines.ipynb)
    - We learn how to load map data and combine it with rendered frames to create lane line annotations.
7. [Road Signs](./7_road_signs.ipynb)
    - In this notebook we write functions to populate our environment with abundant road sign training examples.
8. [Reactor Stroller Experiment](./8_stroller_experiment)
    - We enact interdependent multi-object animation to place pedestrians behind strollers, and review training results achieved using a scaled output batch.
9. [Drone scene from flight log](./8_drone_from_flight_log.ipynb)
    - Takes an existing flight log and generate an airborne Data Lab scene.
10. [Airborne Object Tracking](./9_airborne_object_tracking.ipynb)
    - Jointly simulate an ego and another airborne object to create object tracking data.
11. [Impact of Dataset Statistics](./10_dataset_statistics.ipynb)
    - Observe the benefits of healing domain gap using dataset statistics to tune data generation parameters.