
import random
from functools import partial
import time
from typing import List, Dict
from ipyhop import Actions, IPyHOP
import numpy as np
from IPyHDDLER.Snake.domain.methods import graph_shortest_dist
import networkx as nx

# handle snake domain errors
class snake_deviation_handler():

    # planner: the IPyHOP planner
    # rigid: container for all constants
    # active_mouse_ratio: expected ratio of mice that are active every call
    # move_activity_ratio: probability that active mice will move
    def __init__( self, planner, rigid, active_mouse_ratio: float=0.0, move_activity_ratio: float=0.0 ):
        self.planner = planner
        self.rigid = rigid
        self.active_mouse_ratio = active_mouse_ratio
        self.activity_threshold = move_activity_ratio
        self.planner.actions.action_prob[ "move_long" ] = [ 1 - move_activity_ratio, move_activity_ratio, ]
        self.planner.actions.action_prob[ "move_short" ] = [ 1 - move_activity_ratio, move_activity_ratio, ]

    def __call__( self, plan_index, plan, state ):
        # print("CALL")
        # select mice that will try to move
        mouse_at = state.mouse_at
        mouse_locs = np.asarray( [*map(lambda x: x[0], mouse_at)] )
        mouse_chosen_score = np.random.uniform(size=(len(mouse_locs),))
        chosen_mice = mouse_locs[ mouse_chosen_score <= self.active_mouse_ratio ]
        if chosen_mice.size > 0:
            # print("BEFORE")
            # for (_,bodypos,_) in state.connected:
            #     print((bodypos,) in state.occupied)
            # print( mouse_at <= state.occupied )
            # choose open adjacent location at random for each mouse trying to move
            slots_graph = self.rigid.slots
            occupied = state.occupied
            new_locs = set()
            # for each mouse choose a free adjacent space to move that has not been picked this call
            # pick order is random
            # mice will stay in location if no valid moves exist
            np.random.shuffle(chosen_mice)
            for mouse in chosen_mice:
                potential_new_locs = np.asarray( [*filter( lambda x: (x,) not in occupied and x not in new_locs,
                                                         nx.neighbors( slots_graph, mouse ) )] )
                if potential_new_locs.size > 0:
                    new_loc = np.random.choice(potential_new_locs)
                    new_locs.add( new_loc )
                else:
                    new_locs.add(mouse)
            # update state mouse_at and occupied to reflect moves
            state.mouse_at -= {*map(lambda x: (x,), chosen_mice )}
            state.mouse_at |= {*map(lambda x: (x,), new_locs )}
            state.occupied -= {*map(lambda x: (x,), chosen_mice )}
            state.occupied |= {*map(lambda x: (x,), new_locs )}

        #     print("AFTER")
        #     for (_,bodypos,tailpos) in state.connected:
        #         print({(bodypos,),(tailpos,)} <= state.occupied )
        #     print(mouse_at<=state.occupied)
        # print("END CALL")
        return state



