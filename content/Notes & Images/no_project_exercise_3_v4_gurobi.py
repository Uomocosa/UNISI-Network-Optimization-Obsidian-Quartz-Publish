# -*- coding: utf-8 -*-
"""NO_Project_Exercise_3_v4_GUROBI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NRhXYN90YpXokXBjotcfh05JzFLMS0vY
"""

# Commented out IPython magic to ensure Python compatibility.
# >
# <


# %pip install -i https://pypi.gurobi.com gurobipy


import gurobipy as gp
from gurobipy import GRB
import numpy as np
from pprint import pprint
import os
import math
import pandas as pd
from scipy.ndimage.interpolation import shift

""" ### Gurobi license key
 How to get one:
 https://support.gurobi.com/hc/en-us/articles/4409582394769-Google-Colab-Installation-and-Licensing
"""

# Gurobi WLS license file
# Your credentials are private and should not be shared or copied to public repositories.
# Visit https://license.gurobi.com/manager/doc/overview for more information.
WLSACCESSID = '7386b11d-96ac-4e54-95cb-007e197828ad'
WLSSECRET = '3c1403af-66ed-4bf9-82bb-b4d1736ce5d4'
LICENSEID = 827695

# Create environment with WLS license
e = gp.Env(empty=True)
e.setParam('WLSACCESSID', WLSACCESSID)
e.setParam('WLSSECRET', WLSSECRET)
e.setParam('LICENSEID', LICENSEID)
e.start()

# To create the model within the Gurobi environment
# model = gp.Model(env=e)

"""### Input Data"""

stop = 2 #Ts                                              # duration of stop in each station expressed in time slots (each slot 30s)
trains_schedule = [i for i in range(0, 481, 40)]          # schedule of departures in absolute time
max_delay = 2 #Ts                                         # max value of the delay that can be applied to the departure of a train
Ts = 30                                                   # sampling time in seconds

# print(schedule)
# print(total_trip)

"""### Real World Data"""

from google.colab import drive
drive.mount('/content/drive')
data_path = r'drive/MyDrive/[NO] Network Optimization/raw_data'

# data_path = r'raw_data'
line = 'B'
direction = '_CD-LU_'
train_type = 'IC-050'
path = os.path.join(data_path, line + direction + train_type + '_0.csv')

df = pd.read_csv(path)

data1 = df.iloc[5:df.shape[0], [1, 4]]

# SCALE DATA (50%, 75%, ...)
# data1 = data1[:int(len(data1)*0.5)]

consumption = data1['Unnamed: 4'].values.tolist()
time = data1[line].values.tolist()

trip = []
prev = 0
for t in time: 
    if(int(t) >= prev):
        prev = int(t)    
    else:
        trip.append(prev)
        prev = 0
trip.append(prev)

#print(trip)

def resample(consumption, trip, resample_Ts):
    resampled_consumption = []
    resampled_time = []
    n = 0
    for section in trip:
        count = 1
        time = 1
        s = 0
        for i in range(int(section)-1) :
            if (count==resample_Ts):
                resampled_consumption.append(int(s/count)) 
                count = 1
                time += 1
                s = 0
            count += 1
            s += int(consumption[n])
            n += 1
        resampled_consumption.append(int(s/count))
        resampled_time.append(time)
    return resampled_consumption, resampled_time

consumption_vec, station_distances = resample(consumption, trip, Ts)

assert len(consumption_vec) == sum(station_distances)

"""### Usefull derived data
consumption_tensor:
\
$\kern15px$ @ train '$i$'
\
$\kern15px$ @ station '$j$'
\
$\kern15px$ consumtion = consumption_matrix\[$i$\]\[$j$\]
"""

n_trains = len(trains_schedule)
n_stations = len(station_distances)

consumption_tensor = list()
s = 0

for i in range(n_trains):
  s = 0
  temp_i = list()
  for j in range(n_stations):
    # print(s, s + station_distances[j])
    # print(consumption_vec[s : s + station_distances[j]])
    temp_ij = consumption_vec[s : s + station_distances[j]]
    # print(f'consumption_matrix[{i}][{j}] = {consumption_matrix[i][j]}')
    s += station_distances[j]

    temp_i.append(temp_ij)
  consumption_tensor.append(temp_i)

"""### Obvious Problem
(need to comment 'Spice Things Up' section
"""

# n_trains = 2
# n_stations = 2
# consumption_tensor = [
#   [
#     [1, 1, 20,],    # consumption_vec for train[0] station[0]
#     [1, 1, -10,],   # consumption_vec for train[0] station[1]
#   ],
#   [
#     [1, 1, -10,],   # consumption_vec for train[1] station[0]
#     [1, 1, -10,],   # consumption_vec for train[1] station[1]
#   ],
# ]
# station_distances = [3, 3]
# stop = 2 #Ts                                              # duration of stop in each station expressed in time slots (each slot 30s)
# trains_schedule = [i for i in range(0, 2, 1)]             # schedule of departures in absolute time
# max_delay = 2 #Ts                                         # max value of the delay that can be applied to the departure of a train
# Ts = 30      

# # Obvius Result:
#   # max_value = 10
#   # delay at each station:
#   # train[0] = 
#   #   array([  0.,   0.,   0.,   1.,   1.,  20.,   0.,   0.,   0.,   0.,   0.,
#   #           1.,   1., -10.,   0.])
#   # train[1] = 
#   #   array([  0.,   0.,   0.,   1.,   1., -10.,   0.,   0.,   0.,   0.,   0.,
#   #           0.,   1.,   1., -10.])

"""### Spice Things Up

"""

for i in [1, 3]:
  for j in range(n_stations):
    if i == 0:
      consumption_tensor[i][j] = [2.00*x for x in consumption_tensor[i][j]]
      # OLD train, consumes more
    elif i == 3:
      consumption_tensor[i][j] = [0.80*x for x in consumption_tensor[i][j]]
      # NEW train, consumes less

"""### Review Inpput Data:"""

print(f'> Time Stamp (Ts): {Ts} seconds')
print(f'> Stop Time at each station (stop ± max_delay): {stop} ± {max_delay} Ts')
print()
print(f'> trains_schedule = \n\t{trains_schedule}')
print(f'\t# Define at which Ts the train i will depart')
print()
print(f'> station_distances = \n\t{station_distances}')
print(f'\t# How many Ts the trip j takes')
print()
print(f'> consumption_vec = \n\t{consumption_vec}')
print(f'\t# Avarage consumption at each Ts of the resampled_trip')
print()
# print(f'> consumption_tensor : ')
# pprint(consumption_tensor)

"""### Check on input data"""

for i in range(n_trains):
  for j in range(n_stations):
    consumption_vec_j_of_trian_i = consumption_tensor[i][j]
    distance_station_j = station_distances[j]
    assert_msg = f'\n\tlen(consumption_vec_j_of_trian_i) = {len(consumption_vec_j_of_trian_i)}'
    assert_msg += f' is DIFFERENT from '
    assert_msg += f'distance_station_j = {distance_station_j}'
    assert len(consumption_vec_j_of_trian_i) == distance_station_j, assert_msg

assert stop >= max_delay, f'stop ({stop}) cannot be less than max_delay ({max_delay})'

"""### Useful functions"""

def pre_shift_k(vec, k):
  return shift(vec, -k, cval=0)

def normalize_vec(vec, n_anticipo, n_ritardo):
  return np.hstack(([0]*n_anticipo, vec, [0]*n_ritardo))

"""### Calculate the total maximum Time Stamp length:
This will be the dimension each consumption vector will take
"""

rest = stop - max_delay

total_max_Ts = 0 #Ts
possible_total_max_Ts = list()

for i in range(n_trains):
  possible_total_max_Ts.append(trains_schedule[i] + sum(station_distances) + (n_stations-1)*rest + n_stations*(2*max_delay))

total_max_Ts = max(possible_total_max_Ts)

print(f'total_max_Ts = {total_max_Ts} Ts')

"""### Create helper tensors and matrix 
no_delay_station_tensor: consist of all station consumption vector with normal stops
\
max_delay_station_tensor: consist of all station consumption vector with rest + max\_delay

> rest is the amount of time the train stays at each station which is defined as:
$$rest = stop - max\_delay$$
"""

max_delay_consumption_tensor = list()
no_delay_consumption_tensor = list()
possible_combination_of_delays = list()

rest = stop - max_delay

for i in range(n_trains):
  temp_i1 = list()
  temp_i2 = list()
  temp_i3 = list()
  for j in range(n_stations):
    temp_ij1 = [0]*((j)*rest + 2*(j+1)*max_delay) + consumption_tensor[i][j]
    temp_ij2 = consumption_tensor[i][j] + [0]*rest
    temp_ij3 = 2*(j+1)*max_delay + 1
    
    temp_i1.append(temp_ij1)
    temp_i2.append(temp_ij2)
    temp_i3.append(temp_ij3)

  max_delay_consumption_tensor.append(temp_i1)
  no_delay_consumption_tensor.append(temp_i2)
  possible_combination_of_delays.append(temp_i3)

print(f'no_delay_station_tensor[0] = ')
pprint(no_delay_consumption_tensor[0], compact=True, width=120)
print(">> normal delay (stop time at each station), shown as 0s at the END of each vector")
print()

print(f'max_delay_station_matricies[0] = ')
pprint(max_delay_consumption_tensor[0], compact=True, width=120)
print(">> maximum possible delay, shown as 0s at the BEGINNING of each vector")
print()

print(f'possible_combination_of_delays = \n{possible_combination_of_delays}')
print(f'>> the sum of this vector (= {sum(sum(possible_combination_of_delays, []))}) is the number of boolean')
print()

"""### Create a tensor for normalize the size of each consumption vector

All consumption vector have different size, for summing them we need to normalize it.
\
Then using the function previously declared 'normalize_vec' and the following 'anticipo_e_ritardo_tensor' we can add 0s at the beginning and at the end of each consumption vector making it of size (total\_max\_Ts x 1)
"""

anticipo_e_ritardo_tensor = list()

rest = stop - max_delay

for i in range(n_trains):
  increasing_station_delay = 0
  temp_i_list = list()

  for j in range(n_stations):
    no_delay_lenght = len(no_delay_consumption_tensor[i][j])
    max_delay_lenght = len(max_delay_consumption_tensor[i][j])

    anticipo_Ts = increasing_station_delay + trains_schedule[i]
    ritardo_Ts = total_max_Ts - anticipo_Ts - max_delay_lenght
    ar_tuple = (anticipo_Ts, ritardo_Ts)
    # print(f'anticipo_e_ritardo_tensor[{i}][{j}]: ', end='')
    # print(f'anticipo_Ts, ritardo_Ts = {ar_tuple}, max_delay_lenght = {max_delay_lenght}')

    increasing_station_delay += no_delay_lenght
    # anticipo_e_ritardo_tensor[i][j] = ar_tuple
    # print(f'anticipo_e_ritardo_tensor[{i}][{j}] = {anticipo_e_ritardo_tensor[i][j]}\n')
    temp_i_list.append(ar_tuple)
  anticipo_e_ritardo_tensor.append(temp_i_list)


# print()
# for i in range(n_trains):
#   for j in range(n_stations):
#     print(f'anticipo_e_ritardo_tensor[{i}][{j}] = {anticipo_e_ritardo_tensor[i][j]}')

for i in range(n_trains):
  for j in range(n_stations):
    assert_msg = f'\n\tanticipo_e_ritardo_tensor[{i}][{j}] = {anticipo_e_ritardo_tensor[i][j]} must both be >= 0\n'
    assert all(x >= 0 for x in anticipo_e_ritardo_tensor[i][j]), assert_msg
    assert_msg = f'\tsum(anticipo_e_ritardo_tensor[{i}][{j}]) + len(max_delay_consumption_tensor[i][j]) = \n'
    assert_msg += f'\t{sum(anticipo_e_ritardo_tensor[i][j])} + {len(max_delay_consumption_tensor[i][j])}'
    assert_msg += f'\t!= total_max_Ts ({total_max_Ts})\n'
    assert sum(anticipo_e_ritardo_tensor[i][j]) + len(max_delay_consumption_tensor[i][j]) == total_max_Ts

"""### Define all **Constants**
For each combination of train $i$ and station $j$ we have some possibilites according to the question: 'when the train can depart ?'

Each of this possibility can be described by a boolen $b_{ijk}$ multiplied by a vector of consumption for that train $i$ and station $j$, traslated according to the index $k$

A useful example to understand this is at 'Construct the expression for the objective function' section
"""

model = gp.Model(env=e)

ALL_POSSIBLE_TRAINS = list()
for i in range(n_trains):
  ALL_POSSIBLE_STATIONS = list()
  for j in range(n_stations):
    ALL_POSSIBLE_COMBINATIONS = list()
    for k in range(possible_combination_of_delays[i][j]):

      const_ = np.array(normalize_vec(
            pre_shift_k(max_delay_consumption_tensor[i][j], k),
            n_anticipo = anticipo_e_ritardo_tensor[i][j][0],
            n_ritardo = anticipo_e_ritardo_tensor[i][j][1],  ))
      
      assert_msg = f'\n\tindex: i: {i}, j: {j}, k{k}\n'
      assert_msg += f'\tmax_delay_consumption_tensor[{i}][{j}] = {max_delay_consumption_tensor[i][j]}\n'
      assert_msg += f'\tpre_shift_k(max_delay_consumption_tensor[{i}][{j}], {k}) = {pre_shift_k(max_delay_consumption_tensor[i][j], k)}\n'
      assert_msg += f'\anticipo_e_ritardo_tensor[{i}][{j}] = {anticipo_e_ritardo_tensor[i][j]}\n'
      assert_msg += f'\tlen(const_) = {len(const_)} != total_max_Ts ({total_max_Ts})\n'
      # assert const_.shape[0] == total_max_Ts, assert_msg
      assert const_.shape[0] == total_max_Ts, assert_msg
      
      ALL_POSSIBLE_COMBINATIONS.append(const_)
    ALL_POSSIBLE_STATIONS.append(ALL_POSSIBLE_COMBINATIONS)
  ALL_POSSIBLE_TRAINS.append(ALL_POSSIBLE_STATIONS)

# pprint(ALL_POSSIBLE_TRAINS[0][0][0], compact=False, width=120)
# pprint(ALL_POSSIBLE_TRAINS[0][0][1], compact=False, width=120)
# pprint(ALL_POSSIBLE_TRAINS[0][0][2], compact=False, width=120)

"""### Define all **Variables** (all booleans)"""

b = list()
total_number_of_bool_vars = 0

for i in range(n_trains):
  b_i = list()
  for j in range(n_stations):
    b_ij = list()
    for k in range(possible_combination_of_delays[i][j]):
      # print(f'bool_[{i}][{j}][{k}]')
      b_ijk = model.addVar(
          vtype=GRB.BINARY,
          name=f'bool_[{i}][{j}][{k}]')
    
      total_number_of_bool_vars += 1

      b_ij.append(b_ijk)
    b_i.append(b_ij)
  b.append(b_i)
      
model.update()

print(f'len(b) = {len(b)}, n_trains = {n_trains}')
print(f'len(b[0]) = {len(b[0])}, n_station = {n_stations}')
print(f"total number of variables = {total_number_of_bool_vars}")
print()
print(f'b[0][0][0] = {b[0][0][0]}')
print(f'b[-1][0][0] = {b[-1][0][0]}')
print(f'b[0][-1][0] = {b[0][-1][0]}')
print(f'b[0][0][-1] = {b[0][0][-1]}')
print(f'sum(b[0][0]) = {sum(b[0][0])}')

"""### Construct the expression for the objective function
First contruct $N$ consumption expression, one for each train, than sum them all toghether\
(It's equal to sum all the expression toghether, but we belive this to be more clear)

<br>

---

### ~Ex.:
Let's take train T#0 and let's consider only 2 stations (S#0, S#1):
where we have: 
\
> max_delay_consumption_tensor\[0\]\[0\] = \[0, 0, 1, 1, 20\] $\kern15px$ consumptiom for T#0, S#0 
\
> max_delay_consumption_tensor\[0\]\[1\] = \[0, 0, 0, 0, 1, -10, 1\] $\kern15px$ consumptiom for T#0, S#1

Where the 0 at the start of each consumption_tensor are there to represent the max\_possible\_delay

<br>

For the T#0 S#0 we have 3 possibilities (ONLY ONE OF THEM WILL BE TAKEN, following the rules set by the constraints, see below):
> DELAY = -1 : max_delay_consumption_tensor\[0\]\[0\]\[2\] = \[1, 1, 20, 0 , 0\]
\
> DELAY = 0 : max_delay_consumption_tensor\[0\]\[0\]\[1\] = \[0, 1, 1, 20, 0\]
\
> DELAY = +1 : max_delay_consumption_tensor\[0\]\[0\]\[0\] = \[0, 0, 1, 1, 20\]

For the T#0 S#1 we have 5 possibilities (ONLY ONE OF THEM WILL BE TAKEN, following the rules set by the constraints, see below):
> DELAY = -2 : max_delay_consumption_tensor\[0\]\[1\]\[4\] = \[1, -10, 1, 0, 0, 0, 0\]
\
> DELAY = -1 : max_delay_consumption_tensor\[0\]\[1\]\[3\] = \[0, 1, -10, 1, 0, 0, 0\]
\
> DELAY = 0 : max_delay_consumption_tensor\[0\]\[1\]\[2\] = \[0, 0, 1, -10, 1, 0, 0\]
\
> DELAY = +1 : max_delay_consumption_tensor\[0\]\[1\]\[1\] = \[0, 0, 0, 1, -10, 1, 0\]
\
> DELAY = +2 : max_delay_consumption_tensor\[0\]\[1\]\[0\] = \[0, 0, 0, 0, 1, -10, 1\]

<br>

Then, the train_expression\[0\] shall be somenthing like:
\
> b\[0\]\[0\]\[0\] * normalize(max_delay_consumption_tensor\[0\]\[0\]\[0\]) + 
\
> b\[0\]\[0\]\[1\] * normalize(max_delay_consumption_tensor\[0\]\[0\]\[1\]) + 
\
> b\[0\]\[0\]\[2\] * normalize(max_delay_consumption_tensor\[0\]\[0\]\[2\]) + 
\
> b\[0\]\[1\]\[0\] * normalize(max_delay_consumption_tensor\[0\]\[1\]\[0\]) + 
\
> b\[0\]\[1\]\[1\] * normalize(max_delay_consumption_tensor\[0\]\[1\]\[1\]) + 
\
> b\[0\]\[1\]\[2\] * normalize(max_delay_consumption_tensor\[0\]\[1\]\[2\]) + 
\
> b\[0\]\[1\]\[3\] * normalize(max_delay_consumption_tensor\[0\]\[1\]\[3\]) + 
\
> b\[0\]\[1\]\[4\] * normalize(max_delay_consumption_tensor\[0\]\[1\]\[4\])

Where the 'normalize' function make each vector the same length adding 0s at the begining and at the end, according to the 'anticipo\_e\_ritardo\_tensor'
"""

train_expressions = list()
for i in range(n_trains):
  expr = 0
  for j in range(n_stations):
    for k in range(possible_combination_of_delays[i][j]):
      # expr += b[i][j][k]*ALL_POSSIBLE_TRAINS[i][j][k]
      var = b[i][j][k]
      const = ALL_POSSIBLE_TRAINS[i][j][k]
      expr += const*var
  train_expressions.append(expr)

print(f'len(train_expressions): {len(train_expressions)} == n_trains: {n_trains}')
# print()
# print(f'expressions[0] = {train_expressions[0]}')

expression = sum(train_expressions)

assert_msg = f'\n\texpression.shape[0]: {expression.shape[0]} != total_max_Ts: {total_max_Ts}'
assert expression.shape[0] == total_max_Ts, assert_msg

"""### Construct all constraints

1.   Only one between $b_{ij0}, \ b_{ij1}, \ \ldots , \ b_{ijk}$ can be $1$, all the others have to be $0$
$$\sum_{i,j} b_{ijk} = 1$$

2.   Consider $dl_{j}$ the **delay** (in Ts) of the train $i$ at the station $j$ and $dl_{j+1}$ the delay of the same train ($i$) at the station $j+1$, than we must have that:
$$\forall \kern2px i \kern15px dl_{j+1} >= dl_{j} - max\_delay$$
$$\forall \kern2px i \kern15px dl_{j+1} <= dl_{j} + max\_delay$$

3. The only way to create an objective function that searches for $\min(\max(f(x))$ is to create a new variable 'max_value' and assing the following constraints for each *Time Stamp*:
$$
max\_value >= expression[i] \kern 25px 
\text{for}\  i = 0,\ 1,\ \ldots,\ Ts
$$ 
4. The last constraint is to impose that the first train can only be delayed (it's not necessary and can be removed if needed)
So taking the same variable as in constraint (2.) we can say that:
$$\forall \kern2px i \kern15px dl_{j=0} >= 0$$



"""

n_constrs = 0

model.update()

for i in range(n_trains):
  for j in range(n_stations):
    model.addConstr(sum(b[i][j]) == 1, name=f'SUM_[{i}][{j}]')
    n_constrs += 1

# for i in range(n_trains):
#   s = 0
#   for j in range(n_stations):
#     s += sum(b[i][j])
#   model.addConstr(s == 1, name=f'SUM_[{i}][{j}]')
#   n_constrs += 1

model.update()

for i in range(n_trains):
  for j in range(n_stations-1):
    dl_j = 0
    dl_jPLUS1 = 0
    for k in range(possible_combination_of_delays[i][j]):
      dl_j += (max_delay - k)*b[i][j][k]
    for k in range(possible_combination_of_delays[i][j+1]):
      dl_jPLUS1 += (max_delay - k)*b[i][j+1][k]
    #K_{i} : delay station i
    #K_{i+1} : delay station i+1
    model.addConstr(dl_jPLUS1 >= dl_j - max_delay, name=f'LB_[{i}][{j}]')
    model.addConstr(dl_jPLUS1 <= dl_j + max_delay, name=f'UB_[{i}][{j}]')
    n_constrs += 2

# max_value = model.addVar(name='max_value')
# model.addConstr(max_value == gp.max_(expression))
# gp.max_ accepts only Vars or list of Vars, in the first argument,
# not a list of LinExpr

model.update()

max_value = model.addVar(name='max_value')
for t in range(total_max_Ts):
  model.addConstr(expression[t] <= max_value, name=f'MAX_[{t}]')
  n_constrs += 1

for i in range(n_trains):
  delay_first_station = 0
  j = 0
  for k in range(possible_combination_of_delays[i][j]):
    delay_first_station += (max_delay - k)*b[i][j][k]
  model.addConstr(delay_first_station >= 0, name=f'delay_first_station[{i}] must be positive')
  n_constrs += 1


print(f'number of constraints = {n_constrs}')

"""### Solve the problem and display the solutions"""

model.setObjective(max_value, GRB.MINIMIZE)
model.update()
model.write('m.lp')

model.optimize()

"""### Display Solutions I"""

delay_abs = np.zeros((n_trains, n_stations), dtype=int)
delay_rel = np.zeros((n_trains, n_stations), dtype=int)

print(f'total number of variables = {len(model.getVars())}')
print()

values = list()

for v in model.getVars():
    if v.x == 1 and v.VarName != 'max_value':
      index_vec = v.VarName.split('[')
      i = int(index_vec[1][:-1])
      j = int(index_vec[2][:-1])
      k = int(index_vec[3][:-1])
      n_Ts = (max_delay-k)
      delay = n_Ts*Ts

      values.append((i, j, k, delay))

for i in range(n_trains):
  msg = f'train #{i} has the following anticipations/delays at each station: '
  msg += '\n\t['
  for j in range(n_stations):
    for v in values:
      if v[0] == i and v[1] == j:
        delay = v[3]
        msg += str(delay) + ' s , '
  msg += ']'
  print(msg)

"""### Display Solutionts II"""

delay_abs = np.zeros((n_trains, n_stations), dtype=int)
delay_rel = np.zeros((n_trains, n_stations), dtype=int)

for v in model.getVars():
    if v.x == 1 and v.VarName != 'max_value':
      index_vec = v.VarName.split('[')
      i = int(index_vec[1][:-1])
      j = int(index_vec[2][:-1])
      k = int(index_vec[3][:-1])
      n_Ts = (max_delay-k)
      delay = n_Ts*Ts
      print(f'Train #{i} at station #{j} is anticipated/delayed for a total of: {delay} sec ({n_Ts} Ts)')

"""### Display final consupumtion vectors for each train"""

train_expressions = list()
for i in range(n_trains):
  expr = np.zeros(len(ALL_POSSIBLE_TRAINS[i][j][k]))
  for j in range(n_stations):
    for k in range(possible_combination_of_delays[i][j]):
      var = b[i][j][k]
      const = ALL_POSSIBLE_TRAINS[i][j][k]
      if var.x == 1:
        expr += const
  print(f'train[{i}] = ')
  pprint(expr)

"""### Doubts:

1. 
"""