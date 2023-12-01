from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'p27', 'n15', 'p12', 'p30', 'p9', 'n22', 'o21', 'o28', 'p19', 'p10', 'o15', 'n2', 'n0', 'p22', 'o13', 'n3', 'n5', 'p13', 'p23', 'n21', 'o4', 'p4', 'o6', 'p7', 'n24', 'n26', 'n14', 'n9', 'p1', 'o10', 'o16', 'o29', 'p15', 'p24', 'o11', 'p20', 'n7', 'o17', 'p6', 'o19', 'p16', 'o20', 'n17', 'n18', 'o24', 'o27', 'o7', 'n20', 'n10', 'o25', 'o14', 'o23', 'p17', 'o9', 'p2', 'n23', 'p28', 'o1', 'o30', 'p14', 'n16', 'n6', 'o12', 'n19', 'o22', 'p11', 'n13', 'p21', 'n1', 'o18', 'n27', 'n29', 'o26', 'o5', 'p5', 'n11', 'p25', 'o8', 'n25', 'n8', 'p26', 'p18', 'n28', 'n30', 'n12', 'n4', 'o2', 'p3', 'p29', 'o3', 'p8'}
rigid.count = {'n15', 'n13', 'n20', 'n10', 'n1', 'n27', 'n14', 'n29', 'n9', 'n11', 'n25', 'n22', 'n8', 'n23', 'n28', 'n30', 'n2', 'n7', 'n0', 'n12', 'n4', 'n26', 'n3', 'n5', 'n18', 'n16', 'n21', 'n17', 'n6', 'n19', 'n24'}
rigid.product = {'p27', 'p11', 'p12', 'p30', 'p21', 'p1', 'p9', 'p5', 'p25', 'p15', 'p17', 'p24', 'p2', 'p26', 'p19', 'p20', 'p18', 'p10', 'p8', 'p28', 'p22', 'p6', 'p3', 'p13', 'p23', 'p16', 'p14', 'p29', 'p4', 'p7'}
rigid.order = {'o22', 'o7', 'o25', 'o18', 'o14', 'o26', 'o5', 'o23', 'o10', 'o16', 'o24', 'o29', 'o8', 'o21', 'o9', 'o28', 'o11', 'o15', 'o17', 'o13', 'o1', 'o2', 'o19', 'o30', 'o4', 'o20', 'o3', 'o12', 'o6', 'o27'}
rigid.goal__shipped = set( [('o9',), ('o7',), ('o23',), ('o4',), ('o25',), ('o24',), ('o15',), ('o30',), ('o10',), ('o22',), ('o1',), ('o18',), ('o12',), ('o19',), ('o3',), ('o8',), ('o11',), ('o20',), ('o28',), ('o26',), ('o29',), ('o21',), ('o13',), ('o5',), ('o16',), ('o2',), ('o17',), ('o14',), ('o27',), ('o6',), ] )
rigid.next__count = set( [('n14', 'n15'), ('n11', 'n12'), ('n28', 'n29'), ('n5', 'n6'), ('n25', 'n26'), ('n18', 'n19'), ('n29', 'n30'), ('n17', 'n18'), ('n26', 'n27'), ('n1', 'n2'), ('n0', 'n1'), ('n13', 'n14'), ('n23', 'n24'), ('n24', 'n25'), ('n27', 'n28'), ('n10', 'n11'), ('n3', 'n4'), ('n4', 'n5'), ('n12', 'n13'), ('n8', 'n9'), ('n19', 'n20'), ('n22', 'n23'), ('n7', 'n8'), ('n6', 'n7'), ('n16', 'n17'), ('n9', 'n10'), ('n2', 'n3'), ('n20', 'n21'), ('n15', 'n16'), ('n21', 'n22'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o9',), ('o7',), ('o23',), ('o4',), ('o25',), ('o24',), ('o15',), ('o30',), ('o10',), ('o22',), ('o1',), ('o18',), ('o12',), ('o19',), ('o3',), ('o8',), ('o11',), ('o20',), ('o28',), ('o26',), ('o29',), ('o21',), ('o13',), ('o5',), ('o16',), ('o2',), ('o17',), ('o14',), ('o27',), ('o6',), ] )
rigid.includes = set( [('o3', 'p16'), ('o19', 'p28'), ('o5', 'p18'), ('o8', 'p29'), ('o11', 'p25'), ('o24', 'p15'), ('o9', 'p2'), ('o22', 'p26'), ('o28', 'p28'), ('o26', 'p16'), ('o24', 'p21'), ('o12', 'p5'), ('o13', 'p10'), ('o3', 'p21'), ('o22', 'p17'), ('o20', 'p14'), ('o26', 'p1'), ('o5', 'p23'), ('o15', 'p5'), ('o17', 'p25'), ('o30', 'p26'), ('o18', 'p11'), ('o11', 'p9'), ('o22', 'p14'), ('o18', 'p18'), ('o22', 'p13'), ('o12', 'p3'), ('o27', 'p28'), ('o25', 'p2'), ('o28', 'p8'), ('o10', 'p27'), ('o15', 'p6'), ('o15', 'p8'), ('o15', 'p3'), ('o22', 'p30'), ('o9', 'p8'), ('o14', 'p29'), ('o22', 'p22'), ('o27', 'p24'), ('o21', 'p18'), ('o3', 'p19'), ('o2', 'p10'), ('o7', 'p12'), ('o1', 'p3'), ('o8', 'p4'), ('o23', 'p21'), ('o16', 'p12'), ('o27', 'p17'), ('o10', 'p20'), ('o4', 'p15'), ('o1', 'p11'), ('o12', 'p2'), ('o24', 'p10'), ('o6', 'p26'), ('o28', 'p2'), ('o29', 'p12'), ('o24', 'p7'), ] )
state.started = set( [] )
state.shipped = set( [] )
state.made = set( [] )

task_list = [('plan',)]