# Intern-ST
## 1.14 Settling & Literature Review
*Work*
1. [A simple car model](http://planning.cs.uiuc.edu/node658.html)
2. Kinematic and dynamic model of a vehicle from section 2 of [the thesis paper (dynamic bicycle model + path planning with rapidly-exploring random tree (RRT))](http://www.cs.cmu.edu/~motionplanning/reading/PlanningforDynamicVeh-1.pdf)
3. Kinematic and dynamic model and Control design from [the paper (kinetic bicycle model + Model Predictive Controller (MPC) ++ discretization)](https://borrelli.me.berkeley.edu/pdfpub/IV_KinematicMPC_jason.pdf)
4. Overall structure for OOP implementation from [An electric vehicle model and validation using a Nissan Leaf: A Python-based object-oriented programming approach](https://journals.sagepub.com/doi/full/10.1177/1687814018782099) <br/>
![structure of OOP vehicle](https://journals.sagepub.com/na101/home/literatum/publisher/sage/journals/content/adea/2018/adea_10_7/1687814018782099/20180719/images/medium/10.1177_1687814018782099-fig1.gif) 
5. Watch a video series about [dynamic simulation](http://apmonitor.com/do/) <br/>
 [Dynamic Modeling](http://apmonitor.com/do/index.php/Main/DynamicModeling) with sample code for simulation <br/>
 [Dynamic Estimation](https://www.youtube.com/watch?v=UTxYp0VTe-E)  <br/>
 [Dynmaic Control](https://www.youtube.com/watch?v=DFqOf5wbQtc) <br/> 
6. Try the [libbicycle repo](https://github.com/hazelnusse/libbicycle), but not successful

*Key words*
1. Pfaffian constraints:
In robot planning a set of k linearly independent constraints linear in velocity, <br/>
i.e., of the form  `A(q)dot{q}=0` <br/>
e.g. Rolling without slipping in wheeled robots.<br/>
2. Holonomic system: A system where the No. of controllable DOF = total DOF
3. Kalman filtering (mentioned as a localization technique)
4. [State-space representation](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-30-feedback-control-systems-fall-2010/lecture-notes/MIT16_30F10_lec05.pdf). <br/>
From [wikipeda](https://en.wikipedia.org/wiki/State-space_representation): In control engineering, a state-space representation is a mathematical model of a physical system as a set of input, output and state variables related by first-order differential equations or difference equations.

*Sidenotes*
1. Install PyCharm under`~/Downloads/install/pycharm..`


## 1.15 
*Work*
1. 3 DOF Bicycle model for vehicle dynamics from Chap. 2.3 of [theis paper](https://vtechworks.lib.vt.edu/bitstream/handle/10919/36615/Chapter2a.pdf)
Original book source [Optimal Vehicle Path Generator Using Optimization Methods](https://vtechworks.lib.vt.edu/handle/10919/36615)
2. Try [gekko](https://gekko.readthedocs.io/en/latest/quick_start.html) to build the model. [More examples](https://apmonitor.com/wiki/index.php/Main/GekkoPythonOptimization)
*Bug* 
`AttributeError: dt` <br/>

## 1.16
1. Debug <br/>
* `AttributeError: dt` <br/>
Soln: Any variable that is expressed as a differential in one of the equations should be an Var(), SV(), or CV(). <br/>
* `ValueError: setting an array element with a sequence.` <br/>
Soln: use `gekko_var.value[0]` instead 
* `Solution not found` <br/>
Prob: previously set the upper bound for certain variables and the limit is exceeded within given model.time <br/>
Soln: delete the limit, but haven't found ways to set the appropriate limit
2. Find the "real" literature for [bicycle model](https://scholarworks.rit.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=6924&context=theses), Chapter 4.2
3. Study emily's code of `emily_backup/simulator/simulator_gym/envs/vehicle.py`, but didn't really get it

*Key words*
1. UTM: The UTM (Universal Transverse Mercator) system

## 1.17
1. Study the Linear-quadratic regulator (LQR), [Lec19](https://ocw.mit.edu/courses/mechanical-engineering/2-154-maneuvering-and-control-of-surface-and-underwater-vehicles-13-49-fall-2004/lecture-notes/lec19.pdf) of [Maneuvering and Control of Surface and Underwater Vehicles (13.49)](https://ocw.mit.edu/courses/mechanical-engineering/2-154-maneuvering-and-control-of-surface-and-underwater-vehicles-13-49-fall-2004/lecture-notes/) [\[Full notes\]](https://ocw.mit.edu/courses/mechanical-engineering/2-154-maneuvering-and-control-of-surface-and-underwater-vehicles-13-49-fall-2004/lecture-notes/1349_notes.pdf) 
<br/>
Finish Chap 19 except for Chap19.8, proof for stability margin <br/>

Related courses: <br/>
* [MIT 6.832 Underactuated Robotics](http://underactuated.mit.edu/underactuated.html) with video lecture on [Youtube channel](https://www.youtube.com/channel/UChfUOAhz7ynELF-s_1LPpWg)
* [Stanford EE363 Linear Dynamics Systems](http://web.stanford.edu/class/ee363/lectures.html)
* [Caltech LQR compensator design](https://www.cds.caltech.edu/~murray/courses/cds110/wi06/lqr.pdf)
2. Finally understand emily's model from [Chapter 2.2 Kinematic model for later vehicle motion](https://www.academia.edu/31492223/Rajesh_Rajamani_Vehicle_Dynamics_and_Control_Mechanical_Engineering_Series.pdf). <br/>
3. Study the blog for [LQR and iLQR in ML](https://medium.com/@jonathan_hui/rl-lqr-ilqr-linear-quadratic-regulator-a5de5104c750) <br/>

**Notes:** 
* it's kinematics so you didn't find from dynamics, which follows as Chap 2.3
* You found this book before, but on sale on Springer, go Google  xxx pdf freedownload , then can find it on Academia
* Always ask your supervisor when frustrated. Don't be afraid :)

*Key words*
1. [Linear-quadratic regulator (LQR)](https://en.wikipedia.org/wiki/Linear%E2%80%93quadratic_regulator) <br/>
[video from control bootcamp](https://www.youtube.com/watch?v=1_UobILf3cc)
2. Lagrange equation [wiki](https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation) [wolfram](http://mathworld.wolfram.com/Euler-LagrangeDifferentialEquation.html)
3. [Calculus of variations](https://en.wikipedia.org/wiki/Calculus_of_variations)
4. [Lyapunov function](https://en.wikipedia.org/wiki/Lyapunov_function): used to prove stability of ODEs

## 1.18
1. Quickly finish up [iLQR](https://medium.com/@jonathan_hui/rl-lqr-ilqr-linear-quadratic-regulator-a5de5104c750)
2. [Model-based Reinforcement learning](https://michaelrzhang.github.io/model-based-rl)
3. [Guided Policy Search](https://michaelrzhang.github.io/gps)
4. Learn Visual Studio Code by following [Getting started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) <br/>
**Note:**
* In VS Code, specify a folder to start up and install packages in terminal, instead of `Settings`
5. Run Emily's code for simulator. Debug `__init__() got an unexpected keyword argument 'dtype'` <br/>
Soln: update the version of `gym` package by `pip3 install gym --upgrade`
6. Learn [Pygame API](https://realpython.com/pygame-a-primer/)
7. Learn [OpenAI-Gym](https://gym.openai.com/docs/) <br/>
![Agent-Envirionment loop](https://cdn-images-1.medium.com/max/880/0*e2hmbkTbxk3mNgfQ.)
8. Learn [simple-pycar repo](https://github.com/mdeyo/simple-pycar.git)

*Key words*
1. Differential dynamic programming (DDP): similar to iLQR but follows strictly Newton's method and expands the dynamics to second-order
2. [Bayesian linear regression](https://towardsdatascience.com/introduction-to-bayesian-linear-regression-e66e60791ea7)

*Debug*
1. `E1101:Module 'pygame' has no 'init' member`
Soln: In VS Code,
```
go to File -> Preference -> Setting
search for "pylintArgs"
add the line ` "python.linting.pylintArgs": ["--extention-pkg-whitelist=pygame"] '
```
The error should disappear <br/>
2. `Non-ASCII character '\xc2' in file `
Soln: add `# coding: utf8` at the first line of the file

## 1.21 Building/modifying the simulator
1. Follow another github repo [simulator with bicycle model](https://github.com/WesleyHsieh/gym-driving)
2. Study the codes 
```
assets/kinematic_car.py
assets/rectangle.py
assets/terrain.py
```

*Debug*
1. `No such module` while the modules are already imported from subfolders by `from <path.file> import <module>/<*>` <br/>
Soln: run with python3

*Python*
1. `assert`: suspend the program and pop out an error if the statement is false.
2. Modules and packages: [import modules from files](https://docs.python.org/3/tutorial/modules.html)
3. [super()](https://www.pythonforbeginners.com/super/working-python-super-function): is used to gain access to inherited methods – from a parent or sibling class – that has been overwritten in a class object.
4. Solve 2nd-order DE with [`odeint`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html)
5. [String formatting](https://realpython.com/python-string-formatting/)
6. [`super` with `init`](https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods)
7. ['.format'](https://pyformat.info/)

## 1.22
1. Study the code (bette to review)
```
envs/driving_env.py
envs/environment.py
examples/run_simulator.py
```
2. Go to CETRAN to collect arrow data and observe them testing
*Python*
1. [upyter and IPython](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)\
2. [__str__ VS __repr__ method](https://pythonprogramming.net/__str__-__repr__-intermediate-python-tutorial/)
3. [inheritance of classes](https://www.python-course.eu/python3_inheritance.php)

*Debug*
1. 
```
File "/home/sunardi/ruihan/gym-simulation/gym-driving/gym_driving/envs/environment.py", line 282, in step
    if acc != 0.0 and noise > 0.0:
TypeError: unorderable types: list() > float()
```
Soln: print the `noise` and it is `['gaussian', 0.1]` so change the line to `if acc != 0.0 and noise[1] > 0.0`

## 1.23
1. [Video](https://www.youtube.com/watch?v=iC2a7M9voYU) to watch <br/>
2. Study Emily's code. Reinaldo helps to run it. In home/emily folder, there's a hidder file. Run `. .env` in termial of that folder will trigger an environment with installed packages, under which navigate to emily_backup folder and run the program wiht selected model `--model xxxx` <br/>
e.g. `python3 main.py --model models/DQN.pt` <br/>
If encounter error like "AttributeError: module 'enum' has no attribute 'IntFlag'"<br/>
Soln: "Make sure that nowhere in your shell configuration files, `PYTHONPATH` is set to point to your Python 2.7 installation. You can fix it by running `unset PYTHONPATH` in terminal and then check its current value with `echo $PYTHONPATH` – for me it's now empty." <br/>
In case enconter Import Error like `ImportError: No module named 'gym.envs'`, which is because in `simulator/gym` the script for adding path in [`setup.py`](https://stackoverflow.com/questions/1471994/what-is-setup-py) `sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gym'))` was not run. <br/>
Soln: run in terminal `sudo python3 setup.py install` to go through the path-adding step and to install the required packages

*Python*
1. `time.sleep(sec)`: hang on for how many seconds; `time.ctime()`: time stamp for current time
2. `pass`: a placeholder for unimplemented mehod and so on
3. `zip` takes a bunch of lists likes
```
a: a1 a2 a3 a4 a5 a6 a7...
b: b1 b2 b3 b4 b5 b6 b7...
c: c1 c2 c3 c4 c5 c6 c7...
```
and "zips" them into one list whose entries are 3-tuples (ai, bi, ci). Imagine drawing a zipper horizontally from left to right.
4. The \*args and \*\*kwargs is a common idiom to allow arbitrary number of arguments to functions 
The \*args will give you all function parameters as a tuple:
```
In [1]: def foo(*args):
   ...:     for a in args:
   ...:         print a
   ...:         
   ...:         

In [2]: foo(1)
1


In [4]: foo(1,2,3)
1
2
3
```
The \*\*kwargs will give you all keyword arguments except for those corresponding to a formal parameter as a dictionary.
```
In [5]: def bar(**kwargs):
   ...:     for a in kwargs:
   ...:         print a, kwargs[a]
   ...:         
   ...:         

In [6]: bar(name='one', age=27)
age 27
name one
```
5. `array2d.astype`: copy the array, and cast it into a specific type.
e.g. 
```
>>> x = np.array([1,2,2.5])
>>> x
array([1.,2.,2.5])
>>>
>>> x.astype(int)
array([1,2,2])
```
6. `_` in Python:
```
Descriptive: Naming Styles
The following special forms using leading or trailing underscores are recognized (these can generally be combined with any case convention):

_single_leading_underscore: weak "internal use" indicator. E.g. from M import * does not import objects whose name starts with an underscore.

single_trailing_underscore_: used by convention to avoid conflicts with Python keyword, e.g.

Tkinter.Toplevel(master, class_='ClassName')

__double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo; see below).

__double_leading_and_trailing_underscore__: "magic" objects or attributes that live in user-controlled namespaces. E.g. __init__,  __import__ or __file__. Never invent such names; only use them as documented.
```
7. `pygame.image.load.convert_apha()`: For alpha transparency, like in .png images, use the convert_alpha() method after loading so that the image has per pixel transparency.

## 1.24 
1. [Pygame tutorial series](https://pythonprogramming.net/pygame-tutorial-moving-images-key-input/?completed=/displaying-images-pygame/)
2. Create [customized gym environment](https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa), use `sudo pip install -e .`
*Debug*
* Always put `game_init()` at the very beginning; track `env.screen` back to emily's `simulator_env.py`
* 
```
(emily_env) sunardi@sunardi:~/ruihan/simulator$ /usr/bin/python3 /home/sunardi/ruihan/simulator/simulator/main.py
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "/home/sunardi/ruihan/simulator/simulator/main.py", line 13, in <module>
    env = gym.make('VehicleSimulator-v0')
  File "/usr/local/lib/python3.5/dist-packages/gym/envs/registration.py", line 167, in make
    return registry.make(id)
  File "/usr/local/lib/python3.5/dist-packages/gym/envs/registration.py", line 119, in make
    env = spec.make()
  File "/usr/local/lib/python3.5/dist-packages/gym/envs/registration.py", line 86, in make
    env = cls(**self._kwargs)
  File "/home/sunardi/ruihan/simulator/simulator/envs/simulator_env.py", line 16, in __init__
    pygame.init()
  NameError: name 'pygame' is not defined
```
Soln: do `import pygame` in `simulator_env.py`

*Python*
1. [KDTree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html#scipy.spatial.KDTree)
2. [minkowski distance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.minkowski.html)
3. [cv2.line(img,points,color,...)](https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html#line)

## 1.25
1. Draw the basic bus on a black background with manual control
2. New reference at [PythonRobotics](https://atsushisakai.github.io/PythonRobotics/#what-is-this)

*Python*
1. [Exclude instance from a list while looping](https://stackoverflow.com/questions/24027990/how-to-exclude-an-object-from-a-list-in-python-while-looping)
2. Use `pygame.display.flip()` after each `env.screen.blit` to update the screen display

## 1.28
1. Refer to [PythonRobotics-path following](https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathTracking/model_predictive_speed_and_steer_control/model_predictive_speed_and_steer_control.py), copy and replace the linear model by bicycle model.
2. [Deep Q-Network(DQN)](https://medium.com/@jonathan_hui/rl-dqn-deep-q-network-e207751f7ae4) -- haven't finished
3. [Guided Policy Search by Sergey Levine](https://www.youtube.com/watch?v=CW1s6psByxk)
4. [End-to-End Training of Deep Visuomotor Policies](https://arxiv.org/pdf/1504.00702.pdf): "whether it is better to train teh perception system jointly with the control policy, rather than separately"
5. Bregman ADMM

*Python*
1. [`cvxpy`](https://www.cvxpy.org/tutorial/index.html) package

## 1.29 
1. Continue with [End-to-end visuomotor paper](https://arxiv.org/pdf/1504.00702.pdf)
2. [iLQG](http://maeresearch.ucsd.edu/groups/skelton/publications/weiwei_ilqg_CDC43.pdf) = iLQR + Gaussian noise 
3. [Convex optimization](https://www.youtube.com/watch?v=McLq1hEq3UY)
4. [Matlab source code for Emily's ilqr](https://www.mathworks.com/matlabcentral/fileexchange/52069-ilqg-ddp-trajectory-optimization)

*Python*
1. `x = float('Nan')` # Not a number
2. [CS231n Python Numpy tutorial](http://cs231n.github.io/python-numpy-tutorial/)
3. [Optimization for matrix computation](https://stackoverflow.com/questions/4375617/numpy-compute-x-tx-for-a-large-matrix)

## 1.30 
1. Ref from programtalk for [ilqr](https://programtalk.com/vs2/?source=python/12533/control/studywolf_control/controllers/ilqr.py) <br/>
implement it and modify accordingly
2. Write the `generate_target` method and use cubic spline to approximate smooth trajectory. Ref: [scipy.interpolate](https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html) <br/>
**Problem: it only works for increasing x, i.e. the vehicle cannot turn around.**
3. Understand the [finite difference method](http://mathworld.wolfram.com/FiniteDifference.html)


*Python*
* `plt.show` will show nothing with the `()` after `show`
* Can manually raise error like `raise ValueError ("whatever you want to say")`
* `self.__class__` returns the type (to the detail of subclass) if you call that method from a subclass instance.
```
class Foo(object):
    def create_new(self):
        return self.__class__()
class Bar(Foo):
    pass
b = Bar()
c = b.create_new()
print type(c)  # We got an instance of Bar
```
* [`numpy.tile(A, reps)`](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.tile.html) Construct an array by repeating A the number of times given by reps.

## 1.31
1. Code and debug
2. Try [LQR wrapper](http://www.mwm.im/lqr-controllers-with-python/]

*Python*
1. Multiply elements in a list / an array, cannot use `array\*3` (which means copying), but <br/>
`my_list = [1, 2, 3, 4, 5]
 my_new_list = \[i * 5 for i in my_list\]`
 2. [How to create a new instance from a class object in Python](https://stackoverflow.com/questions/5924879/how-to-create-a-new-instance-from-a-class-object-in-python)
 3. [NumPy array initialization (fill with identical values)](https://stackoverflow.com/questions/5891410/numpy-array-initialization-fill-with-identical-values)  Use `np.full()`
 4. matplot pause
 ```
plt.show(block=False)
plt.pause(3)
plt.close()
```
5. [`np.wxpand_dims`](https://docs.scipy.org/doc/numpy-1.9.0/reference/generated/numpy.expand_dims.html)
6. [`np.newaxis`](https://stackoverflow.com/questions/29241056/how-does-numpy-newaxis-work-and-when-to-use-it)
 
 *Debug*
 * `Error: 'float' object does not support item assignment` <br/>
 Soln: [double check assignment](https://stackoverflow.com/questions/39627259/error-float-object-does-not-support-item-assignment)

## 2.1
1. Draw the silly trajectory on gym
2. Ref for [ilqr example with drake wrapper coding in c++](https://github.com/RobotLocomotion/drake)
3. [Underactuated Robotics](http://underactuated.mit.edu/underactuated.html) and its [balancing ilqr example github](https://github.com/RussTedrake/underactuated/blob/master/src/acrobot/balancing_lqr.py)
4. [1D ilqr -- pylqr](https://github.com/navigator8972/pylqr/blob/master/pylqr_test.py)
5. [`Condition number`](https://en.wikipedia.org/wiki/Condition_number): In the field of numerical analysis, the condition number of a function with respect to an argument measures how much the output value of the function can change for a small change in the input argument. This is used to measure how sensitive a function is to changes or errors in the input, and how much error in the output results from an error in the input.

*Debug*
* `Cannot find a finite solution` in LQR <br/>
Soln: modify the matrix parametes, especially B

*MatLab* 
1. [`deal`](https://www.mathworks.com/help/matlab/ref/deal.html): basically is `copy`
2. `fliplr(cumsum(fliplr()))` cumulatively add backwards from the end

*Python*
1.[`pygame.time`](https://www.pygame.org/docs/ref/time.html)
2. [`pygame.draw.lines`](https://www.pygame.org/docs/ref/draw.html)
3. [`scipy.linalg.solve_discrete_are`](https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.linalg.solve_discrete_are.html)

## 2.11
1. Make use of pylqr, trajctrl. Need to see how to interpret the meaning of `res` from synthesize_trajectory and define short horizon, "piece-wise" solution

*Debug*
```
File "/home/sunardi/ruihan/pylqr/pylqr.py", line 359, in build_lqr_system
    np.tile(cu1, (len(x), 1)).T - np.tile(cu2, (len(x), 1)).T
ValueError: operands could not be broadcast together with shapes (2,4,1) (2,4)
```
Solution: add `# instant_cost = instant_cost[0]` for `else` statement in instantaneous_cost method

* `IndexError: list assignment index out of range` when using <br/>
```
ref_traj = []
for i in range(len(cx)):
    ref_traj[i] = np.array([cx[i], cy[i], cyaw[i], CONST_SPEED])
```
Soln: 
`ref_traj` is an empty list, but you're attempting to write to element [0] in the first iteration, which doesn't exist yet. Reportde as `IndexError: list assignment index out of range`
```
for i in range(len(cx)):
    ref_traj.append(np.array([cx[i], cy[i], cyaw[i], CONST_SPEED]))
 ```

*Python*
* 'None list' <=> 'Nan value array'
* To convert a list to an array, can use `np.array(mylist)`
* [Underscore in Python](https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc)

## 2.12 
1. Problem with pylqr: <br/>
* Low speed for calculating each iteration
* The syn_traj does not work in gym environment. E.g. only finish 1/10 of the whole path after 1000 steps
* The path cannot follow exactly even in original matplot 
* The state is \[x,y\], no yaw angle
* haven't use bicycle model, just take the A,B matrices as it was
* Most IMPT problem: it is actually LQR, without iteration over timestep

2. Problem with Emily's Matlab-based code 
* Need to implement dynamics func (easy)
* Don't understand the backpass and the boxQP inside backpass (hard)
3. Discussion with Reinaldo
4. [iLQR algorithm from studywolf](https://studywolf.wordpress.com/2016/02/03/the-iterative-linear-quadratic-regulator-method/)
5. Move to Studywolf's ilqr code
6. Modify Studywolf's code into `myilqr.py` and modify `vehicle.py` to apply 6D states.
7. Related: [line search](https://en.wikipedia.org/wiki/Backtracking_line_search)
8. ilqr is one wat to implement MPC (Model Predicative Control)
9. [BoxQP](https://domino.research.ibm.com/library/cyberdig.nsf/papers/02EEF0AC3CBD415085257FDC00545444/$File/rc25612.pdf): extension from Matlab ilqr code
10. [Compare two files in Sublime Text](https://stackoverflow.com/questions/25874018/comparing-the-contents-of-two-files-in-sublime-text)


*Pyhton*
* [How to multiply individual elements of a list with a number?](https://stackoverflow.com/questions/8194959/how-to-multiply-individual-elements-of-a-list-with-a-number)
* [TypeError: unsupported operand type(s) for -: 'list' and 'list'](https://stackoverflow.com/questions/26685679/typeerror-unsupported-operand-types-for-list-and-list)

## 2.13
1. Debug the ilqr code
* change`dof` to `num_action = self.m` for dimension of differential cost about u; `self.veh.DOF` remains unchanged
2. The code runs but it is not working at all. The actions are not updated by ilqr
3. [drake controller in c++](https://drake.mit.edu/doxygen_cxx/group__control__systems.html#ga70a9177e4ce3145f156da077fb1613b3)
4. Use [pydrake wrapper](https://drake.mit.edu/python_bindings.html), must use python2.7 for pydrake. <br/>
Rewrite the file and compare pydrake with [Mark's dlqr](http://www.mwm.im/lqr-controllers-with-python/). <br/>
Manually perform partial differentiation for [Ref for dynamic bicycle model](file:///home/sunardi/Downloads/9781461414322-c1%20(1).pdf) and get the model_based A, B matrices, feed A and B into LQR function. <br/>
Firstly got different K values. Solution: In pydrake, change `LinearQuadraticRegulator` to `DiscreteTimeLinearQuadraticRegulator`. Then the values conform, which means can use dlqr and python3. <br/>
5. Caltech slides of algorithm for [LQR for Trajectory planning](http://www.cds.caltech.edu/~murray/courses/cds110/wi06/L2-1_LQR.pdf). <br/>
After getting K values, u = K\*x. Move on to see trajectory planning, need to see piece-wise linearization.

*Debug*
* `ValueError: only 2 non-keyword arguments accepted` <br/>
soln: `np.array([ your lists ])` add square bracket inside
* For `np.zeros(int, dof, int)` where `dof`= `int/2`, get error `typeerror 'float' object cannot be interpreted as an integer` <br/>
Soln:Looks like `reshape`/`np.zeros` is expecting an integer, but it gets a float because Python 3 does not auto convert floats to integers in division unless you use `//`. Change to `dof = int//2`
* After installing pydrake and change interpreter to python2.7(/usr/bin), error 'no such module `pydrake`' still occurs <br/>
Soln: run the code in terminal, not visual studio. Do not anyhow install pydrake in usr or whatever

*Linux*
* To run a script of commands, just call it int terminal. If fails, add sudo at the beginning. >br/<
e.g. `sudo /opt/drake/share/drake/setup/install_prereqs`

## 2.14
*To do*
1. Generate a trajectory based on 6D state [x y v beta theta thetadot].
2. use algo in 2.13.5

*Python*
* numpy.ravel(a, order='C')[source](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.ravel.html)turn a contiguous flattened array.
* matrices multiplication <br/>
use `np.dot(A, B)` or `A.dot(B)`, not `A*B` <br/>
multiple matrices, can use `A.dot(B.dot(C))` or [`np.linalg.multidot([A,B,C])`](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.linalg.multi_dot.html)

*
## 2.15 
0. [ref for bicycle model used in dlqr, see p25](file:///home/sunardi/Downloads/9781461414322-c1%20(1).pdf)
1. Modify the program, using error terms err_x, err_u following P32 of [EE363] notes(http://web.stanford.edu/class/ee363/lectures/dlqr.pdf)
2. To get A, B changed at each timestep, put `self.u[t] = self.u[t] + self.err_u[t]` inside the forward pass loop of ilqr
3. [1D dynamic programming](https://github.com/tnaduc/Dyanmic_Programing_Linear_Dynamical_System/blob/master/DP_1.ipynb)
4. [ilqr anassiator](https://github.com/anassinator/ilqr)
*Debug* 
Error:The bus kept rotating, not moving straight. <br/>
Soln: modify the bus.display method, change the variable representing the yaw angle from `self.states[2]` to `self.states[4]`
*Python*
* [np.nan_to_num](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.nan_to_num.html)

## 2.18
1. LQR vs MPC: The main differences between MPC and LQR are that LQR optimizes in a fixed time window (horizon) whereas MPC optimizes in a receding time window, and that a new solution is computed often whereas LQR uses the single (optimal) solution for the whole time horizon.
2. Implement [Python Robotics](https://github.com/AtsushiSakai/PythonRobotics) and **it works!!!!** <br/>
Add tehe `get_linear_model_matrix_bicycle` method., with reference to [Vehicle Model Linearization](https://pythonrobotics.readthedocs.io/en/latest/modules/path_tracking.html#vehicle-model-linearization). <br/>
The *C* term helps a lot to reduce the steady-state error but the bicycle model cannot drive backwards for the "switch back course", jsut stucking there.
3. Create virvual environment in terminal: `conda command not found`
```
do in the directory that shows "conda command not found", not the installation direcrory
for anaconda 2 :

export PATH=~/anaconda2/bin:$PATH
for anaconda 3 :

export PATH=~/anaconda3/bin:$PATH
for anaconda 4 :

Use the Anaconda Prompt

and then

conda --version  
to confirm that it worked.
```
[install conda](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04)
4. Discussion with Reinaldo for the next step, probabilistic guided policy search. I.e. p(u|x) & p(x_t+1|x_t. u_t). Ref: [Talk by Sergey, 19:14/21:53](https://www.youtube.com/watch?v=CW1s6psByxk)
5. New concepts: inverse reinforcement learning [Ref 1](https://thegradient.pub/learning-from-humans-what-is-inverse-reinforcement-learning/)[ Ref 2](https://towardsdatascience.com/inverse-reinforcement-learning-6453b7cdc90d)

*Debug*
* `typeError: 'builtin_function_or_method' object is not subscriptable ` <br/>
Solution: when initialize the np.array, change `A = np.array[1., 0.]` to `A = np.array([1., 0.])`

## 2.19
1. Reading: <br/>
[RL - Model based reinforcement learning](https://medium.com/@jonathan_hui/rl-model-based-reinforcement-learning-3c2b6f0aa323) <br/>
[Dynamic Programming notes](https://web.stanford.edu/class/cs97si/04-dynamic-programming.pdf) <br/>
Materials <br/>
PILCO — Probabilistic Inference for Learning COntrol [paper](http://mlg.eng.cam.ac.uk/pub/pdf/DeiRas11.pdf) [video&code](http://mlg.eng.cam.ac.uk/pilco/) <br/>
CS 294-112 UC Berkeley Deep Reinforcement Learning [course website](http://rail.eecs.berkeley.edu/deeprlcourse/) [video channel](https://www.youtube.com/playlist?list=PLkFD6_40KJIxJMR-j5A1mkxK26gh_qg37) Finish Lec 11&12 <br/>
To read: <br/>
[Dynamic programming in Python (Reinforcement Learning)](https://medium.com/harder-choices/dynamic-programming-in-python-reinforcement-learning-bb288d95288f) <br/>
[small DP exercise with Python](http://interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html)

## 2.20
1. Guided Policy Search by Berkeley. [paper](https://graphics.stanford.edu/projects/gpspaper/gps_full.pdf) [code](https://github.com/cbfinn/gps)
2. [ROS](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment): rospy, subscriber, publisher, callback(processing and decoding); compatible with c++ and python. **Follow up later** <br/>
Failed the installation with CMake Error. <br/>
Read tutorials until [Building Packages](http://wiki.ros.org/ROS/Tutorials/BuildingPackages) <br/>
For installation, use ROS kinetic instead of ROS Indigo for Ubuntu 16.04, "normally choose 2 version before the latest which enough many people use and support"


## 2.21
*Reading*
1. Partially Observable Markov Decision Process (POMDP) [video](https://www.youtube.com/watch?v=-q61H11Lm0s)
2. [End-to-end visumotor paper](https://arxiv.org/pdf/1504.00702.pdf)

*Python*
* threading — [Thread-based parallelism](https://docs.python.org/3/library/threading.html#module-threading)
* sample code to use PyTorch to calculate KL Divergence <br/>
`err2 = torch.log(F.softmax(a)) - F.log_softmax(b)`

## 2.22
1. Try to write `agent_vehicle.py`
2. 

*Python*
* [\"Google Protocol buffer\"](https://developers.google.com/protocol-buffers/docs/overview):  a flexible, efficient, automated mechanism for serializing structured data – think XML, but smaller, faster, and simpler.
* PyBox2D [manual](https://github.com/pybox2d/pybox2d/wiki/manual), similar to gym environment
* [More for import](https://docs.python.org/3/library/imp.html)  `imp.load_source` is used in [gps]((https://github.com/cbfinn/gps))
* Additional defaults may be passed into the get() method which will override all others. <br/>
[`ConfigParser.get(section, option[, raw[, vars]])`](https://docs.python.org/2/library/configparser.html):Get an option value for the named section. If vars is provided, it must be a dictionary. The option is looked up in vars (if provided), section, and in defaults in that order.
* [`string.split`](https://www.w3schools.com/python/ref_string_split.asp): `str.splilt(separator, max)`
* [datetime](https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior)

*Others*
* hotkey for Sublime. `Alt+shit+2` for splitting the window/pane

## 2.25
*Reading*
1. [Differences between the L1-norm and the L2-norm (Least Absolute Deviations and Least Squares)](http://www.chioka.in/differences-between-the-l1-norm-and-the-l2-norm-least-absolute-deviations-and-least-squares/)
2. Study the `cost` folder and `box2d` body. <br/>
Reinaldo help with debugging. <br/>
Error: the bus stays at origin and doesn't move. <br/>
I have tried: modify the action part, trying to find where the position is updated. Find the built-in function b2World.step does that.
```
Step( $timeStep, $velocityIterations, $positionIterations )
Take a time step. This performs collision detection, integration, and constraint solution.

Parameters:
float32 $timeStep - the amount of time to simulate, this should not vary.
int32 $velocityIterations - for the velocity constraint solver.
int32 $positionIterations - for the position constraint solver.
```
Reinaldo helps to : check basic syntax error; add `+action[0]*dt` to the speed update. and it WORKS!
3. The sample GPS works for the vehicle model in a sense that the driving behavior looks like a bus. 
4. Study the `gui` folder. The `mean-cost` plot is also modified in `gui.mean_plotter.py >> __init__ (min_iter)` to display the cost for more than 10 trials.
5. TODO: it's only one target now, and not in gym environment. See how to perform path tracking and embed it in gym environment.
6. TODO: the target will somehow move after some iterations. Check that condition.
7. TODO: Figure out the z-coord of GPS plot.
8. TODO: try to add obstacles on the way to test the strategy.

*Python*
* [Abstract classes](https://www.python-course.eu/python3_abstract_classes.php). An abstract method is a method that is declared, but contains no implementation, which can be implemented in subclass, but not necessary.

*Others*
* Error: IndentationError: unindent does not match any outer indentation level <br/>
For Sublime Text users:
Set Sublime Text to use tabs for indentation: View --> Indentation --> Convert Indentation to Tabs
Uncheck the Indent Using Spaces option as well in the same sub-menu above. This will immediately resolve this issue.

## 2.26
1. Solve for 2.25.6. The target moves because it is a dynamicbody, which has collsion. Fix it by changing it into StaticBody.
2. Solve for 2.25.7. Based on `gps_training_gui.py >> calculate_3d_axis_limits()`, the x, y, z are 3D ECND_EFFECTOR_POSTION, respectively, i.e. x, y, yaw.
3. Solve for 2.25.8. Add one and more obstacles. The strategy can be learnt to avoid obstacles, but need to re-learn once the obstacle changes. Differentiate the target and the obstacles by setting `self.target.active = False ` in `vehicle_world.py` so that the traget does not participate in any collision/dynamics (just a marking there).
4. To make compatible files, copy emily's `traffic.py`, and copy the `loadMap` function. <br/>
Need to convert python3 to python2 syntax.<br/>
* `FileNotFoundError` in python3 <=> `IOError` in python2
```
from __future__ import print_function

import os
import errno

try:
    open('no file of this name')   # generate 'file not found error'
except EnvironmentError as e:      # OSError or IOError...
    print(os.strerror(e.errno)) 
```
Or just use IOError in the same way:
```
try:
    open('/Users/test/Documents/test')   # will be a permission error
except IOError as e:
    print(os.strerror(e.errno))  
```
* `import pickle` in python3 <=> `import cPickle as pickle` in python2 <br/>
The default protocol changes with the file type. Need to convert the pickle file if it is dumped by pickle in python3. <br/>
```
Read in python3 and save it as python2 format
#!/usr/bin/env python3
import pickle
with open("a.pkl", "rb") as f:
    w = pickle.load(f)

pickle.dump(w, open("a_py2.pkl","wb"), protocol=2)
Then you can load a_py2.pkl in python2.
```

*Python*
* [`numpy.r`](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.r_.html) Translates slice objects to concatenation along the first axis, a simple way to build up arrays quickly. 
* To modify the default version of Python, 
```
gedit ~/.bashrc
in the file add "alias python=python3" or "alias pyhton3 = 3.5" 
no space on the left and right side of "="
save the file
source /.bashrc
check by "python --version"
```

*Debug*
* `No module named Caffe`: need to `make all` for Caffe [Full installation guide for Caffe](https://github.com/yixindu1573/Caffe-Installation-Ubuntu-16.04-cuda-9.0-cudnn-v7)
* `install caffe fatal error: hdf5.h: No such file or directory compilation terminated.`
```
To get the build to pass on Debian Jessie, I had to (in addition to the above)
1. modify `INCLUDE_DIRS` in `Makefile.config`
   INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/
   e.g.
   PYTHON_INCLUDE := /usr/include/python2.7 \
		         /usr/lib/python2.7/dist-packages/numpy/core/include \
		         /usr/local/include \
		         /usr/include/hdf5/serial/
2. create symlinks as instructed [here](https://github.com/NVIDIA/DIGITS/issues/156)
   cd /usr/lib/x86_64-linux-gnu
   sudo ln -s libhdf5_serial.so.8.0.2 libhdf5.so
   sudo ln -s libhdf5_serial_hl.so.8.0.2 libhdf5_hl.so
   
3. Work around #337 by installing `g++-4.6` from the Wheezy repo and adding to `Makefile.config`:
   CUSTOM_CXX := g++-4.6
```
* `libgcc` is for anaconda: 'Shared libraries for the GNU Compiler Collection', not necessary for Caffe. The actual installation at [step7]((https://github.com/yixindu1573/Caffe-Installation-Ubuntu-16.04-cuda-9.0-cudnn-v7)) Build Caffe   `echo 'export PYTHONPATH=$CAFFE_ROOT/python:$PYTHONPATH' >> ~/.bashrc`
4. To check opencv version in ubuntu terminal ` dpkg -l | grep libopencv`
5. `ImportError: No module named PySide` <br>
Soln: `sudo apt-get install python3-pyside` for Python3
6. Error: `'dict' object has no attribute 'iteritems' ` <br/>
Soln: As you are in python3 , use dict.items() instead of dict.iteritems(). <br/>
Removed dict.iteritems(), dict.iterkeys(), and dict.itervalues().
Instead: use dict.items(), dict.keys(), and dict.values() respectively.

## 2.27
1. Try to use the emily's `loadMap` adn `displayMap` and draw the map on box2D world with road and obstacle.
2. Draw the parts that are not road as polygon. use `cv2.findContours` method <br/>
The contour is not smooth and contains so many points that exceeds the `drawPolygon` limit 
3. TODO:smooth the contour. 

*Python*
* pygame.time.wait(ms) to halt th program
* working with [images with Opencv](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html)
* [opencv image thresholding](https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html)
* [output formatting](https://www.python-course.eu/python3_formatted_output.php)

*Debug*
* 
```
File "python/gps/agent/box2d/vehicle_world.py", line 289, in loadMap
    print(self.map_state.shape())
AttributeError: 'NoneType' object has no attribute 'shape'
```
Find that `cv2.line` output is Nonetype. <br/>
Trying to run emily's code to see what the funtion output should be. Not sure why she could return to map_state, but it also works without return
* Somehow need to reinstall `torch` fro python3.5 or `pygame` for python3.6. Install `torch` and run her program.
* somehow the `map_state`appears as `tuple` not array, so struggling a bit with that.When restart the program, it is okay.
* opencv findContour ValueError: need more than 2 values to unpack <br/>
In OpenCV 2, findContours returns just two values, contours and hierarchy. The error occurs when python tries to assign those two values to the three names given on left in this statement: <br/>
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) <br/>
while opencv3 returns three values, without modifying the original image
* ValueError: Failed on kwargs for b2PolygonShape.vertices: Expected tuple or list of length >= 2 and less than b2_maxPolygonVertices=16, got length 1004. <br/>
Soln: try to reduce the number of waypoints by smoothening the contour. <br/>
Try [approxPolyDP](https://stackoverflow.com/questions/41879315/opencv-using-cv2-approxpolydp-correctly) and [spline in interpolate](https://agniva.me/scipy/2016/10/25/contour-smoothing.html) [affect of differetn epsilon](https://stackoverflow.com/questions/11925777/opencv-how-to-use-arrays-of-points-for-smoothing-and-sampling-contours)<br/>
[contour property](https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html)

*Others*
* Hot key for a clean window in terminal `ctrl + L` 

## 2.28 
1. Solve 2.27.3, reduce the epsilon to `epsilon = 0.001*cv2.arcLength(contour,True)` and draw contour in a clear canvas so that will not be confused with original contour.
2. Draw the approximated contour for each one in `contours` and return the list `approx` instead of `[approx1]`
3. When pass back to box2D, encounter `TypeError: in method 'new_b2Vec2', argument 1 of type 'float32'`. <br/>
Use `new_vec = b2.b2Vec2(float(point_x), float(point_y))` to convert.
4. Try to divide the road into tiles, and draw on the box2d screen

*Python*
* a.astype(float32) generates ndarray, better to use float(a) to get correct datatype for `b2newVec2` method


## 3.1
1. rewrite the `divideRoute` method. **Note: think about what to do, how to do, then just do it**
2. create `BusWorld`, `agent_bus`
3. figure out the coordinates of box2d and find the configuration of pygame scale. finally draw the map (without cropping) in box2d environment

*Debug*
* `TypeError: __init__() takes no arguments (1 given)` <br/>
Soln: You need to add the default self parameter to __init__:   `def __init__(self):`
* `usage: new_gps.py [-h] [-r N] [-s] [-q] new_gps.py: error: unrecognized arguments: box2d_bus_example` <br/>
Soln: if you want to specify it when you run it, you need to parse the parameter `parser.add_argument('experiment', type=str, help='experiment name')` even if it is known. 
* 
```
File "python/gps/new_gps.py", line 337, in get_policy
    hyperparams.config.agent.target_state = endpoint
AttributeError: 'dict' object has no attribute 'agent'
``` 
Python syntax problem. Change `hyperparams.config.agent.target_state = endpoint` to `hyperparams.config['agent']['target_state'] = endpoint`
* `NameError: name 'self' is not defined` <br/>
Soln:the parameters must include `self` when you define a method, including `__init__` method
* `IndentationError: unexpected indent. ` <br/>
Try to justify first. If constantly encounter the error, reopen the program in Sublime Text and do `convert indentation to tab`

*Others*
* Hot key in Visual Studio Code, `Ctrl + Shift + F` to find in all files.
* crop an image by OpenCV in python: `crop_img = img[y:y+h, x:x+w].copy() `

## 3.4
1. The polygon in box2d does not match the polygons in opencv2. Try to increase the lane width and find that it is because box2d does not accept concave polygons. <br/>
Soln: find a souce code to perform [triangulation](https://www.emanueleferonato.com/2011/09/12/create-non-convex-complex-shapes-with-box2d/). 

## 3.5
1. Also try [Mark Keil's Algo](https://mpen.ca/406/keil) for [polygon decomposition](https://mpen.ca/406/overview), though half-way.
2. see a bit for c++ -> python wrapper[documentation](https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/c++-wrapping.html) [Boost.Python](https://www.boost.org/doc/libs/1_49_0/libs/python/doc/)
3. Go back to [triangulation](https://www.emanueleferonato.com/2011/09/12/create-non-convex-complex-shapes-with-box2d/), but encouter errors. <br/>
'error 2': ot in clockwise order. Because of the opencv coord, the direction is opposite to what we see. <br/>
'error 0': but still return None for v, `if b1 and b2`, does not hold, so `h` is never assigned

*Debug*
* TypeError: 'float' object has no attribute '__getitem__' <br/>
Problem: may have applied index to a float number instead of a list/array

## 3.6
1. Continue with polygon decomposition. Rei has given nice algo (dived-and conquer), and try to realize it. The general flow in `to_convex(poly)` and several helper function. <br/>
Finally get it working for the current road case. <br/>
But still leave with problems: narrow lane length will introduce more complex concave road shape, and the algorithm may not work. Need to introduce checking mechanism. e.g. lane width 20 -> 8
2. Modify the `bus_world` so that we iterate each polygon and get the total complex polygon list
3. set a target and increase the iterations of GPS. <br/>
Problem: The body and target positions are not properly converted. Use manual setting now to see whether GPS works for our case first.
4. Trying to understand the [triangulation](https://www.emanueleferonato.com/2011/09/12/create-non-convex-complex-shapes-with-box2d/) code based on [Ray-segment intersection](https://rootllama.wordpress.com/2014/06/20/ray-line-segment-intersection-test-in-2d/)  <br/>
The `hitRay` function returns the possible intersection of a ray and a line segment. However, it does not return `True` when pt2 seems to be a reflex point <br/>
e.g. `('hitRay', array([460, 285]), array([448, 258]), array([123,   1]), array([460,   1]), None)` <br/>
and I get different calculation from it.

*Python*
* [For list](https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists/11520540), <br/>
`remove` removes the first matching value, not a specific index; <br/>
`del` removes the item at a specific index; <br/>
`pop` removes the item at a specific index and returns it <br/>
for [nd array -> delete](https://docs.scipy.org/doc/numpy/reference/generated/numpy.delete.html) <br/>
It returns a copy of arr with the elements specified by obj removed. Note that delete does not occur in-place. so need to use `new_arr = np.delete(arr, obj)` rather than `arr.delete()` which will give an error like "ndarray doesn't have attribute delete"
* use of `any` and `all` to check elements in a list <br/>
e.g. `any(item[2] == 0 for item in items)` `all(item[2] == 0 for item in items)`, which return a boolean
* [`numpy.isin`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isin.html)

## 3.7
1. Problem: in simulation with even longer horizon, e.g. 8000, the bus will be stuck in the middle and stays there.
2. try to understand more about the GPS, and check the experiment setting in papers

## 3.8
1. Try to cut the map
2. Fix the bug that the road and route do not correspond to each other. Firstly change `route.append` to `road.append`, then realize that road and route index are different. one route consist of several roads, and the directions are not necessarily consistent. so change back to `route.append`.
3. find that x, y axes were accidentally swapped. change them back and do some geometric transformation.
4. Draw the ground box, with position `[0, 0]`; others have position `[-map_width/2, -map_height/2 ]`
5. learn from Rei's perception part. homography & perspective <br/>
intrinsic (internal error, like sitortion) using checkboard & extrinsic (exernal error, such as installation position) calibration of lidar <br/>
learn point match algo and code <br/>
Rei uses division of quadrants and line fitting to deploy the two-stick X tool for calibration

## 3.11
*To Do*
1. Last time, the bus can go some distance but cannot reach the target yet. so try to reduce the distance/increase the horizon until it can go to the target without any collosion
2. Try to concatenate the tiles so that the bus can cover the whole route
3. extract the image and corresponding GPS local policy

*Do*
1. Yes, it can go to the target without any collision but will also go beyond. A good horizon is required.

*Python*
* [Python multithread programming](https://www.tutorialspoint.com/python/python_multithreading.htm)  [documentation](https://docs.python.org/2/library/threading.html)
* [semaphore](https://en.wikipedia.org/wiki/Semaphore_(programming), a variable or abstract data type to control the access to the common resources by multiple processes in a concurrent system.

## 3.12
1. Make the loop works, with checking conditions(whether the target is reached or not) and updated target
2. Geometries again for converting the `final_pos` in box2D into corresponding pos in route/opencv sys.
3. Extract the GPS trajectory `U`

*Python*
* `os._exit` calls the C function `_exit()` which does an immediate program termination. Note the statement "can never return". <br/>
`sys.exit()` is identical to raise `SystemExit()`. It raises a Python exception which may be caught by the caller.
* `range`: if you wanted to count from last to posn you would use `range(last, posn - 1, -1)`
* [Threading](https://www.novixys.com/blog/python-threading-tutorial/#4_Using_a_Lambda_as_the_Task_Function) <br/>
[Thread and queue](https://www.shanelynn.ie/using-python-threading-for-multiple-results-queue/)

*Debug*
* When I try to concatenate different tiles, the GUI halts there. Tried to look into thread, but it is actully `plt.ioff`, `plt.show()` that halt the program.
* `'list' object has no attribute 'shape'`: `print(np.asarray(mylist).shape())`
* [`'instancemethod' object has no attribute '__getitem__' with class variables`](https://stackoverflow.com/questions/21365521/instancemethod-object-has-no-attribute-getitem-with-class-variables): unsure hwo to solve
* [`TypeError: 'NoneType' object has no attribute '__getitem__'`]: The error means you tried to do something like `None[5]`, check how you assigned value to the array

## 3.13
*Resources*
[CMU-OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)

*To Do*
1. cut the map per tile, as Emily did
2. see how to save the action, e.g. in csv? => np.save
3. Try testing the policy, compare learning from traj and from policy
4. after cutting map, save the image
convert to gymj environment first. either redo all the winodw things, or redo the drawing/cutting map

*Python*
* [deepcopy and shallow copy] (https://www.python-course.eu/deep_copy.php)
* [Python assert statement](https://www.programiz.com/python-programming/assert-statement): Assertions are simply boolean expressions that checks if the conditions return true or not. <br/>
Syntax: `assert <condition>` or `assert condition, <error message>`
* To concatenate a list of arrays into one single array, use [`numpy.concatenate`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html) <br/>
or [`numpy.stack`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.stack.html), if each array must have the same shape.
* save a list of arrays, use [`numpy.save`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.save.html)
```
 import numpy as np
  np.save('testnp.npy', [[2,3,4],[1,2]])
  np.load('testnp.npy')
 ```

*Other*
* visual studio code hotkey: Zoom in `Ctrl =`, zoom out `Ctrl -`

## 3.14
1. concatenate the tiles of map

*Debug*
* Problem: the bus will reach the target faster with more iterations, but will also quickly deviate from the route since no future target is provided. <br/>
Soln: limit the number of iterations, 15 for now <br/>
Once the bus reaches the target, save that sample and return from that iteration. Cannot return immediately due to fixed horizon but it works when an iteration is done. <br/>
if `sorry, not hit`, find the nearest point to return, and adjust the weight for angle error. <br/>
Becasue we return from the very first iteration that hits the target, it is generally slow. Can add velocity limit later so that only return when it is smart enough to learn the way and to gain speed as well.
* adjust the order of map_width and map_height
* Problem: sometimes the bus cannot reach the next target and deviates <br/>
Soln: write `insertroute` to insert more waypoints per `COVER_TILE` distance. 
* Problem: there are some obtrusive points in the original route that suddenly change direction <br/>
Soln: check the angle difference between adjacent point, and omit the point from the route if its angles diviates a lot from the previous point
* Problem: after excluding the points, somewhere will be empty. <br/>
Soln: adjust the logic a bit and interchange the order of "inserting point" and "excluding obtrusive points", i.e. use the position info to insert midway points first and then delete obtrusive points.
* The polygon algo works for certain lane width, for current map, LANE_WIDTH >=14

* Problem: extend to 40 waypoints, and the bus will stuck at the U-turn <br/>
Possible soln: try fine-tune that part of the route or make use of the policy (brain/experience) gained in previous route

## 3.15
1. Try to solve the problem of the bus hitting the wall, such as insert more waypoints in the map based on the yaw difference, and only return finishing sample with certain velocity so that won't return those stuck states
2. Chit chat with managers. Stay with engineering
3. See Yan's "handing over" CUDA stuff, [reduction](https://raw.githubusercontent.com/mateuszbuda/GPUExample/master/reduce1.png) (sum up an array in an efficient way)
4. Discuss with Rei, some rational/psychological concern of human driving 

## 3.18
1. Continue with trying gps. Hitting the wall at about 60 steps, probably due to the angle setting. <br/>
Later found out that it is because although the bus is simulated to be stuck at about 40 steps, I still save the actions. With the walls rendered in box2d, it happened to appear like that the bus can "roughly" follow the rest steps, but actually not. Once the walls are removed, teh first40 steps can still follow, the rest are just go straight and then circle around, making no sense.
2. [Paper about occupancy map ](https://arxiv.org/pdf/1812.03079.pdf) <br/>
"We augment the imitation loss with lossesthat discourage bad behavior and encourage progress, and, importantly, augment our data with synthesized perturbations in the driving trajectory. These expose the model to nonexpert behavior such as collisions and off-road driving, and inform the added losses, teaching the model to avoid these behaviors. Note that the opportunity to synthesize this data comes from the mid-level input-output representations (a top-down representation of the environment and intended route, where objects such as vehicles are drawn as oriented 2D boxes along with a rendering of the road information and traffic light states), as perturbations would be difficult to generate with either raw sensor input or direct controller outputs." <br/>
useful in terms of: <br/>
* occupancy map with the agent always in a certain point (u0,v0) but not center, facing +-25 degrees rather than straight in front to aviod bias to always go vertically up
* take reference for the combination of different kinds of cost, i.e. imitation loss and environment loss
```
Overall, our losses may be grouped into two sub-groups, the imitation losses:
Limit = {Lp,LB,Lθ,Lp−subpixel,Lspeed} (13)
and the environment losses:
Lenv = {Lcollision,Lonroad,Lgeom,Lobjects,Lroad} (14)
```
3. Try to add the collision cost term in algorithm

## 3.19
1. Analyze the configuration dictionary and hard code to pass the map_state and target_state to the `config['algorithm']` by <br/>
`config['algorithm']['cost']['costs'][2]['data_types'][3]['map_state'] = config['agent']['map_state']`, <br/>
notice that previsous cost is super high probably because the target for calculating the target is not updated at all, i.e. still the dummy target in `hyperparams.py`
2. Change the angle information in both `map.py self.route.append` and `bus_world.py get_state()` to keep the angles within (-pi, pi)
3. The results are not good. Although the cost is reduced significantly, from 15,000 to (2000(no collision), 7000(collision)), the bus is easy to be stuck, e.g. at index 2, just cannot reach.
4. Discuss with Rei, underactuated robotics and convex optimization

## 3.20
1. For 3.19.3, try without collision cost but with yaw angle within (-pi, pi). It works and turn normally at the u-turn located at the bottom of the map
2. Passing that point, the bus is stuck at future turning point due to the abrupt yaw change. Since the bus is back steering, it has limits on the turning angle for path and cannot do shifting. <br/>
Soln: increase the yaw error tolerance and finally get rid of it. It still can follow the path quite nicely
3. For the "wierd waypoint" near the destination, it occurrs because the original route has branches, and when we randomly choose one for the bus, the point, which may be there for left turn, remains there. It also explains why the angle is always 90 degrees so that the bus cannot tell which to tell. <br/>
Soln: use the vector dot product and if the product is less than zero or Nan, remove the waypoint. <br/>
Thanks to Rei, try using the dot product of sum of v1 and v2 with v0, instead of individual one
4. Finally, for map with randomseed 13, the bus can reach the end at once.
5. Try with other maps, and change the some hard-code part to `map_size` so that it displays normally.
6. However, the case does not really generalize to other maps. <br/>
The map is partly cut, cannot cover the whole route. <br/>
Abrupt turning will affect its performance. <br/>
More fine-tuning, such as number of samples, number of iteration, is needed. <br/>
For map with seed=20, i cannot even find the bus, although the target is passed correctly.

## 3.21
1. Generate other maps and notice that the image was messed up. Modify by interchanging `map_width` and `map_height` for generating map images in `map.py`
2. Find that the turning always causes troubles, and try to dive into the GPS algorithm to understand more. Re-watch [Sergey Levine's talk](https://www.youtube.com/watch?v=CW1s6psByxk)
3. Bregman Alternating Direction Method of Multipliers (BADMM) [video](https://www.youtube.com/watch?v=Xg0ozgCXXB8) [paper](https://arxiv.org/pdf/1306.3203.pdf)

*Python*
* [numpy.sign](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.sign.html)

*Others*
* [Gauss map](https://en.wikipedia.org/wiki/Gauss_map)In differential geometry, the Gauss map (named after Carl F. Gauss) maps a surface in Euclidean space R3 to the unit sphere S2. Namely, given a surface X lying in R3, the Gauss map is a continuous map N: X → S2 such that N(p) is a unit vector orthogonal to X at p, namely the normal vector to X at p.
* [Indicator function](https://en.wikipedia.org/wiki/Indicator_function)In mathematics, an indicator function or a characteristic function is a function defined on a set X that indicates membership of an element in a subset A of X, having the value 1 for all elements of A and the value 0 for all elements of X not in A. It is usually denoted by a symbol 1 or I, sometimes in boldface or blackboard boldface, with a subscript specifying the subset.
* [Lasso](https://en.wikipedia.org/wiki/Lasso_(statistics)) least absolute shrinkage and selection operator
* [Gauss-Siedal model](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)
* [Duality](https://en.wikipedia.org/wiki/Duality_(optimization)) [Stanford ee364 slides](https://web.stanford.edu/class/ee364a/lectures/duality.pdf)
* [ADMM](https://web.stanford.edu/~boyd/papers/pdf/admm_slides.pdf)

## 3.22
1. Read [Variational End-to-End Navigation and Localization](https://arxiv.org/pdf/1811.10119.pdf) <br/>
Summary: <br/>
Input: raw sensory data from left, front, and right camera, cut with bonding boxes of either empty road or road curb + noisy roadmap (routed and unrouted) <br/>
Feed into shallow NN to preserve translation information and be compatible with fewer feature <br/>
Output: either probability distribution of steering control (for unrouted map) or deterministic direction (for routed map), with steering angel referring only to the road turning, i.e. not considering slip angle and other control plant parameters
2. Try to cut the map and produce a smaller image for training,  may need to readjust the epsilon parameter for polygon fitting 

*Others*
* [Normal-Inverse-Wishart distribution](https://en.wikipedia.org/wiki/Normal-inverse-Wishart_distribution) It is the conjugate prior of a multivariate normal distribution with unknown mean and covariance matrix (the inverse of the precision matrix)
* [Multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution): a random vector is said to be k-variate normally distributed if every linear combination of its k components has a univariate normal distribution. Its importance derives mainly from the multivariate central limit theorem. 
* [Cholesky decompostion](https://en.wikipedia.org/wiki/Cholesky_decomposition): decomposing a symmetrical matrix `A` in to the product of a lower triangular matrix `L` and its transpose `L_T`
* [Drive by wire](https://www.youtube.com/watch?v=vlM-VcQVMo0)
<br/>
To follow up
* Warm start
* [NVIDIA Drive Platform](https://www.nvidia.com/en-sg/self-driving-cars/drive-platform/)
* [Variational Inference for ML](https://www.youtube.com/watch?v=2pEkWk-LHmU)
* Learning a Variational Network for Reconstruction of Accelerated MRI Data [paper](https://arxiv.org/abs/1704.00447) [video](https://www.youtube.com/watch?v=5tXcVUTsWD4)

*Python*
* [`dict.update`](https://www.programiz.com/python-programming/methods/dictionary/update): insert a key if it does not exist, otherwise, update the value

## 3.25
*To do*
1. check the difference of action and policy and find the appropriate one for training.
2. ensure that image generation can be automated and generalized to other maps.

1. Skim through [Learning Neural Network Policies with Guided Policy
Search under Unknown Dynamics](https://papers.nips.cc/paper/5444-learning-neural-network-policies-with-guided-policy-search-under-unknown-dynamics.pdf)

*Python*
* [Pickle in Python](https://pythontips.com/2013/08/02/what-is-pickle-in-python/) serialize and deserialize the python data (lists, objects, etc) into files.

*Others*
* [Difference between policy search and policy iteration]: PI foucses more on value function
* [Policy search by Dynamic Programming](https://www.cs.cmu.edu/~schneide/bagnellPSDP.pdf)
* [RL algorithms quick overview](https://medium.com/@jonathan_hui/rl-reinforcement-learning-algorithms-quick-overview-6bf69736694d)

*anachronistic records, for cleaning the code*
* Tried to use `stuck_cnt`. The counter is incremented by one if the target is not reached and the final speed is unreasonably small (kind of interpreted as being stuck). Once the counter reaches 5, change the start position to `last_final_pos`. However, it doesn't really work, probably because it is guided in the same way as before, and therefore cannot be solved by repetitive process, but by addiing more samples or iterations.
* Use the following to check the final state
```
if final_pos is None or (not final_pos.any()):
# neither reach the target nor have enough speed to continue
continue
```
But same as before, simply repeating does not help

* To pass road info to GPS (change configurations in `hyperparams.py` into variables), manuly add them in the initialization of GPSMain. e.g. `hyperparams.config['agent']['target_state'] = target` <br/>
Follow the steps:
  * in hyperparams.py, create dummy variable under desired category, e.g. `action: {target: None}`
  * in GPSMain, re-initialize based on the params  e.g. `hyperparams.config['agent']['target_state'] = target`
  * in agent_bus.py and bus_world.py, add `target` to corresponding initialization and declaration
* In `bus_world.py`, don't consider yaw when `check_reach`, but in `new_gps.py`, when not hit and loop through the trajectory to find an appropriate "final_pos", do consider yaw. <br/>
Initially use weight, later add an upper limit <br/>
`target_dist = (X[i][0]-target[0])**2 + (X[i][1]-target[1])**2 + 1250*(X[i][2]-target[2])` <br/>
chaged to <br/>
`yaw_diff = min(500, 500*abs(X[i][2]-target[2]))
target_dist = (X[i][0]-target[0])**2 + (X[i][1]-target[1])**2 + yaw_diff`

## 3.26 
1. Consider circuit diagram of linear actuator, surge limiter
2. Add bus to the saved image for training. `draw_rot_rectangle` in map.py. Re-organize the code a bit, return X from `get_policy` in order to iterate for each timestep
3. Problem: the image generation and action saving stops after first index, i.e. cannot loop through the waypoints automatically, due to errors like <br/>

`  File "python/gps/new_gps.py", line 538, in get_policy
    raise ValueError("None in gps.U")
ValueError: None in gps.U`

*Debug*
* `OpenCV Error: Assertion failed (size.width>0 && size.height>0) in imshow` <br/>
cv2.line return nothing [see more](https://blog.csdn.net/sjx1989/article/details/79038996)

## 3.27
1. Pytorch [DEEP LEARNING WITH PYTORCH: A 60 MINUTE BLITZ](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html#deep-learning-with-pytorch-a-60-minute-blitz)
 <br/>
 To follow up: full documentation [DOCS](https://pytorch.org/docs/stable/torch.html)
2. Help Rei with geometries, but haven't concluded yet. Ref: [points, lines, spaces](http://paulbourke.net/geometry/pointlineplane/)

*Others*
*  [“Define-by-Run” frameworks](https://hackernoon.com/how-is-pytorch-different-from-tensorflow-2c90f44747d6): the system generates the graph structure at runtime.
* Find [distance between two line segments](http://csharphelper.com/blog/2014/08/find-the-shortest-distance-between-two-line-segments-in-c/)

## 3.28
1. Help with auto-calibration, driving the robot. Solve the problem with turning by swapping the batteries.
2. Finish the udacity part3 policy-based videos
3. see into pytorch optimizer

## 3.29
* PyTorch tutorial [Learn with examples](https://pytorch.org/tutorials/beginner/pytorch_with_examples.html#examples-download)
* Re-modify the code, changing from running GPS per timestep into running GPS for one index and save a series of actions and maps. (can also set an interval of 5 for saving files)
* Map 13 is stuck at about index 52, a turn. Try to use test_action to visualize. To keep consistent with collect_action, use `set_display_center` before creating the BusWorld


*Python*
* [np.concatenate, hstack, vstack](http://cmdlinetips.com/2018/04/how-to-concatenate-arrays-in-numpy/)

*Debug*
* `TypeError: 'tuple' object is not callable` <br/>
Soln: `print(U.shape)` shouldn't have `()` after `shape`
* `ValueError: all the input arrays must have same number of dimensions` when using `np.concatenate` <br/>
Soln: empty array cannot be concatenated with others. Check if `action_policy` is empty first

*Others*
* [ReLU in Deep learning](https://www.kaggle.com/dansbecker/rectified-linear-units-relu-in-deep-learning) `h=max(h, 0)`, <br/>
simple but good for dealing with non-linearirty and corelation
* Github <br/>
Submodule [explantation](https://gist.github.com/gitaarik/8735255)
[Add a local project to github repo](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line)

## 4.1
*Debug*
* Problem: the directions of waypoints are inaccurate. <br/>
Soln: First notice that only step 33-44 (U-turn) has problem, then swap the `BUS_LENGTH` and `BUS_WIDTH` in `recall_map` to correct the logic. Then I thought it might be the problem of opencv coordinates, but [ref](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html) and [documentation](https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#getrotationmatrix2d) shows that the positive angle is indeed counter-clockwise, i.e. consistent with normal coordinates. Finally realize that in `draw_rot_rectangle` (previously copied from Emily's code), the line `theta = np.radians(theta)` should be deleted cuz I use radian directly so no need to convert. 
* Problem: stuck at step 52, 53 <br/>
feel like the policy search is not working well, trying to dive into the GPS

*Modification*

*Others*
* [Tensorflow vs PyTorch](https://medium.com/@UdacityINDIA/tensorflow-or-pytorch-the-force-is-strong-with-which-one-68226bb7dab4)
* Obtain a MuJoco trial license. One step is to run a downloaded program called `getid_linux` <br/>
Initiallly, use `sudo getid_linux`, but since it is a program not a file, it doesn't work. <br/>
Use `./getid_linux` instead and get error `bash: ./getid_linux: Permission denied` <br/>
Soln: `chmod u+x program_name` or `sudo chmod +x program_name` followed by `./program_name` <br/>
then successfully get the id required 
* When I try to copy the `mujoco` folder to `gps`, it's locked and unable to directly change permission in `Properties` tab. <br/>
To change folder permission
```
1 - Open the Terminal
Enter the following command;
2 - sudo -i
You have now become Root
Enter The following command;
3 - gksudo nautilus
The nautilus file manager will now open, go to the folder you wish to change permissions on.
Right click on the folder and select Properties, click on the Permissions tab.
In the Owner part, click on File Access and set it to Read & Write, then click on Apply Permissions To Enclosed Files.
Close Terminal
```
* after copying, the mujoco simulation example can be run in its own folder (observe the directory hierachy and command to navigate to correct path) <br/>
but `cmake` fails and running example fails in `gps`, get error `CMake Error at /usr/share/cmake-3.5/Modules/FindPythonLibs.cmake:64 (get_filename_component): get_filename_component called with incorrect number of arguments Call Stack (most recent call first): Boost.NumPy/CMakeLists.txt:14 (find_package)` <br/>
`ubuntu LIB: /usr/lib/x86_64-linux-gnu/libboost_python.so -- Could NOT find osg (missing: OSG_LIBRARY OSG_INCLUDE_DIR) -- Could NOT find osgViewer (missing: OSGVIEWER_LIBRARY OSGVIEWER_INCLUDE_DIR) -- Could NOT find OpenThreads (missing: OPENTHREADS_LIBRARY OPENTHREADS_INCLUDE_DIR) -- Could NOT find osgGA (missing: OSGGA_LIBRARY OSGGA_INCLUDE_DIR) osg includes: OSG_INCLUDE_DIR-NOTFOUND CMake Error: The following variables are used in this project, but they are set to NOTFOUND.` <br/>
Tried to update cmake but it did not help <br/>
[Related issue 1](https://github.com/cbfinn/gps/issues/28) [Possible soln 2](https://stackoverflow.com/questions/40460841/linking-of-openscenegraph-libraries-for-cmake)

* [augmented Lagragian](https://en.wikipedia.org/wiki/Augmented_Lagrangian_method)

## 4.2 
1. To fix broken packages and cmake, use some apt commands sucha s <br/>
	* [How to use apt Package Manager on Ubuntu Command Line](https://vitux.com/how-to-use-apt-get-package-manager-on-ubuntu-command-line/)
	* `apt-cache search x` will output all packages that in a way or another make a reference to x.
	* `sudo dpkg -i <package>` for installation
	* [select and pin a package from a repo](https://www.jaredlog.com/?p=1820)
	* After you get that error, try `sudo apt-get -f install` to force an install of the files that didn't get loaded because of the error. Then try `sudo apt-get update` again, `sudo apt-get -f install` back and forth until only the package that has the error is left. `sudo dpkg --configure -a` and clean the cache `sudo apt-get clean`
	* "How do I remove only one specific package with apt-get?" <br/>
	apt-get won't let you do that, since it's a potentially dangerous step for a package management system to allow. As long as you are aware that there may be consequences, use dpkg with the --remove option to do it. For example:
`sudo dpkg --remove mysql-common` <br/>
From insomnia's comment: If you need to override the dependency system's decision you can (with great care and making sure you know what you are doing) use an additional --force-depends.
`sudo dpkg --remove --force-depends mysql-common`
2. To use Mujoco
* `Cmake` debugging tricks
	* To [display message in CMake list](https://cmake.org/cmake/help/v3.0/command/message.html), use `message([<mode>] "message to display" ...)` 
	* To [get filename](https://cmake.org/cmake/help/v3.5/command/get_filename_component.html), use `get_filename_component(<VAR> <FileName> <COMP> [CACHE])`

* Error at cmake "get_filename_component called with incorrect number of arguments" when `find_package( PythonLibs 2.7 REQUIRED ) ` in CMakeLists.txt is called <br/>
Soln: `cmake ../src/3rdparty/ -DPYTHON_EXECUTABLE= 'which python2.7' ` add `-DPYTHON_EXECUTABLE= 'which python2.7'` helps <br/>
Learn to find python path and python lib path, and configure them in CMakeLists.file like:
`    set(PYTHON_LIBRARY /usr/lib/python2.7/config-x86_64-linux-gnu/libpython2.7.so)
    set(PYTHON_INCLUDE_DIR /usr/include/python2.7)`
* `make` debugging <br/>
`In file included from /media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/gps/src/3rdparty/mjcpy2/mjcpy2.cpp:287:0:
/media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/gps/src/3rdparty/mjcpy2/mjcpy2_getdata_autogen.i: In member function ‘boost::python::dict {anonymous}::PyMJCWorld2::GetData()’:
/media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/gps/src/3rdparty/mjcpy2/mjcpy2_getdata_autogen.i:4:35: error: ‘mjData {aka struct _mjData}’ has no member named ‘maxuse_stack’
     out["maxuse_stack"] = m_data->maxuse_stack;
.......` <br/>
[Soln](https://github.com/cbfinn/gps/issues/83) follow acrosson <br/> run the autogen.py and toggle around the last few lines
* after `make`, import error debugging <br/>
	* error:     import mjcpy
ImportError: `/media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/gps/src/3rdparty/mjpro/bin/libmujoco200.so: undefined symbol: __glewBindBuffer` <br/>
[Soln](https://github.com/deepmind/dm_control/issues/3) (with navigating in my own computer and modify the path a bit by looking for libGL.so): `sudo apt-get install libglew-dev libglfw3-dev` followed by `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so:/usr/lib/libGL.so.1 python`
	* error:     import mjcpy
ImportError: `/media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/gps/build/lib/mjcpy.so: undefined symbol: _ZN5boost5numpy6detail15get_float_dtypeILi320EEENS0_5dtypeEv`
For my case, I only install mujoco200 at first and then find [soln](https://github.com/cbfinn/gps/issues/86) by searching "mjcpy.so: undefined symbol". Notice that "mujoco verisions newer than 131 are not compatible with python2.7" Re-downloading mujoco and copying the license file work. <br/>
Till now `import mjcpy` passes
3. install plugins in gedit to use ["code comment" function](https://delightlylinux.wordpress.com/2015/05/22/code-comment-gedit-plugin/) <br/>
`sudo apt-get update
sudo apt-get install gedit-plugins` <br/>
Encounter error `E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable)` <br/>
[Soln](https://itsfoss.com/could-not-get-lock-error/):
```
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
```
then repeat `sudo apt-get install gedit-plugins`
4. For 2. Preload thing, somehow in Terminator rather than Terminal), `python` withoud `LD_PRELOAD` works fine.
5. Run `gps_main.py mjc_example`, getting error `KeyError: 'body_pos'`, not solved yet. Find that the xml files in mjc_models are actually equivalent to world.py that contain world information. The error may be due to empty model, but `get_model` functions are written in c++. which fails me.
6. Switch to my bus and emulate to create a `agent_bus_pol`, which is not used yet
7. Modify the `hyperparams.py` for AgentBus, including `obs_include` for `algorithm` and `agent`
8. Debug: `module object has not attribute batch_matmul tensorflow` <br/>
Soln: The `tf.batch_matmul()` op was removed in 3a88ec0. You can now use `tf.matmul()` to perform batch matrix multiplications (i.e. for tensors with rank > 2).

## 4.3 
1. Copy&paste stop working in Terminator. Restarting the program helps.
2. Try to run consecutive indexes with tf, but get problems for variable scope and reuse stuff. Modify in `algorithm_badmm.py`, `tf_network_example.py` (sovled), and `tf_utilus` (not solved)
3. Switch to modify Emily's code
4. [sys.path](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)
5. [post on DQN and prioritized experience replay](https://medium.freecodecamp.org/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682)
6. [experience replay](https://arxiv.org/pdf/1712.01275.pdf) <br/>
prioritized experience replay [paper](https://arxiv.org/pdf/1511.05952.pdf)
7. To put the bus at the bottom, modify in `vehicle.py` <br/>
Try several methods like `setScreenCenter` and others, finally modify in `getObvservation()`, ~L651, increase the padding size, follow the original steps to rotate, and then shift the bus to desired place at final cutting step. <br/>
(Though not sure how the padding works and why crop_rad becomes the center)

*Python*
* Pad an array. [`numpy.pad(array, pad_width, mode, **kwargs)`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.pad.html)
* Interesting [WarpAffine proj](https://www.learnopencv.com/tag/warpaffine/)

## 4.4 
1. Going out to help log data
2. Study Emily's `ddpg.py` and `ReplayMemory` in `utils.py`
3. Try to retrain ddpg model with the bus located at the bottom <br/>
However, the model is not trained properly in that the bus learns only to go backwards even if the reward is negative.

*Debug*
* Error: `SyntaxError: Non-ASCII character '\xce' in file scripts/ddpg.py on line 215, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details` <br/>
Soln: It's a file encoding problem. Try adding this at the beginning of the file: `#coding=utf-8` or `# -*- coding: utf-8 -*-`
* Error `Invalid Syntax` for `model = DDPG(**model_arch, actor_lr=actor_lr, ...).to(device)`. <br/>
Soln: Note that `model_arch` is a dictionary containg keywords and their values, and the syntax [`*tuple` and `**dictionary`](https://stackoverflow.com/questions/21809112/what-does-tuple-and-dict-means-in-python) are only valid for python3. so switch python version to 3.
* Error: `ImportError: HDFStore requires PyTables, "No module named 'tables'" problem importing` for hdf data reading <br/>
Soln: In terminal, run `sudo apt-get install python3-tables`
* Error: `ValueError: cannot set WRITEABLE flag to True of this array Closing remaining open files:models/experiences/DDPG.h5...done` <br/>
Soln: Downgrade numpy by running in terminal `sudo pip3 install numpy==1.15.4` <br/>
To check numpy version, run in terminal `>> import numpy >> print numpy.__version__`
* Try to run the trained model in a new terminal, and encounter `AttributeError: '_NamespacePath' object has no attribute 'sort'` and other consecutive errors. Try to debug by upgrade pip and install `setuptools`, finally realize that I need refo `unset PYTHONPATH` in new terminal even if I'm using `python3 main.py`

*Others*
* ddpg [paper](http://proceedings.mlr.press/v32/silver14.pdf) [github impl. with tf](https://github.com/cookbenjamin/DDPG) [continuous control with ddpg paper](https://arxiv.org/pdf/1509.02971v5.pdf)
* [Segment tree for a faster implementation of prioritized replay buffer](https://www.hackerearth.com/zh/practice/data-structures/advanced-data-structures/segment-trees/tutorial/)

## 4.5 
1. Read Emily'code, esp. `ddpg.py` and `utils.py`, get the basic understanding.
2. Training the ddpg with original map works, with the returns increase from -80 to -30 at 3xxxx steps. <br/>
However, training with bus at the bottom doesn't work. Trying to look into feeding tiles, see whether it is because the feeding is too far away. <br/>
Soln: Check the code and notice that in `simulation_env.py` L152 step() function, the `self.bus.update()` (where the uncovered tiles are fed) comes first, followed by `self.bus.getObservation()` (where the observation map is obtained). Therefore, changing observation is impertinent to tiles feeding. It finally turns out that it just takes more steps for the bus to learn to go forward; at around step 5xxxx, it proceeds in the correct direction.
3. Priority Exp Replay is implemented in `utils.py -> updatePriors()` with priority set according to td_error.
4. After understanding the replay buffer implemented by Emily, should proceed to generate GPS "expert data" <br/>
Solve the problem by inserting `tf.reset_default_graph()` in `__init__` of PolicyOptTf. Find the appropriate position to be after `tf.initialize_all_variables()` and before `self.sess.run(init_op)`. Now the tensorflow can continuously provide policy for different indexes. However, in this case, it cannot reuse the policy learn before. Need to figure out correct way to reuse the tf networks. The problem is the minimizer such as Adam uses an input of `var_list`, hence hard to set var_scope

*Python*
* use [`import signal`](https://docs.python.org/3/library/signal.html#module-signal) to implement interrupt handler and to deal with unsynchronized events
*Others*
* Ornstein–Uhlenbeck process: a stochastic process in continuous-time. "The process is a stationary Gauss–Markov process, which means that it is a Gaussian process, a Markov process, and is temporally homogeneous. The Ornstein–Uhlenbeck process is the only nontrivial process that satisfies these three conditions, up to allowing linear transformations of the space and time variables. Over time, the process tends to drift towards its long-term mean: such a process is called mean-reverting. The process can be considered to be a modification of the random walk in continuous time, or Wiener process, in which the properties of the process have been changed so that there is a tendency of the walk to move back towards a central location, with a greater attraction when the process is further away from the center.` [wiki](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process)

## 4.8
1. Try to combine GPS and emily's simulator. <br/>
Initially try create gym agent for GPS, then hard to consider the collision, and the way of running gym (by reward) and GPS are a bit conflicting. Finally choose to use gym as overall env adn at each step, create corerspondent box2d agent for GPS to obtain action. Modify the `guidedPS.py`, `agent_bus.py`, and `bus_world.py`. 
*Debug*
* `ImportError: No module named '[]; [] is not a package` <br/>
either the problem of path or there are a file and a folder (package) that have the same name. e.g. `gps.py` and `gps` folder
* ValueError: too many values to unpack when running `findContours` <br/>
Soln: OpenCV version 3. cv2.findContours does return 3 objects `img, contours, hierarchy`, while version 2 returns only 2 objects `contours, hierarchy`

## 4.9 
1. Run the program and debug. <br/>
change part of python2 syntax to python3 <br/>
e.g. `import cPickle` -> `import pickle` <br/>
` dict.iteritems(), dict.iterkeys(), and dict.itervalues()` -> `dict.items(), dict.keys(), and dict.values()` respectively. <br/>
e.g. iterate over a dictionary: 
```
for key in d:
For Python 2.x:
for key, value in d.iteritems():
For Python 3.x:
for key, value in d.items():
```

solve the matplot deprecated syntax for new version <br/>
e.g. `'AxesSubplot' object has no attribute 'set_axis_bgcolor'`<br/>
Soln: `set_axis_bgcolor` -> `set_facecolor`, `get_axis_bgcolor` -> `get_facecolor`, `canvas.update()` -> `canvas.draw_idle()` <br/>

`filepath = os.path.abspath(__file__)` to get absolutu path of the current file <br/>
effective way to navigate around the directory `gps_dir = '/'.join(str.split(gps_filepath, '/')[:-2]) + '/gps/'`

2. Current problem <br/>
	* box2d polygon, vertices >=3
	* once not hit, the program stops

*Python*
1. [numpy.where](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html): used to check conditions and filter an array or matrix <br/>
[multiple conditions](https://stackoverflow.com/questions/16343752/numpy-where-function-multiple-conditions): e.g.  `dists[(np.where((dists >= r) & (dists <= r + dr)))]`

*Debug*
* `cv2.error: /io/opencv/modules/imgproc/src/contours.cpp:199: error: (-210) [Start]FindContours supports only CV_8UC1 images when mode != CV_RETR_FLOODFILL otherwise supports CV_32SC1 images only in function cvStartFindContours_Impl` <br/>
`cv2.error: /io/opencv/modules/imgproc/src/thresh.cpp:1505: error: (-210) in function threshold` <br/>
`cv2.error: /io/opencv/modules/imgproc/src/color.cpp:11048: error: (-215) scn == 3 || scn == 4 in function cvtColor` <br/>
Soln: `afterFourier = afterFourier.astype(np.uint8)`
`cv2.cvtColor(X, cv2.COLOR_RGB2HSV) ⇒ cv2.cvtColor(X.astype(np.uint8), cv2.COLOR_RGB2HSV)` <br/>
if `gray = cv2.imread('C:/Python34/images/2015-05-27-191152.jpg',0)` (load with `0` parameter) or already in binary format, no need to do cvtColor
* to smooth the edge and eliminate tiny narrow lines, dilate and erode <br/>
```
import cv2
import numpy as np
blur=((3,3),1)
erode_=(5,5)
dilate_=(3, 3)
cv2.imwrite('imgBool_erode_dilated_blured.png',cv2.dilate(cv2.erode(cv2.GaussianBlur(cv2.imread('so-br-in.png',0)/255, blur[0], blur[1]), np.ones(erode_)), np.ones(dilate_))*255)  
```

## 4.10
1. Revise [Policy Search](https://icml.cc/2015/tutorials/PolicySearch.pdf)
2. Find the inconsistency between emily's action setting and box2d setting. Tried to delve into how the policy (trajectory samples) are set. However, actually only `agent_bus` and `bus_world` matter, so adding some processing before `get_policy` returns gps.U is fine.

## 4.11
1. Stuck when the bus keeps turning. Find that the coordinate are inconsistent with the dynamics, for example, the bus should go up but the action is dragging it down. <br/>
Soln: change the [x, y] to `[x-display_center[0], display_center[1]-y]` before passing to `get_policy`
2. Stuck again when the bus travels a short distance. Firstly searching for "why box2d keeps flickering", notice it is wrong focus and begin to debug myself, printing out action and state at each step. Notice it is the problem of sign of y-speed, that shouldn't be negated between return from get_policy and iteration for next index.
3. Bug: The bus appears behind the target and route in box2d. <br/>
Soln: fail by searching "layers of rendering in box2d", but find that swap the change in `box_world init` helps. The earlier the body is created, nearer to the top it appears to be.
4. After it runs, tune the params a bit until box2d works fine. but it doesn't when replicating actions to gym. Try to see whether it is the problem of `getObservation`
5. git [delete local repo](https://superuser.com/questions/599289/github-completely-messed-up-the-local-files-of-github-in-my-computer) navigate to the directory, do `rm -rf .git`
6. [Show hidder files in Ubuntu](https://www.ubuntudoc.com/show-hidden-files-folders-ubuntu/)
7. opencv, `getRotationMatrix2D` only returns the matrix, while `warpAffine` performs the actual rotation action.

## 4.12
1. supplementary notes: [Image Warping and Morphing](https://www.comp.nus.edu.sg/~cs4340/lecture/imorph.pdf)
2. Understand emily's `	getObservation`. It crops centering `crop_rad[1], crop_rad[0]` because that is the actual pos of the bus after padding with crop_rad at each side. <br/>
Figure it out by trying my naive idea and ending up with column & row number < 0 if crop cetering `idx` <br/>
Enlarge the crop_rad and modify the y-coordinates of second cropping from previous `crop_rad[1]-obs_size-BOTTOM_OFFSET: crop_rad[1]+obs_size-BOTTOM_OFFSET` to `crop_rad[1]-obs_size: crop_rad[1]+obs_size-2*BOTTOM_OFFSET`
3. Problem: box2d uses acceleration as action\[0], while gym uses speed as action\[0], which doesn't work in box2d world (don't know why) <br/>
Soln: after returning from `get_policy`, concatenate speed and action\[1] (steering) and save as actions for gym. It works better. **Note**: in box2d, it may recover after collision, but not in gym
4. Learn [rectangle-fitting in PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics#rectangle-fitting), understand that it projects all ponts got from LidarSimulator to different angles with `c1` representing dot product, `c2` representing cross product, but sill not too clear about how the cost functions are set.
5.Try to finetune the ddpg network since state images are ready now. <br/>
Debug: Previously, the road banana keeps turning to the right when running `ddpg.py` and the bus goes backwards with rightmost steering when running `main.py` with gym rendering. <br/>
Soln: print out the actions taken by ddpg and find it is always \[-1.0, -1.0], even after long-time training. Then trace the `ddpg.py` and save the state and next_state in batch samples by `imwrite`. Find that though next_state is with bus at the bottom since it is obtained from `getObservation`, the state image coming from original memory is still with bus at the center. Start a new memory `DDPG_bottom.h5` and run `ddpg.py`, which add memory to the repo first and then finetune the `DDPG_finetune.pt` 
6. [Transfer Learning with Convolutional Neural Networks in PyTorch](https://towardsdatascience.com/transfer-learning-with-convolutional-neural-networks-in-pytorch-dd09190245ce)
7. Check [if a file or directory exists](https://stackabuse.com/python-check-if-a-file-or-directory-exists/) `isfile(filename)`, `isdir(dirname)`, `os.path.exists()`
8. Debug: `QObject::moveToThread: Current thread (0x39d2190) is not the object's thread (0x26ab880). Cannot move to target thread (0x39d2190)` <br/>
Check Qt version by `qmake --version`, which returns `QMake version 2.01a
Using Qt version 4.8.7 in /home/sunardi/anaconda3/envs/emily_env/lib` seeming not to have conflict versions.
Check installation history by `gedit /var/log/apt/history.log` in terminal and find that two commands  ` /usr/bin/unattended-upgrade` and `apt install cmake-qt-gui` contain qt. <br/>
Look at posts [github](https://github.com/skvark/opencv-python/issues/46) and [stackflow](https://stackoverflow.com/questions/46449850/how-to-fix-the-error-qobjectmovetothread-in-opencv-in-python), but still not solved yet. <br/>
[Threads and Qobjects explained](https://doc.qt.io/archives/qt-5.7/threads-qobject.html)9. 
9. Finally can connect gym and GPS, with the bus running from GPS's action. The next is to improve GPS to give more reliable action.
10. Save new memory `DDPG_bottom.h5` and retrain the model `DDPG_fineture.pt`
11. *To Do* Try to run MUJOCO to see how to use images as input. (visualmotor), but none of the model can be loaded.  

*Python*
* The @ (at) operator is intended to be used for matrix multiplication. No builtin Python types implement this operator.New in version 3.5.
* Python [create `hdf5` file](http://docs.h5py.org/en/stable/quick.html)

## 4.14 
!. check the training. find that the DDPG_bottom.pt memory is 1.7T, hard to delete, either. `No such file or directory`. Restart the computer helps, maybe because the file systems lags and stucks a bit.
2. Find that the probles is that I shouldn't add `memory.add(memory_path)` when iteratively collecting the memory, new memory will be created by ReplayMemory and will be saved. Learn [hdf store with pandas](https://riptutorial.com/pandas/example/9812/using-hdfstore)  [panda cookbook](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html)

## 4.15
1. [ROS cheatsheet](https://mirror.umd.edu/roswiki/attachments/de/ROScheatsheet.pdf)
2. Try to plot the training curve. <br/>
[Insert chart in LibreOffice Calc](https://help.libreoffice.org/Common/Inserting_Charts): select the data -> Toolbar Insert -> Charts -> select the setting and choose "first column as label" to plot the rewards (second column) w.r.t to the NO. of iterations. <br/>
To [save the chart as image](https://ask.libreoffice.org/en/question/2142/save-a-chartgraph-as-image-in-calc/), I copy and paste the chart to LibreOffice Draw and save.

*Debug*
* The top toolbar is missing for every program. To recover it, in terminal do `sudo service lightdm restart`. Note: that will stop currently active processes. Save necessary things before executing the command.
*Python*
* [Python Interrupt](http://effbot.org/zone/stupid-exceptions-keyboardinterrupt.html): works for `ctrl+C`, so please wait `ddpg.py` to save models before after delayedInterrupt. Use `ctrl+X/Z` will stop it fast but will not trigger `KeyboardInterrupt` and save the model!
* commit and [rollback](https://www.youtube.com/watch?v=WJLIekhNwcg) The changes can be rolled back or "reverted" by calling `rollback()` after `try`, while `commit()` finalized the changes so that they cannot be changed back.

## 4.16
Idea 1: given a start state, use GPS to get a short series of action to replace `action = model.get_action(stacked_state)` and then step in gym and add to memory 
```
next_state, reward, done, info = env.step(action)
env.render(wait=False)
memory.add(state, action, reward, done)
```
Idea 2: pass the global map to GPS, run in box2d and create images just as `get_Observation` does in gym. use image as supplementary input to the policy optimization algo.

1. [Create virtualenv and install specified packges with pip](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) I create an virtualenv called `env2` for python3.5 under `ruihan` but haven't installed anything, can be used later if needed.
2. Come up with two ideas of combining GPS and gym <br/>
One is: pass the global map (with route) from gym to GPS and run a rollout, pack the actions and send back to gym to `step` and `memory.add` <br/>
The other is use something similar to `cv2.fillConvexPoly` in `update()` in `vehicle.py` to generate images directly from GPS. These images can be also used as image output `get_image` for tensorflow network to perform policy optimization.
3. Map transformation between emily's and previous GPS one. Modify in `ruihan/gps`, but the GPS is not reliable enough to reach the target.
4. [Inverse RL Bootcamp](https://www.youtube.com/watch?v=d9DlQSJQAoI)

*Debug*
* Modify `get_target_from_banana` with `x_temp = np.median(np.where(banana[i,:]==255))` and check `np.isnan(x_temp)` before appending new target. Pay attention to the order!! Previously used `np.where(banana==255)`, which gave an invalid constant.

## 4.17
1. Run GPS, tune the `init_var` params for traj_opt and it to some extent works. e.g. init_var=0.1: can only reach index 5, init_var-0.5, can reach index 57, init_var=1.0, can reach till the end. But current problem is that when I convert and copy the actions to gym, the bus still hits the wall. I guess it is because no road curb information is included in GPS, so it may hit while exploring. Sidenote, save two sets of actions per run of GPS, one for box2d replay, one for checking in gym.
	
*Python*
* [del keyword](https://www.w3schools.com/python/ref_keyword_del.asp): The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
* [slice](https://www.programiz.com/python-programming/methods/built-in/slice): The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step)
* [\_setattr\_](https://python-reference.readthedocs.io/en/latest/docs/dunderattr/setattr.html): e.g. `object.__setattr__(self, key, value)`
* [numpy.c_](https://docs.scipy.org/doc/numpy/reference/generated/numpy.c_.html): column stack vectors into 2D array

*Math*
* • If you add a matrix and its transpose the result is symmetric. You can only do the addition
if the matrix and its transpose are the same shape; so we need a square matrix for this. <br/>
• If you subtract the transpose from the matrix the result is antisymmetric. <br/>
[sum of a matrix and its transpose](https://mathoverflow.net/questions/52578/eigenvalues-of-sum-of-a-non-symmetric-matrix-and-its-transpose-aat)
* [Introduction to Regression Analysis](https://www.youtube.com/watch?v=TU2t1HDwVuA&gl=SG&hl=en-GB). Read wiki about linear regression and least square. "linear" refers to fitting the data with a line, while "least square" refers to choosing the best params for fitting by minimizing the square error.
* how to fit a Gaussian linear model [notes 1](http://www.math.univ-toulouse.fr/~agarivie/Telecom/centrale/modlin.pdf) [notes 2](https://ocw.mit.edu/courses/mathematics/18-655-mathematical-statistics-spring-2016/lecture-notes/MIT18_655S16_LecNote19.pdf)
* [Sampling Distribution of the Sample Proportion, p-hat](https://bolt.mph.ufl.edu/6050-6052/module-9/sampling-distribution-of-p-hat/)


## 4.18
1. To draw the map appropriately on box2D environment: <br/>
change the `LANE_WIDTH` to 8 to be consistent <br/>
use valid algorithm "ear clipping" [code](https://github.com/linuxlewis/tripy) [note](https://www.geometrictools.com/Documentation/TriangulationByEarClipping.pdf) for [polygon triangulation](https://en.wikipedia.org/wiki/Polygon_triangulation) <br/>
notice that the approx_poly function always return the outer layer (which we don't want) <br/>
try to tune [`cv2.line`](https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html#void line(Mat& img, Point pt1, Point pt2, const Scalar& color, int thickness, int lineType, int shift)) function such as lineType and shift, not the way. Supplementary: [anti-aliasing line](https://en.wikipedia.org/wiki/Xiaolin_Wu%27s_line_algorithm) [pixel connectivity](https://en.wikipedia.org/wiki/Pixel_connectivity)
comment the `add_border` part (which changes the pixel value at the border) in `map.py` helps <br/>
Supplementary: cv2 [superpixel](https://docs.opencv.org/3.4/df/d6c/group__ximgproc__superpixel.html), which is color-based and not necessarily return convex shapes.
2. There is still discrepancy between dynamics of box2d and gym. esp for collision. Temporarily set coll_sped = 0 in gym and reduce the LAENE_WIDTH for box2d.
3. Adjust box2d environment params like `friction` and `restitution` in bus_world, but it doesn't help much. And when the LANE_WIDTH is reduced, the bus tends to collide, rub, rub and go, which is not practical. It also fails to reach the final target, around index 53 for map 13.

*To Do*
* Look into statistics and understand how to fit linear Gaussian model with prior
* check why the cost is so high
* check how dynamic programming works, e.g. in `traj_opt_lqr_python` Line 309

## 4.22
1. The ddpg model finishes training at a return of about 2 and does not learn to turn. Thanks to Rei's advice, check the memory. write `check_memory.py` and `convert_memory.py` to look into the format of hdf and convert it to make them consistent. It's possible since Emily may adjust the code after training. After comparing, notice that DDPG_bottom.h5 contains mostly map13, adjust and retrain. (waste so much time!!!!)
*Debug*
* `TypeError: list indices must be integers or slices, not float` <br/>
when u set `memory_size = 1e6`, its default type is float and conflicts with later funtions, use` int(1e6)` instead )

## 4.23
1. Try [GAIL](https://hollygrimm.com/rl_gail) [paper](https://arxiv.org/pdf/1606.03476.pdf) [github fork](https://github.com/havefun28/baselines) (run by `python3 ...`) <br/>
To install `baselines` packages, debug: <br/>
* run `pip3 install -U mujoco-py`, get ` File "/usr/share/python-wheels/pkg_resources-0.0.0-py2.py3-none-any.whl/pkg_resources/__init__.py", line 2066, in _rebuild_mod_path`
`AttributeError: '_NamespacePath' object has no attribute 'sort'` <br/>
Soln: `unset PYTHONPATH` to solve `py2.py3-` followed by `pip3 install -U mujoco-py --user`
* run `sudo pip install xxx` get `ImportError: cannot import name 'main'` <br/>
Soln: run `pip install xxx --user` instead
* Re-download the correct mujoco200 folder for Linux (MacOS has separate folders, pay attention!) <br/> 
find out that in addition to download mujoco200 from website (whihc can be tested by running `./simulate` in folder `mujoco200/bin`, or `python3 >> import mujoco`), need to install `mujoco-py` as a separate library 
`git clone https://github.com/openai/mujoco-py.git` <br/>
add the line to `request` as specified in README <br/>
`sudo python3 setup.py install` need to run the `setup.py` since it is there!! <br/>
* still get building error 
```
/usr/bin/ld: cannot find -lmujoco200
/usr/bin/ld: cannot find -lglewegl
collect2: error: ld returned 1 exit status
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
```
Soln: `locate libmujoco200.so` (filename = `lib` + \[lib-name] + `.so`) <br/>
output: `/home/sunardi/Downloads/mujoco200_linux/bin/libmujoco200.so` <br/>
`sudo cp /home/sunardi/Downloads/mujoco200_linux/bin/libmujoco200.so /usr/lib` (copy the `.so` file to `/usr/lib`) <br/>
do the same for `libglewegl.so` <br/>
add `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu/` to `~/.bashrc` and `source ~/.bashrc` followed by `sudo ldconfig` (Possible [alterntive](https://askubuntu.com/questions/1007591/usr-bin-ld-cannot-find-lopencl) "The solution there was to make a link for the library to a known lib location:"
`sudo ln -s /usr/lib/x86_64-linux-gnu/libOpenCL.so.1 /usr/lib/libOpenCL.so`)<br/>
run `pip3 install mujoco-py --user` again and get new error `running build_ext  error: [Errno 2] No such file or directory: 'patchelf'`<br/>
Soln: ` pip3 install -e . --user` then install patchelf 
```
sudo add-apt-repository ppa:jamesh/snap-support
sudo apt-get update
sudo apt install patchelf
```
Run `pip3 install mujoco-py --user` again and finally succeed `Successfully installed mujoco-py-2.0.2.2`. Now can run the command to train the model as specified in Github.
Side-linnks: [usr/bin/ld: cannot find \<nameOfTheLibrary>](https://stackoverflow.com/questions/16710047/usr-bin-ld-cannot-find-lnameofthelibrary) <br/>
[What does “collect2: error: ld returned 1 exit status” mean?](https://stackoverflow.com/questions/27272525/what-does-collect2-error-ld-returned-1-exit-status-mean/27272651) <br/>
`arch` command in terminal to return the computer's architecture e.g. `x86_64`

2. Implement image-based GPS <br/>
write `new_gps_pol.py`. try to generate an init map, run 5 trials, then draw local map again. <br/>
Notice that for 5 steps, it is still loop one by one, without global information. and hard to get the target info from global state_map due to the image transformation matrix <br/>
write `new_gps_pol2.py` and `agent_bus_pol.py`. mainly modify the `init_sample` and `set_sample` part to include the image information.

3. Ask about Rei's traffic lights. quite a lot situation, self-adjusting camera, try to use homographical info (height of traffic lights) to get depth prediction.

*Debug*
* `pygame.py has no attribute 'PygameFramework'` <br/>
It is because of mutual import. Try to delink them (I delete the line of `from framework import *` in  `map.py` since it is not usefuly for now)

## 4.24
1. Conitnue to implement image-based GPS. Try to see how mjcpy works but fails.
*Debug*
* `ValueError: all the input arrays must have same number of dimensions` <br/>
algorithm_badmm takes `x0` as a vector, so need to convert the format

*Debug*
* Solve an "enduring" bug: [`QObject::moveToThread: Current thread (0x4b33490) is not the object's thread (0x2ca6db0). Cannot move to target thread (0x4b33490)`](https://stackoverflow.com/questions/46449850/how-to-fix-the-error-qobjectmovetothread-in-opencv-in-python) (multiple lines, quite frustrating) <br/>
Soln: First, uninstall any versions of OpenCV you may have installed. If you installed using pip:
`sudo pip uninstall opencv-python`
Next, try installing OpenCV using your Linux distro's package manager. For Ubuntu/Debian, this is:
`sudo apt-get install libopencv-dev python-opencv`
For python3, install opencv-python in your machine using:
`unset PYTHONPATH` for me followed by `sudo pip3 install opencv-python` To specify the version, use `sudo pip3 install opencv-python==3.3.0.10` <br/>
NO! IT DOESN'T HELP see [here](https://www.bountysource.com/issues/49237490-opencv-gui-does-not-work) cannot solve.
* pip ImportError: cannot import name 'main' after update <br/>
soln: `sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall`
* To check module version, e.g. `pkg-config --modversion opencv`
* [Install opencv for python](https://medium.com/@debugvn/installing-opencv-3-3-0-on-ubuntu-16-04-lts-7db376f93961) `pip install opencv-contrib-python`

## 4.25
1.  Continue to implement GPS with images, mainly debugging for TF policy, such as the tensor dimension (e.g. get_shape), syntax discrepancy (e.g. concat), and gui functions
2. Go through the process, can draw graphs and iterate over `iter_num`. But the loss is huge and policy is not working well. Work to be done.
* In `policy_opt_tf.py`, comment Line 176,177; 194,195 for simplicity. Search `LOGGER.info` to find them and uncomment
3. Following Emily's advice, retrain the ddpg model from scratch, calling it `DDPG_bottom3`

*Python*
* [numpy.empty(shape, dtype=float, order='C')](https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html) Return a new array of given shape and type, without initializing entries.
* numpy.random.shuffle(x) Modify a sequence in-place by shuffling its contents.
* [tf.nn.relu](https://www.tensorflow.org/api_docs/python/tf/nn/relu)
* [tf.tensor](https://www.tensorflow.org/api_docs/python/tf/Tensor#get_shape)

*Debug*
* `TypeError: Fetch argument None has invalid type <class 'NoneType'> ` for `self.feat_op` in tf_policy.py -> get_feature() <br/>
Whether flatten the image, use `tf.shape` instead of `shape` <br/>
For me, it turns out that I should use `multi_modal_network_fp` to return network with feature points `fp` <br/>
also find dicrepancy in function definition of `tf.concat`. For my version 1.12.0, use `tf.concat(values, axis, name='concat')`, e.g. `concat = tf.concat([x, h], 1)` instead of `concat = tf.concat(1, [x, h])`
* `TypeError: int() argument must be a string, a bytes-like object or a number, not 'Tensor'` <br/>
Soln: instead of using, 
```
layer_shape = tf.shape(conv_layer_2)
num_rows = int(layer_shape[1])
num_cols = int(layer_shape[2])
```
use `   num_rows, num_cols, num_fp = [int(x) for x in [conv_layer_2.get_shape()[1], conv_layer_2.get_shape()[2], conv_layer_2.get_shape()[3]]]`
* in `gps_training_gui.py` get `TypeError: 'float' object cannot be interpreted as an integer` <br/>
`print(ee_pt.shape) # (150,3)` use `for i in range(ee_pt.shape[1]//3):` instead of `for i in range(ee_pt.shape[1]/3):` <br/>
maybe because of difference between python 2&3

## 4.26
1. Continue to implement and try out the GPD with badmm algorithm and image input. It runs smoothly (can reach the end without walls), but still hit the wall and be stuck with obstacles. <br/>
Discuss with Rei: <br/>
	* Try reduce the COVER_TILE and pave denser for GPS. (the point of using GPS instead of normal controller is that, normal controller using pre-defined path and control output and cannot deal with environment noise well, while GPS is real-time exploring. See how to add environment noise e.g. obstacle in simulator and observe its performance) <br/>
	* Alternatively, after saving all actions, run in gym, if stuck, jump to the next waypoint, and only collect valid partition as replay memory.
2. Modify `data_files_dir` in get_policy, so that include map seed info in the filename. <br/>
Like in hyperparams.py add `if not os.path.exists(data_files_dir):
	os.makedirs(data_files_dir)`
after `	data_files_dir = exp_dir + 'map_{}/'.format(mapseed) + 'data_files/'`
because of error `FileNotFoundError: [Errno 2] No such file or directory: '/media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/gps/experiments/box2d_bus_badmm_example/map_13/data_files/figure_itr_00.png'`.

*Debug*
* With `render=True`, get error
 ```
 File "python/gps/agent/box2d/bus_world.py", line 287, in run_next
    super().run_next(action)
  File "python/gps/agent/box2d/pygame_framework.py", line 254, in run_next
    self.clock.tick(self.settings.hz)
AttributeError: 'BusWorld' object has no attribute 'clock'
```
Soln: Python2&3 syntax difference for `super()` function. Change `super(Childclass, self).__init__(student_name, student_age)` to `super().__init__()` and same for other inherited methods; <br/>
also uncomment `self._worlds[condition].run()` and `self._worlds[condition].reset_world()` in `agent_bus_pol.py` -> `sample()` method to reset the world and initialize `clock` in Pygamework.py

*Notes*
* To follow up: Hamilon Jacobi Bellman equation [video](https://www.youtube.com/watch?v=_zE5z-KZGRw)  [lec notes](http://www.princeton.edu/~moll/ECO521Web/Lecture4_ECO521_web.pdf)
[stochastic differential equation video][https://www.youtube.com/watch?v=qdbkvD4N-us]
* Watched: [Hamilton Jacobi Bellman equation](https://www.youtube.com/watch?v=YpSmbH3H890)
* [Passive dynamics](https://en.wikipedia.org/wiki/Passive_dynamics) Passive dynamics refers to the dynamical behavior of actuators, robots, or organisms when not drawing energy from a supply (e.g., batteries, fuel, ATP).
* Read PI2 control [paper 1](http://www.jmlr.org/papers/volume11/theodorou10a/theodorou10a.pdf)
* [Matirx differentiation](https://www.comp.nus.edu.sg/~cs5240/lecture/matrix-differentiation.pdf)
* [race of a matrix](http://mathworld.wolfram.com/MatrixTrace.html): suum of elements on principal diagonal

*Books to read*
* [Reinforcement learning: An introduction](http://incompleteideas.net/book/bookdraft2017nov5.pdf)
* [Convex optimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

*Python*
* make directory for file
```
import os
import errno
filename = "/foo/bar/baz.txt"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filename, "w") as f:
    f.write("FOOBAR")
```

## 4.29
1. Test the gps trained with tf policy, not good at all.  <br/>
	* Try pure traj_opt with denser targets (COVER_TILE=10)
	* Check whether images are accurate
	* add obstacle when exploring policy
2. Adjust the `gps._log_data()` in `new_gps_pol2`, save both `idx` and `itr` information
3. Change in get_observation. Create a map for each sample and add `map_state_shared = map.map_state.copy()` in order to clear prev cars. **every sentence in emily's code counts!**
4. To debug, write in `set_sample` `cv2.imwrite`, use `if t%10 == 0` to reduce memory required.
5. In hyperparams, change BUS_GAIN from `[1, 1]` to `[1, 1e-3]`
6. agent.sample(), adjust the if else sentences to debug `    period = self.reach_end - self.reach_start TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'`
7. save map_state_shared as `CONTEXT_IAMGE` in `init_sample` and can retrieve it by `sample._data[CONTEXT_IMAGE]`

## 4.30
1. Debug the images generated for gps, use different map and find that should swap IMAGE_WIDTH and IMAGE_HEIGHT
2. Help with calibration, driving the robot
3. Problem: though copying the route for each sample, it only works for idx 0.

## 5.2
1. Debug for images in GPS, find two stupid mistakes. <br/>
For incredibly high cost, find out that in `cost_state.py`, you once change the target by `tgt = [target_state[0]-map_size[1]/2, map_size[0]/2-target_state[1], target_state[2]]`, which is implemented later in `new_gps_pol` before passsing `hyperparams.config`, i.e. redundant chane results in wrong calculation of cost ` dist = x - tgt`. (that may also explain why the bus always tends to collide with the wall) <br/>
For the problem in 4.30, it turns out that the part for rendering new `TARGET` pixels in get_observation are wrong, having a yaw angle difference of pi/2 compared to the part of restoring `ROAD`. Debug by writing a small program to draw the polygons and the vehicle position on empty canvas with opencv and compare two polygons removed and added due to the same COVER pixel. 

## 5.3 
1. Misc: [Bash functions](https://linuxize.com/post/bash-functions/)
2. Check and learn the plot for Linear Gaussian Controller, roughly understand `gps_training_gui.py`  <br/>
where it draws ellipses to represent the mean and covariance of end-effector positions. <br/>
Related: [how to draw a covariance error ellipse](http://www.visiondummy.com/2014/04/draw-error-ellipse-representing-covariance-matrix/) <br/>
[sigular value decomposition](https://www.youtube.com/watch?v=mBcLRGuAFUk) <br/>
Tick most of conect in `cost` folder, except for `evall1l2term`  ` evallogl2term` in cost_utils <br/>
[L1/l2 loss function and regularization](http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/)
3. Find that the problem is still in `cost_state`, modify in GPSMain to pass the global map_size instead of box2d map_size (48, 48) to `tgt` in cost_state
4. Find that, with images and tf policy, the trajectories are different for each run, bearing some randomness.
5. Play with nano-degree. [Install Jupyter on Ubuntu](https://www.rosehosting.com/blog/how-to-install-jupyter-on-an-ubuntu-16-04-vps/) If encounter error `Jupyter command not found`, may need to install Anaconda, see below. After installation, open the folder of `deep-reinfrcement learning` in terminal and run `jupyter notebook`, follow the instruction to copy the url in chrome browser and there you go~
6. Install Anaconda at `/media/ml2/Storage` on `sky` computer. NO space in `~` directory

## 5.6
1. The policy was not working well. Debug and find that changing coordinates for box2d rendering affect the images generated in get_observation, thus the image features does not help. Modify in `init_sample` and `set_sample` in `agent_bus_pol`: <br/>
```
map_X = b2d_X[END_EFFECTOR_POINTS]
map_X = [map_X[0]- self.env_map.map_size[1]/2, map_X[1]- self.env_map.map_size[0]/2, map_X[2]]
```
so that `x0` and `obs_route` in `get_observation` are consistent with each other
2. TODO: currently, for each idx, the GPS restart learn from scratch  <br/>
want to do: save the policy/algorithm of last index and use `resume` function to make use of prior experience.
3. Rei: use vgg-ssd. mapping camera and all lidars using transformation matrices. pos/neg z value, need to set constraint or adjust cost for optimization


*Python*
* numpy.argmax(a, axis=None, out=None): Returns the indices of the maximum values along an axis.
* [enumerate()](https://www.geeksforgeeks.org/enumerate-in-python/)
* [`=` operation, shallowcopy and deepcopy](https://www.programiz.com/python-programming/shallow-deep-copy)

*Notes*
* [clustering](https://people.eecs.berkeley.edu/~jordan/courses/294-fall09/lectures/clustering/slides.pdf) 
* [cross entropy method(cem) video](https://www.youtube.com/watch?v=tRsSi_sqXjI)

## 5.7
1. Logbook, wk11-12, 13-14. 15-16
2. Modify `new_gps.py` especially in and `get_policy` and `test_action`, where `map_state` is added as parameters passed to BusWorld.
3. Problem of image-based GPS, even if I set only one target, it still keeps turning and turning. TODO: try to debug.

*Notes*
* [Experience replay](https://medium.freecodecamp.org/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682)

## 5.8
1. Try to run GAIL, stuck at `Expired activation key...` after obtaining a new key <br/>
Try a host of ways, including checking the access date of files, moving around the activtion key text file, and copy the mujoco200 folder to home directory. <br/>
Ask Rei for help. It was because when I create mujoco200 in home folder,it did not match with the path. <br/>
In the path, the dot `.` in `~/.mujoco` means hidden file, which can be created in terminal by `mkdir .mujoco`, while `create new folder` in GUI only create non-hidder folder `~/mujoco`. So should either mkdir in terminal or modify the path to `~/mujoco`. <br/>
Sidenote: for permission issue, can try `chmod +x filename` or `chmod -R 777 ./`, where `-R` or `--recursive` loop through the directory, `./` means giving same permission to all files in current directory, `777` means `all permission`.
2. Ask Rei about vision part, try to do semantic segmentation based on [kitti dataset](http://www.cvlibs.net/datasets/kitti/eval_semseg.php?benchmark=semantics2015) <br/>
Use[pykitti tools](https://github.com/utiasSTARS/pykitti)

*To follow up*
* Read about [PPO](https://medium.com/@jonathan_hui/rl-proximal-policy-optimization-ppo-explained-77f014ec3f12)
* Read about [Python egg](https://setuptools.readthedocs.io/en/latest/formats.html)

*Python*
* `replace`
* [`glob` module](https://docs.python.org/2/library/glob.html)

## 5.9
1. Write the script to read the kitti dataset and label the points. <br/>
load the file, parse into dictionary, calculate 3D bounding box, render for display (convert from matplot to opencv).
2. [kitti 3D object dataset explained](https://medium.com/test-ttile/kitti-3d-object-detection-dataset-d78a762b5a4)

*Python*
* Efficient way of writing
my efficient way:
```
    f = open(fcalib, 'r')
    for line in f.readlines():
      line = line.split()
      if line:
          print(line[0])
          line_key = line[0][:-1]
          data[line_key] = []
          line.pop(0)
          while len(line):
              data[line_key].append(float(line.pop()))
    print(data)
```
Efficient way:
```
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if len(line) < 2:
                continue
            key, value = line.split(':', 1)
            try:
                data[key] = np.array([float(x) for x in value.split()])
            except ValueError:
                pass
	
```

* [split](https://www.geeksforgeeks.org/python-string-split/)
* [np.fromfile](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromfile.html) TODO
* matplot rendering: [path](https://matplotlib.org/api/path_api.html): MOVETO: moving the "brush" to the starting point; LINETO: draw a line to that point. [pathpatch example](https://www.programcreek.com/python/example/67942/matplotlib.patches.PathPatch). In correspondence, can use [polyline in opencv](https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html#polylines) `cv2.polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) → None`

## 5.10
1. Implement the kitti vision to find the visible surfaces. <br/>
Try a few methods, such as
	* lowest top point (highest y pixel value)
	* compare the distance (to middle center and to bottom center)
	* working one: find the quadrant where the observation point is located in w.r.t. the car center location
	try to set the observation at different position. if bottom middle, some cases don't work. finalize it to be \[car_center_2D_x, img_height], i.e. moving along the bottom line with the x-coords of car object
Spent some time on coords transformation. <br/>
use opencv draw line and draw point(small circle) functions to help debug
2. 

*Python*
* [inverse of matrix](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html) ainv = np.linalg.inv(a)
* [sorting](https://wiki.python.org/moin/HowTo/Sorting#Sortingbykeys)
```
# To sort the list in place...
cars.sort(key=lambda car: car.max_area, reverse=True)
or
sorted(cars, key=lambda car: car.max_area) 
# To return a new list, use the sorted() built-in function...
newlist = sorted(cars, key=lambda car: car.max_area) 
```

## 5.13
1. Decode the velodyne data. Try to use it to draw car shape, but it does not help much if converted to image without depth info.

2. final report
* policy gradient <br/>
[pong game for policy gradient: HIGH-DIMENSIONAL CONTINUOUS CONTROL USING
GENERALIZED ADVANTAGE ESTIMATION](https://arxiv.org/pdf/1506.02438.pdf) <br/>
https://medium.com/deep-math-machine-learning-ai/ch-13-deep-reinforcement-learning-deep-q-learning-and-policy-gradients-towards-agi-a2a0b611617e <br/>
https://medium.com/@jonathan_hui/rl-policy-gradients-explained-9b13b688b146 <br/>
http://karpathy.github.io/2016/05/31/rl/ <br/>
http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/pg.pdf <br/>

[Beyesian locally weighted regression](https://www.cs.cmu.edu/~schneide/tut5/node37.html)
https://pdfs.semanticscholar.org/c3ae/a964f75b04e2ee04082cbf94d034f3af1b4b.pdf
[policy inference](https://www.youtube.com/watch?v=A6Ud6oUCRak)
[PILCO](http://mlg.eng.cam.ac.uk/pub/pdf/DeiRas11.pdf)

*Python*
* Opencv, use line width of `-1` to fill the polygon shape
* [`pointPolygonTest`](https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=pointpolygontest#pointpolygontest) returns 1 if point is inside, 0 if on the edge of, -1 if outside the polygon shape.

## 5.14
1. Debug kitti `make_dataset.py` <br/>
Use Rei's code for checking. The problem was I accidentally modified the velodyne data. It is already in 4D, so don't need to extend the dimension. what I though to be used to extend the dimension `+[1.0]` actually change the data, and results in offset for each individual point <br/>
To use velodyne depth information, find the polygons, within each surf cluster the points and choose closest cluster as selected points. 
For clustering, first try 1D [Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html) or [gaussian-kde](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html), but it outputs a score, not cluster number. Swich to 2D [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) and use the index as the other dimension. [example in documentation](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py)
2. Clean up my code

*Debug*
* import pydrake <br/>
	* `ImportError: libpng16.so.16: cannot open shared object file: No such file or directory`  <br/>
Soln: copy libpng16.so.16 to /usr/lib/ may be ok `locate libpng16.so.16` then `cp <location> /usr/lib/`
	* `ImportError: libprotobuf.so.10: cannot open shared object file: No such file or directory` <br/>
locate: libprotobuf9 in usr/lib/gnu and libprotobuf15 in anaconda

**Latex**
* [cheatsheet](https://www.nyu.edu/projects/beber/files/Chang_LaTeX_sheet.pdf)
* [overleaf-mathematical expression](https://www.overleaf.com/learn/latex/Mathematical_expressions)
* [overleaf-Greek letters](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols)
* [limits and derivatives](https://math-linux.com/latex-26/faq/latex-faq/article/how-to-write-latex-derivatives-limits-sums-products-and-integrals)
* [epsilon and log](https://tex.stackexchange.com/questions/238179/epsilon-and-log-functions)
* [refer to an equation](https://tex.stackexchange.com/questions/58764/cross-referencing-an-equation)
* [argmin & argmax](https://tex.stackexchange.com/questions/5223/command-for-argmin-or-argmax)
* [overleaf-font size & style](https://www.overleaf.com/learn/latex/Font_sizes,_families,_and_styles#Font_styles)
* [math letter](https://tex.stackexchange.com/questions/58098/what-are-all-the-font-styles-i-can-use-in-math-mode)
* [norm and abs value symbol](https://tex.stackexchange.com/questions/43008/absolute-value-symbols) [resize it](https://tex.stackexchange.com/questions/107186/how-to-write-norm-which-adjusts-its-size)
* [fraction and binomial](https://www.overleaf.com/learn/latex/Fractions_and_Binomials)
* natural log [ln]()https://tex.stackexchange.com/questions/314609/no-natural-log-parentheses-when-typesetting use `()` instead of `{}` after `\ln`
* [Matrix or column vector](): use `\begin{bmatrix}` for square brackets and `\begin{Bmatrix}` for curly brackets.


* [subscript and superscript](https://www.overleaf.com/learn/latex/Subscripts_and_superscripts)
* [citation doc](http://texdoc.net/texmf-dist/doc/latex/cite/cite.pdf)
* [overleaf-BibLatex](https://www.overleaf.com/learn/latex/Articles/Getting_started_with_BibLaTeX)
* [video-insert an algorithm](https://www.youtube.com/watch?v=l7Z7tvCkQrg) <br/>
Note:for `\State` in algorithm, use`$...$` for the whole line of math expression and it helps with line break and alignment
* [for loop](https://tex.stackexchange.com/questions/56871/how-to-format-for-loop)
* [symbol list](https://mirror.unpad.ac.id/ctan/info/symbols/comprehensive/symbols-a4.pdf)

* [subfigure placement](https://tex.stackexchange.com/questions/333249/controlling-subfigure-captions-and-subfigure-placement)

* [Page numbering](https://www.overleaf.com/learn/latex/Page_numbering)
* customize the `\tableofcontents` by [`\addcontentsline`](http://www.emerson.emory.edu/services/latex/latex_162.html)



* Debug: `erroneous nesting of equation structures` <br/>
when use `\begin{align}` environment, use it separately, no need to put in `\equation` environment.


## 5.15
1. Read [Semantic segmentation](https://medium.com/nanonets/how-to-do-image-segmentation-using-deep-learning-c673cc5862ef), which train 'encoder' and 'decoder' network
2. Finish the masking. <br/>
	* use [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) instead of 'DBScan'
	* use `hull` and `fillpoly` instead of `approxPolyDP` that gives zig-zag shape lines for unordered velodyne points
	* the overlapping between front car and back car will affect the choice in clustering <br/>
	do clustering and rendering from front to back, remove selected points from `velo_img`
	* use idx to trace `velo_img`, simplify the code
*To follow up*
* [inpainint in opencv](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_photo/py_inpainting/py_inpainting.html)
* [fill holes in opencv](https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/)
*Python*
* Inefficient way:
```
if pt_img [0]>0 and pt_img[0]<img_width and pt_img[1]<img_height:
cv2.circle(img, (np.int32(pt_img[0]),np.int32(pt_img[1])), 2, (0, 0, 255), -1)
```
Efficient:
min_max `pt_img[0] = min(img_width-1, max(0, pt_img[0]/pt_img[2]))`

* ind = np.argsort()
ind = -ind # to reverse
* nonzero = np.nonzero\[x, y, :]
* np.where
* [delete array elelment](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.delete.html), single element or by index array
* delete dictionary elemeny `del dict[key]`
* to test if each element in an numpy array lies between two values?
```
a = numpy.array([1,2,3,4,5])
(a > 1).all() and (a < 5).all()
if you want the acutal array of truth vaues, just use:
(a > 1) & (a < 5)
```
*Debug*
* `error: (-215) p.checkVector(2, CV_32S) >= 0 in function fillPoly` for `fillPoly` or `polyLines`<br/> 
Soln: 
	* check array datatype first <br/>
	e.g. `cv2.polylines(img, [points], 1, (255,255,255))` change `[points]` to `np.array([points], dtype=np.int32)` or `np.int32([points])`
	* check the length of `[point]`, single point will raise abovementioned error
	
## 5.16
*To Do*
1. Study and make masks for [`nuscenes` dataset](https://github.com/nutonomy/nuscenes-devkit)
2. Follow up: use matplot and jupyter

1. Write code for using NuScenes data, create `myNuScenes` and `myNuScenesExplorer` classes in `mynuscenes.py` and process the data in `make_dataset_nu.py`
	* use 2D array to store data instead of parsing into a dictionary for each car
	* simpler way to parse data into dictionary `car = dict(x.split(':') for x in str(box).split(','))`, but `,` in array affects splitting
	

*Python*
* To convert PIL to opencv, `img = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)`

*Debug*
* `ImportError: with error 'is not a package'` <br/>
possible reason: python file and floder have the same name. <br/>
Soln: `import sys
sys.path.insert(0,'/media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/nuscenes/nuscenes-devkit/python-sdk')` add the parent folder of the package by `sys.path.insert`
* `Import error: cannot import name` <br/>
possible reason: mutual inmport or wrong spelling (lowercase or uppercase), pls check carefully


## 5.17
1. Read dataset ro find how group bounding boxes for one car together. <br/>
Try `instance` first, but it is convenient for tracking, but does not contain instantaneous translation and rotation information. <br/>
`selected_anntokens` in `get_sample` function helps to identify which car it is. <br/>
Next step: find how to get all annotations within one sample
2. TODO: need to append to velo_img the other dimension, height and sqrt(x^2 + y^2)

*Note*
* [Quaternion](https://www.youtube.com/watch?v=zjMuIxRvygQ) <br/>
q = cos(theta/2) + sin(theta/2)(x\*i + y\*j + z\*k), where (x\*i + y\*j + z\*k) is unit vector of the rotation axis <br/>
To rotate point P around specified axis by specified angle, P' = q \* P \* q_inv

## 5.21
1. Make dataset for nuscenes, but the Lidar points are sparse to create poly. <br/>
Rei suggests to use [segnet](https://github.com/alexgkendall/SegNet-Tutorial)
2. Write final report

*Python*
* To check if an object is an instance of a given class or of a subclass of it: use the built-in function isinstance. <br/>
```
if isinstance(obj, MyClass):
     print "obj is my object"
```

## 5.22 
1. Finish logbook
2. Follow [Segnet Tutorial](http://mi.eng.cam.ac.uk/projects/segnet/tutorial.html) <br/>
[segnet-caffe](https://github.com/alexgkendall/SegNet-Tutorial)
3. Write `nuscenes_dmo.py` to generate segmentation data for `CAM_FRONT` images. To run it, do `sunardi@sunardi:/media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/SegNet$ python Scripts/nuscenes_demo.py`

*Debug*
* When install and compile [Caffe](http://caffe.berkeleyvision.org/installation.html#compilation), encounter `fatal error: hdf5.h: No such file or directory` <br/>
Soln: [check the installation and export CPATH](https://ahmedibrahimvt.wordpress.com/2017/02/19/fatal-error-hdf5-h-no-such-file-or-directory/)
* Compiling `Caffe`, encounter `nvcc fatal   : Unsupported gpu architecture 'compute_20'` <br/>
Soln: Remove or comment the line `-gencode arch=compute_20,code=sm_20 and -gencode arch=compute_20,code=sm_21` in Makefile.config.
* Compiling `Caffe`, encounter `.build_release/lib/libcaffe.so: undefined reference to "cv::imread(cv::String const&, int)"` <br/>
Since I am using OpenCV3, set the `OPENCV_VERSION` variable in `Makefile.config`
* Compiling `Caffe`, encounter `caffe with OPENCV 3.3.0: undefined reference to 'TIFFReadDirectory@LIBTIFF_4.0'` <br/>
Soln: some say remake OpenCV with [`tiff = ON`](https://github.com/BVLC/caffe/issues/4436), but for me, I just uncomment the `OPENCV version` in `Makeconfig`, **delete the previous cmake folder**, and do `make all` again. Previous cmake files amy mess up so the error stays.
* After successful compilation, do `make pycaffe` and `make distribute` no error. <br/>
However, when `python >>import caffe`, encounter `ImportError: No module named caffe` <br/>
Soln: only making and compiling the caffe is not enough, need to provide the caffe's path to Python, <br/>
In `~/.bashrc` add `export PYTHONPATH=$PYTHONPATH:/media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/SegNet/caffe/distribute/python` <br/>
if encounter `ImportError: libcaffe.so.1.0.0: cannot open shared object file: No such file or directory`, <br/>
in `~/.bashrc` add `export LD_LIBRARY_PATH=/media/sunardi/5c4c121b-5f45-4689-b8c3-f44b3e5ef4da/ruihan/SegNet/caffe/distribute/lib:$LD_LIBRARY_PATH` <br/>
finally can import caffe in python 2.7 successfully
* Change default python path `alias python=/usr/bin/python2.7`, but maybe need to redo when opening a new terminal

* run SegNet and encounter error `bn_param` import error <br/>
Soln: should install `segnet-caffe` instead of the "bare" `BVLC caffe`

* `make all` for `segent-caffe` encounter `undefined reference to cv::imread(cv::String const&, int)' `
Set `OPENCV_VERSION := 3` and uncommenting `USE_PKG_CONFIG` in the `Makefile.config` followed by `make all`

* `make test` encounter `src/caffe/layers/contrastive_loss_layer.cpp:56:30: error: no matching function for call to ‘max(float, double)’ Dtype dist = std::max(margin - sqrt(dist_sq_.cpu_data()[i]), 0.0); ` <br/>
Soln: Modify Line 56 in `contrastive_loss_layer.cpp` to  `Dtype dist = std::max(margin - (float)sqrt(dist_sq_.cpu_data()[i]), Dtype(0.0));`


*Notes from Rei*
* use [the website](https://arnon.dk/matching-sm-architectures-arch-and-gencode-for-various-nvidia-cards/) to check the version of the GPU card and specify corresponding version for `gencode sm-xx`
* cudnn is a library to speed up cuda. [Installation instructions](https://askubuntu.com/questions/767269/how-can-i-install-cudnn-on-ubuntu-16-04)


*Reminders*
* git clone `caffe-segnet` to `SegNet` and rename it as `caffe` to keep consistent with `PYTHONPATH`

*To do*
* write 4\*4 `quat2rot_center` in `data_class` but not using it
* Swop the left and right poly in `mynuscenes`
* the shape does not look so nice, may need to add fornt and back ordering

## 5.23
1. Finish with generating data for CAM_FRONT. Problem solving for choosing "visible polys",. Read for quaterion, Rei recommends Ros `quat to euler` but I am using Python3. Find another rotation_matrix to euler angle function. <br/>
Sorry to bother Rei too much by asking questions, but he is so helpful to save me from stucking there for another day. <br/>
Finally solve the program by get yaw theta from `euler_angle[1]` and add `pi` to it for coordinate transformation. For cars in opposite direction,both front/back and left/right are reverted, but not affecting the rendering too much.

2. Prepare slides for the presentation. Practice, practice.
*Python*
* elementwise compare two array `(A==B).all()`
* Opencv [morphology, e.g. dilation, erosion](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html)
* [http://kieranwynn.github.io/pyquaternion/](http://kieranwynn.github.io/pyquaternion/) [scipy transformation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html)
* [quaterion in ROS](https://answers.ros.org/question/69754/quaternion-transformations-in-python/) [quaterion message](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html)
* [rotation matrix to euler angle](https://www.learnopencv.com/rotation-matrix-to-euler-angles/)

## 5.24 
1. Try Carla
2. Ask Ee Wei for starting points for C++: <br/>
tutorial: cplusplus.com <br/>
key points: class, stream, STL container(std::vector), way of defining `const`
3. Presentation

## 5.30 - 5.31
1. Finish report
2. Continue to generate the masks

## 6.3 
1. Sentosa with testing team <br/>
Record the traffic, different types of vehicles and abonormal behaviour like road hogging



