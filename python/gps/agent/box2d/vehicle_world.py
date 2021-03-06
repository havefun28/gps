""" 
This file defines an environment for the vehicle simulator. 
"""

import Box2D as b2 
import numpy as np
import cv2
import pygame
from framework import Framework 
from gps.agent.box2d.settings import fwSettings
from gps.agent.box2d.traffic import Traffic 
from gps.proto.gps_pb2 import END_EFFECTOR_POINTS, END_EFFECTOR_POINT_VELOCITIES

STEERINGSCALE = 0.01
BUS_LENGTH = 5.
BUS_WIDTH = 1.

# For traffic map
# macros
DISP_SCALE = 1  #10          # display pixels per meter
SCREEN_BORDER = 0.3      # border to keep vehicle in the screen
STEERING_RATIO = 12      # steering wheel to steering angle ratio

SPEED_DECAY = 0.05       # vehicle speed decrease each timestep
COLL_SPEED = 0.1         # percentage speed remaining after collision

MAP_CLEARANCE = 20       # clearance between route and map borders (meters)
CAR_DIST_MAX = 250       # max distance between car and ego vehicle before respawning

TASK_DIST = 1000         # meters from starting point to goal
COVER_TILE = 5           # distance per tile of road to cover
SHOW_TILES = 20          # show the next 20 tiles
LANE_WIDTH = 8           # width of lane in meters
LANE_DEVIATION = 1       # random cars deviation from center of lane
OBS_SCALE = 1            # observation pixels per meter
OBS_CLEARANCE = 0.25     # clearance between vehicle and observation

MAX_EP_TIME = 100        # maximum no of seconds per episode
WAIT_TIME = 10           # maximum waiting time (seconds) for vehicle to cover another tile before terminating episode

IMAGES = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple', 'aqua', 'magenta', 'white']

# state values
SELF = 255
UNCOVERED = 200
ROAD = 150
OUT = 50
OBSTACLE = 0

# pygame colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BACKGROUND = (50,50,50)
TEXT = (200,200,200)

STATE_W = 48
STATE_H = 48
SCREEN_W = 1000
SCREEN_H = 1000
THROTTLE_SCALE = 0.01    
STEERING_SCALE = 0.02    
STEER_ANGLE = 20        

GROUND_EDGE = 20
BOX_SCALE = 10

class VehicleWorld(Framework):
    """ This class defines the vehicle and its environment"""
    name = "Vehicle"
    def __init__(self, x0, target, render):
        # TODO: try to pass the initial point as shift so that it will not affect the original code
        self.render = render
        if self.render:
            super(VehicleWorld, self).__init__()
        else: 
            self.world = b2.b2World(gravity=(0, -10), doSleep=True)
        self.world.gravity = (0.0, 0.0)
        self.initial_position = (x0[0], x0[1])
        self.initial_angle = x0[2]
        self.initial_linear_velocity = (x0[3], x0[4])
        self.initial_angular_velocity = x0[5]
        # ?? how to assign the parameter setting to dynamic body itself?  
        self.wheelbase = BUS_LENGTH
        self.lr = BUS_LENGTH/2

        ground = self.world.CreateBody(position=(0,0)) # set the initial position of the body
        ground.CreateEdgeChain(
            [(-GROUND_EDGE, -GROUND_EDGE),
             (-GROUND_EDGE, GROUND_EDGE),
             (GROUND_EDGE, GROUND_EDGE),
             (GROUND_EDGE, -GROUND_EDGE),
             (-GROUND_EDGE, -GROUND_EDGE)]
             )
        # ground.CreateEdgeChain(
        #     [(0, 0), (0, GROUND_EDGE), (GROUND_EDGE, GROUND_EDGE), (GROUND_EDGE, 0),(0, 0)])

        # self.introduce_roads()

        # Initialize the rectangular bus
        rectangle_fixture = b2.b2FixtureDef(
            shape=b2.b2PolygonShape(box=(BUS_LENGTH/2, BUS_WIDTH/2)),
            density=1.5,
            friction=1.,
        )
        square_fixture = b2.b2FixtureDef(
            shape=b2.b2PolygonShape(box=(0.5, 0.5)),
            density=10,
            friction=5.,
        )

        self.body = self.world.CreateDynamicBody(
            position=self.initial_position,
            angle=self.initial_angle,
            linearVelocity=self.initial_linear_velocity,
            angularVelocity=self.initial_angular_velocity,
            fixtures=rectangle_fixture,
        )

        self.target = self.world.CreateStaticBody(
            position=target[:2],
            # angle=target[2],
            # linearVelocity=target[3:5],
            # angularVelocity=target[5],
            angle=self.initial_angle,
            linearVelocity=self.initial_linear_velocity,
            angularVelocity=self.initial_angular_velocity,
            fixtures = rectangle_fixture,
        )
        self.target.active = False
        # self.introduce_obstacles()
    
    def introduce_obstacles():
        self.obstacle1 = self.world.CreateStaticBody(
            position = [16, 15],
            angle=0,
            fixtures=square_fixture
        )

        self.obstacle2 = self.world.CreateStaticBody(
            position = [13, 10],
            angle=0,
            fixtures=square_fixture
        )

        self.obstacle3 = self.world.CreateStaticBody(
            position = [15, 25],
            angle=0,
            fixtures=square_fixture
        )
    
    def introduce_roads():
        # Introduce traffic map 
        self.traffic = Traffic()
        self.map_scale = OBS_SCALE   # map px per meters. set it to OBS_SCALE so no resizing necessary when getting observation

        contours = self.loadMap()
        num_contour = len(contours)
        print("num", num_contour)
        obstacles = []

        for contour in contours:
            vertices = []
            for item in contour:
                new_vec = b2.b2Vec2(float(item[0][0]/BOX_SCALE), float(item[0][1]/BOX_SCALE))
                vertices.append(new_vec)
            print("vertices")
            print(vertices)
            contour_shape = b2.b2PolygonShape(vertices=vertices)
            obstacle = self.world.CreateStaticBody(position=(0,0), shapes=contour_shape)
            obstacles.append(obstacle)

    def run(self):
        """
        Initiate the first time step
        """
        if self.render:
            # use the implementation in pygame_framework.py
            # which runs SimulationLoop and flip the pygame display
            # the pygame_framework.SimulationLoop links to frameworkbase.step
            super(VehicleWorld, self).run()
        else:
            self.run_next(None)

    def run_next(self, action):
        """
        Move one step forward. Call the render if applicable
        """
        dt = 1.0/fwSettings.hz
        if self.render:
            super(VehicleWorld, self).run_next(action)
        else:
            if action is not None:
                #update the velocity based on vehicle dynamics
                vel_action = self.convert_action(action)
                self.body.linearVelocity = (vel_action[0], vel_action[1])
                self.body.angularVelocity = vel_action[2]
                # # update position/state
                # pos = self.pos.copy()
                # pos[0] += self.vel[0] * dt
                # pos[1] += self.vel[1] * dt
                # pos[2] += self.vel[2] * dt
            #TODO: figure out what velocityIterations and positionIterations represent
            self.world.Step(dt, fwSettings.velocityIterations,
                            fwSettings.positionIterations)

    def convert_action(self, action):
        dt = 1.0/fwSettings.hz
        
        beta = np.arctan( self.lr*np.tan(action[1]) / self.wheelbase)
        speed = np.sqrt(self.body.linearVelocity[0]**2 + self.body.linearVelocity[1]**2) + action[0]*dt

        vel_action = [0., 0., 0.]
        vel_action[0] = speed * np.cos(self.body.angle+beta)
        vel_action[1] = speed * np.sin(self.body.angle+beta)
        vel_action[2] = speed * np.cos(beta) / self.wheelbase * np.tan(action[1])
        return vel_action


    def Step(self, settings, action):
        """
        Called upon every step
        update the agent states based on action 
        and call the world to update
        """
        #?? where to update the states [x, y, yaw],  i.e. where to put dynamics
        dt = 1.0/fwSettings.hz
        # self.body.linearVelocity += action[0]*dt
        # ?? relationship between step and run_next?
        # beta = np.arctan( self.lr*np.tan(action[1]) / self.wheelbase)
        # speed = np.sqrt(self.body.linearVelocity[0]**2 + self.body.linearVelocity[1]**2)
        # self.body.linearVelocity[0] = speed * np.cos(self.body.angle+beta)
        # self.body.linearVelocity[1] = speed * np.sin(self.body.angle+beta)
        # self.body.angularVelocity = speed * np.cos(beta) / self.wheelbase * np.tan(action[1])      
        vel_action = self.convert_action(action)
        self.body.linearVelocity = (vel_action[0], vel_action[1])  
        self.body.angularVelocity = vel_action[2]

        super(VehicleWorld, self).Step(settings)

    def reset_world(self):
        self.world.ClearForces()
        # Introduce traffic map
        self.loadMap()
        self.displayMap()

        self.body.position = self.initial_position
        self.body.angle = self.initial_angle
        self.body.linearVelocity = self.initial_linear_velocity
        self.body.angularVelocity = self.initial_angular_velocity
    

    def get_state(self):
        state = {END_EFFECTOR_POINTS: np.append(np.array(self.body.position), self.body.angle),
                 END_EFFECTOR_POINT_VELOCITIES: np.append(np.array(self.body.linearVelocity), self.body.angularVelocity)}

        return state

    def loadMap(self):
        # get random route
        route = self.traffic.randomRoute(dist=TASK_DIST, np_random=np.random.RandomState(seed=123))
        # crop map
        self.map_borders = [
            np.amin(np.array(route)[:,0]) - MAP_CLEARANCE,
            np.amax(np.array(route)[:,0]) + MAP_CLEARANCE,
            np.amin(np.array(route)[:,1]) - MAP_CLEARANCE,
            np.amax(np.array(route)[:,1]) + MAP_CLEARANCE
        ]
        map_center = ( (self.map_borders[0]+self.map_borders[1])/2, (self.map_borders[2]+self.map_borders[3])/2 )
        radius = max( map_center[0] - self.map_borders[0], map_center[1] - self.map_borders[2] )
        # self.traffic.cropMap(center=map_center, radius=radius)
        # uncomment above to show all roads instead of only the ones going to be travelled through by agent

        # create image
        img_width = int(self.map_scale*(self.map_borders[1]-self.map_borders[0]))
        img_height = int(self.map_scale*(self.map_borders[3]-self.map_borders[2]))
        self.map_state = np.zeros((img_height, img_width), dtype=np.uint8)
        # self.map_disp = np.zeros((img_height, img_width, 3), dtype=np.uint8)
        self.map_size = (img_height, img_width)

        for i in range(img_height):
            for j in range(img_width):
                self.map_state[i,j] = OUT
                # self.map_disp[i,j,:] = [0,OUT,0]

        # add roads on image
        for road in self.traffic.cropped_roads:
            for i in range(len(road)-1):
                pt0 = self._utmToIdx(road[i])
                pt1 = self._utmToIdx(road[i+1])
                print(pt0, pt1)
                # self.map_state = cv2.line(self.map_state, (pt0[1], pt0[0]), (pt1[1], pt1[0]), ROAD, int(LANE_WIDTH*2*self.map_scale))
                cv2.line(self.map_state, (pt0[1], pt0[0]), (pt1[1], pt1[0]), ROAD, int(LANE_WIDTH*2*self.map_scale))
                # self.map_disp = cv2.line(self.map_disp, (pt0[1], pt0[0]), (pt1[1], pt1[0]), (ROAD, ROAD, ROAD), int(LANE_WIDTH*2*self.map_scale))
                # cv2.line(self.map_disp, (pt0[1], pt0[0]), (pt1[1], pt1[0]), (ROAD, ROAD, ROAD), int(LANE_WIDTH*2*self.map_scale))

        cv2.imwrite("new_map.jpg", self.map_state)
        img = cv2.imread("new_map.jpg")

        # add borders around map
        for i in range(self.map_state.shape[0]):
            self.map_state[i][0] = OUT
            self.map_state[i][-1] = OUT
            # self.map_disp[i][0] = [0,0,0]
            # self.map_disp[i][-1] = [0,0,0]
        for j in range(self.map_state.shape[1]):
            self.map_state[-1][j] = OUT
            self.map_state[0][j] = OUT
            # self.map_disp[0][j] = [0,0,0]
            # self.map_disp[-1][j] = [0,0,0]

        # Try to find the contours, line -> polygon
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray map', imgray)
        cv2.waitKey(3000)
        ret, thresh = cv2.threshold(imgray, 120, 255, cv2.THRESH_BINARY_INV)  # 127
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # # Draw the original thresholded contour for comparison
        # # last para is thickness, fill the contour is it is negative, which may white the whole screen for approxPolyDP
        # cv2.drawContours(thresh0, contours, -1, (255, 0, 0), 2)
        # cv2.imshow('contour_map', thresh0)
        # cv2.imwrite("contour_map.jpg", thresh0)
        # cv2.waitKey(3000)

        num_contour = len(contours)
        print("num", num_contour)
        # Draw the approximated contour on a clear canvas
        thresh1 = np.zeros((img_height, img_width))
        approx=[]
        for contour in contours:              
            epsilon = 0.001*cv2.arcLength(contour,True)
            print("epsilon", epsilon)
            approx1 = cv2.approxPolyDP(contour,epsilon,True)
            approx.append(approx1)
            cv2.drawContours(thresh1, [approx1], -1, (255, 0, 0), 2)
            # cv2.imshow('approx1', thresh1)
            # cv2.waitKey(2000)
        # cv2.imshow('approx', thresh1)
        cv2.imwrite("approx.jpg", thresh1)
        return approx

        # # convert route from utm to index on map
        # self.route = []
        # for i in range(len(route)-1):
        #     pt0 = route[i]
        #     pt1 = route[i+1]
        #     angle = np.arctan2(pt1[1]-pt0[1],pt1[0]-pt0[0])
        #     idx = self._utmToIdx(pt0)
        #     self.route.append( [ idx[0], idx[1], angle ] )
        # idx = self._utmToIdx(pt1)
        # self.route.append( [ idx[0], idx[1], angle ] )

        # calculate other scales
        self.screen_scale = int(DISP_SCALE/self.map_scale)  # scale when displaying to screen to give the right display size
        self.obs_scale = int(OBS_SCALE/self.map_scale)      # convert obs_px per meters to obs_px per map_px

        # create copies of maps, to be shared among vehicles and updated with each vehicle occupancy per timestep
        self.map_state_shared = self.map_state.copy()
        # self.map_disp_shared = self.map_disp.copy()

        # # set origin on map
        # self.origin_on_map = (self.map_size[1]//2, self.map_size[0]//2)         # (0,0) on map

        # self.observation_size = (48, 48)

        # if self.render:
        #     self.screen_size = self.screen.get_size()
        #     self.scaled_screen_size = (self.screen_size[0]//self.screen_scale,self.screen_size[1]//self.screen_scale)

        #     # create surfaces
        #     self.screen_surf = pygame.Surface(self.scaled_screen_size)
        #     self.map_surf = pygame.surfarray.make_surface(np.transpose(self.map_disp, (1, 0, 2))) # pygame axis sequence x,y,ch
        #     self.state_surf = pygame.Surface((0.2*self.screen_size[0],self.observation_size[1]/self.observation_size[0]*0.2*self.screen_size[0]))

        #     # set screen center
        #     self._setScreenCenter((0,0))                                            # set origin as screen center
        #     self.center_on_map = (self.origin_on_map[0] + self.screen_center[0], \
        #                         self.origin_on_map[1] + self.screen_center[1])      # screen center on map
    

    # def displayMap(self):
    #     self.screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
    #     pygame.display.set_caption('Map simulator')
    #     self.screen_surf.fill(BACKGROUND)
    #     self.screen_surf.blit(self.map_surf, (0,0), \
    #                           (self.center_on_map[0]-self.scaled_screen_size[0]//2, self.center_on_map[1]-self.scaled_screen_size[1]//2, \
    #                            self.scaled_screen_size[0], self.scaled_screen_size[1]) )
    #     self.screen.blit(pygame.transform.scale(self.screen_surf, self.screen_size), (0,0))
    #     pygame.time.wait(5000)
    #     pygame.display.flip()


    # Private Methods for transformations #
    def _utmToIdx(self, utm):
        i = self.map_size[0]-1-(utm[1]-self.map_borders[2])*self.map_scale
        j = (utm[0]-self.map_borders[0])*self.map_scale
        return ( int(i), int(j) )
    
    def _idxToUtm(self, idx):
        x = idx[1] / self.map_scale + self.map_borders[0]
        y = ( self.map_size[0]-1 - idx[0] ) / self.map_scale + self.map_borders[2]
        return ( x, y )
    
    def _utmToCoords(self, utm):
        x = utm[0] - self.map_borders[0] - self.origin_on_map[0]/self.map_scale
        y = utm[1] - self.map_borders[2] - (self.map_size[0]-1-self.origin_on_map[1])/self.map_scale
        return ( x, y )
    
    def _coordsToUtm(self, coords):
        x = coords[0] + self.origin_on_map[0]/self.map_scale + self.map_borders[0]
        y = coords[1] + (self.map_size[0]-1-self.origin_on_map[1])/self.map_scale + self.map_borders[2]
        return ( x, y )

    def _coordsToIdx(self, coords):
        j = self.origin_on_map[0] + coords[0]*self.map_scale
        i = self.origin_on_map[1] - coords[1]*self.map_scale
        # clip to ensure within map
        if i < 0 or i >= self.map_size[0] or j < 0 or j >= self.map_size[1]:
            i = min(max(i,0),self.map_size[0]-1)
            j = min(max(j,0),self.map_size[1]-1)
        return ( int(i), int(j) )

    def _idxToCoords(self, idx):
        x = (idx[1] - self.origin_on_map[0]) / self.map_scale
        y = (idx[0] - self.origin_on_map[1]) / self.map_scale * -1
        return ( x, y )

    def _idxToScreen(self, idx):
        x = ( idx[1] - self.origin_on_map[0] - self.screen_center[0] + self.scaled_screen_size[0]/2 ) * self.screen_scale
        y = ( idx[0] - self.origin_on_map[1] - self.screen_center[1] + self.scaled_screen_size[1]/2 ) * self.screen_scale
        return ( int(x), int(y) )

    def _coordsToScreen(self, coords):
        x = ( coords[0]    * self.map_scale - self.screen_center[0] + self.scaled_screen_size[0]/2 ) * self.screen_scale
        y = ( coords[1]*-1 * self.map_scale - self.screen_center[1] + self.scaled_screen_size[1]/2 ) * self.screen_scale
        return ( int(x), int(y) )
    
    def _screenToCoords(self, screen):
        x = ( screen[0] / self.screen_scale - self.scaled_screen_size[0]/2 + self.screen_center[0] ) / self.map_scale
        y = ( screen[1] / self.screen_scale - self.scaled_screen_size[1]/2 + self.screen_center[0] ) / self.map_scale * -1
        return ( x, y )

    def _coordsWithinMap(self, coords):
        j = self.origin_on_map[0] + coords[0]*self.map_scale
        i = self.origin_on_map[1] - coords[1]*self.map_scale
        if i < 0 or i >= self.map_size[0] or j < 0 or j >= self.map_size[1]: return False
        else: return True
    
    def _setScreenCenter(self, coords):
        self.screen_center = [ coords[0]*self.map_scale , -1*coords[1]*self.map_scale ]
        self.center_on_map = (self.origin_on_map[0] + self.screen_center[0], self.origin_on_map[1] + self.screen_center[1])

    def _updateScreenCenter(self, coords):
        pos_on_screen = self._coordsToScreen(coords)
        if pos_on_screen[0] < SCREEN_BORDER*self.screen_size[0]:
            self.screen_center[0] -= ( SCREEN_BORDER*self.screen_size[0] - pos_on_screen[0] ) / self.screen_scale
        elif pos_on_screen[0] > (1-SCREEN_BORDER)*self.screen_size[0]:
            self.screen_center[0] += ( pos_on_screen[0] - (1-SCREEN_BORDER)*self.screen_size[0] ) / self.screen_scale
        if pos_on_screen[1] < SCREEN_BORDER*self.screen_size[1]:
            self.screen_center[1] -= ( SCREEN_BORDER*self.screen_size[1] - pos_on_screen[1] ) / self.screen_scale
        elif pos_on_screen[1] > (1-SCREEN_BORDER)*self.screen_size[1]:

            self.screen_center[1] += ( pos_on_screen[1] - (1-SCREEN_BORDER)*self.screen_size[1] ) / self.screen_scale
        self.center_on_map = (self.origin_on_map[0] + self.screen_center[0], self.origin_on_map[1] + self.screen_center[1])

