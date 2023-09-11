from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.snake = {'viper'}
rigid.location = {'px5y6', 'px3y6', 'px2y3', 'px0y0', 'px2y5', 'px0y3', 'px6y5', 'px4y6', 'px4y0', 'px3y1', 'px1y3', 'px6y2', 'px3y0', 'px5y5', 'px6y6', 'px5y2', 'px6y0', 'px0y4', 'px1y4', 'px0y5', 'px3y5', 'px1y2', 'px5y0', 'px4y4', 'px2y0', 'px1y0', 'px4y1', 'px2y1', 'px4y2', 'px4y3', 'px0y6', 'px6y3', 'px5y1', 'px3y2', 'px4y5', 'px2y4', 'px2y2', 'px5y4', 'px1y5', 'px6y4', 'px3y4', 'px3y3', 'px5y3', 'px1y6', 'px2y6', 'px0y2', 'px6y1', 'px1y1', 'px0y1'}
state.head = { ('viper', 'px1y0'), }
state.connected = { ('viper', 'px1y0', 'px0y0'), }
state.tail = { ('viper', 'px0y0'), }
state.mouse_at = { ('px2y4',), ('px5y3',), ('px1y4',), ('px4y3',), }
state.occupied = { ('px0y1',), ('px4y5',), ('px1y4',), ('px5y5',), ('px1y0',), ('px0y2',), ('px2y5',), ('px6y2',), ('px5y1',), ('px2y4',), ('px6y3',), ('px1y5',), ('px0y3',), ('px0y0',), ('px3y2',), ('px4y3',), ('px0y5',), ('px0y4',), ('px6y5',), ('px3y1',), ('px6y4',), ('px3y4',), ('px3y3',), ('px5y4',), ('px6y1',), ('px3y5',), ('px5y3',), ('px2y1',), ('px4y4',), }
rigid.adjacent = { ('px0y6', 'px0y5'), ('px1y3', 'px2y3'), ('px0y1', 'px1y1'), ('px1y4', 'px0y4'), ('px6y0', 'px5y0'), ('px4y4', 'px3y4'), ('px1y1', 'px1y0'), ('px4y5', 'px3y5'), ('px6y2', 'px6y1'), ('px3y4', 'px2y4'), ('px5y2', 'px6y2'), ('px2y6', 'px1y6'), ('px5y3', 'px5y4'), ('px1y3', 'px1y4'), ('px3y2', 'px4y2'), ('px2y4', 'px1y4'), ('px2y0', 'px1y0'), ('px1y2', 'px1y1'), ('px5y1', 'px5y2'), ('px4y3', 'px4y2'), ('px3y3', 'px3y4'), ('px1y0', 'px2y0'), ('px4y1', 'px4y2'), ('px5y6', 'px4y6'), ('px4y5', 'px4y6'), ('px4y3', 'px5y3'), ('px4y0', 'px5y0'), ('px0y1', 'px0y0'), ('px2y1', 'px2y2'), ('px6y4', 'px6y5'), ('px4y6', 'px4y5'), ('px6y3', 'px5y3'), ('px2y1', 'px2y0'), ('px3y1', 'px3y2'), ('px1y4', 'px1y3'), ('px4y2', 'px3y2'), ('px1y5', 'px1y6'), ('px3y2', 'px2y2'), ('px6y6', 'px5y6'), ('px1y2', 'px2y2'), ('px3y5', 'px3y4'), ('px4y6', 'px3y6'), ('px6y6', 'px6y5'), ('px5y3', 'px4y3'), ('px0y3', 'px0y4'), ('px4y1', 'px5y1'), ('px2y4', 'px3y4'), ('px0y6', 'px1y6'), ('px4y1', 'px4y0'), ('px2y3', 'px2y2'), ('px3y3', 'px4y3'), ('px4y6', 'px5y6'), ('px5y6', 'px5y5'), ('px1y5', 'px2y5'), ('px0y1', 'px0y2'), ('px4y0', 'px4y1'), ('px2y2', 'px2y1'), ('px5y5', 'px6y5'), ('px2y5', 'px1y5'), ('px0y0', 'px0y1'), ('px5y1', 'px6y1'), ('px6y3', 'px6y4'), ('px2y5', 'px2y6'), ('px4y3', 'px4y4'), ('px1y3', 'px0y3'), ('px2y6', 'px2y5'), ('px4y0', 'px3y0'), ('px0y2', 'px1y2'), ('px6y5', 'px6y4'), ('px6y1', 'px6y2'), ('px1y1', 'px2y1'), ('px5y1', 'px4y1'), ('px0y3', 'px1y3'), ('px6y1', 'px5y1'), ('px1y2', 'px0y2'), ('px2y6', 'px3y6'), ('px5y5', 'px4y5'), ('px2y5', 'px3y5'), ('px0y2', 'px0y1'), ('px5y4', 'px5y3'), ('px6y3', 'px6y2'), ('px5y1', 'px5y0'), ('px4y2', 'px5y2'), ('px6y5', 'px5y5'), ('px5y0', 'px5y1'), ('px5y0', 'px4y0'), ('px2y0', 'px2y1'), ('px2y2', 'px1y2'), ('px2y1', 'px3y1'), ('px1y5', 'px1y4'), ('px3y5', 'px2y5'), ('px4y4', 'px4y5'), ('px4y5', 'px5y5'), ('px3y3', 'px2y3'), ('px3y0', 'px2y0'), ('px3y6', 'px2y6'), ('px4y1', 'px3y1'), ('px0y4', 'px1y4'), ('px6y4', 'px6y3'), ('px2y5', 'px2y4'), ('px5y5', 'px5y6'), ('px3y5', 'px3y6'), ('px3y0', 'px4y0'), ('px3y2', 'px3y3'), ('px4y3', 'px3y3'), ('px6y1', 'px6y0'), ('px0y0', 'px1y0'), ('px1y1', 'px1y2'), ('px3y4', 'px4y4'), ('px5y2', 'px4y2'), ('px2y3', 'px3y3'), ('px1y4', 'px1y5'), ('px4y2', 'px4y3'), ('px0y4', 'px0y5'), ('px3y6', 'px3y5'), ('px5y4', 'px6y4'), ('px6y4', 'px5y4'), ('px1y1', 'px0y1'), ('px5y2', 'px5y3'), ('px0y5', 'px0y6'), ('px2y2', 'px3y2'), ('px5y0', 'px6y0'), ('px2y4', 'px2y3'), ('px4y4', 'px5y4'), ('px5y6', 'px6y6'), ('px1y6', 'px0y6'), ('px5y4', 'px4y4'), ('px1y2', 'px1y3'), ('px6y2', 'px5y2'), ('px1y3', 'px1y2'), ('px1y0', 'px1y1'), ('px2y2', 'px2y3'), ('px4y5', 'px4y4'), ('px2y3', 'px2y4'), ('px2y3', 'px1y3'), ('px5y2', 'px5y1'), ('px3y3', 'px3y2'), ('px5y4', 'px5y5'), ('px5y3', 'px5y2'), ('px3y1', 'px2y1'), ('px3y5', 'px4y5'), ('px3y2', 'px3y1'), ('px0y2', 'px0y3'), ('px3y6', 'px4y6'), ('px2y1', 'px1y1'), ('px3y1', 'px4y1'), ('px4y2', 'px4y1'), ('px6y0', 'px6y1'), ('px2y4', 'px2y5'), ('px0y3', 'px0y2'), ('px6y2', 'px6y3'), ('px3y4', 'px3y5'), ('px4y4', 'px4y3'), ('px5y5', 'px5y4'), ('px3y4', 'px3y3'), ('px0y5', 'px1y5'), ('px1y5', 'px0y5'), ('px1y4', 'px2y4'), ('px2y0', 'px3y0'), ('px3y1', 'px3y0'), ('px0y4', 'px0y3'), ('px1y6', 'px1y5'), ('px1y0', 'px0y0'), ('px6y5', 'px6y6'), ('px1y6', 'px2y6'), ('px3y0', 'px3y1'), ('px5y3', 'px6y3'), ('px0y5', 'px0y4'), }

task_list = [('hunt',)]
