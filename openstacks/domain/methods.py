from ipyhop import Methods
import itertools

def plan__method__1( state, rigid ):
	if any( all( [ ( o, ) in rigid.goal__shipped, not( ( o, ) in state.shipped ), ] ) for ( o, ) in itertools.product( rigid.order, ) ):
		yield [ ( 'open__all__stacks', ), ( 'plan__for__goals', ), ]

def open__a__stack__and__recurse( state, rigid ):
	for n in rigid.count:
		for n1 in rigid.count:
			if all( [ ( n, ) in state.stacks__avail, ( n, n1, ) in rigid.next__count, ] ):
				yield [ ( 'open__new__stack__complex', n, n1, ), ( 'open__all__stacks', ), ]

def done__opening__stacks( state, rigid ):
	for n in rigid.count:
		if all( [ ( n, ) in state.stacks__avail, all( not( ( n, n1, ) in rigid.next__count ) for ( n1, ) in itertools.product( rigid.count, ) ), ] ):
			yield [ ]

def open__new__stack__method__1( state, n, n1, rigid ):
	if all( [ ( n, ) in state.stacks__avail, ( n, n1, ) in rigid.next__count, ] ):
		yield [ ( 'open__new__stack', n, n1, ), ]

def ship__one__order( state, rigid ):
	if any( not( ( o, ) in state.shipped ) for ( o, ) in itertools.product( rigid.order, ) ):
		yield [ ( 'one__step', ), ( 'plan__for__goals', ), ]

def done__shipping__orders( state, rigid ):
	if all( ( order, ) in state.shipped for ( order, ) in itertools.product( rigid.order, ) ):
		yield [ ]

def one__step__make__product( state, rigid ):
	if all( any( [ not( not( ( order, ) in state.shipped ) ), any( all( [ ( order, p, ) in rigid.includes, not( ( p, ) in state.made ), ] ) for ( p, ) in itertools.product( rigid.product, ) ), ] ) for ( order, ) in itertools.product( rigid.order, ) ):
		yield [ ( 'make__a__product', ), ]

def one__step__ship__order( state, rigid ):
	for o in rigid.order:
		if all( [ ( o, ) in rigid.goal__shipped, not( ( o, ) in state.shipped ), all( any( [ not( ( o, p, ) in rigid.includes ), ( p, ) in state.made, ] ) for ( p, ) in itertools.product( rigid.product, ) ), ( o, ) in state.started, ] ):
			yield [ ( 'ship__an__order', o, ), ]

def start__an__order__and__recurse( state, p, rigid ):
	for order in rigid.order:
		if any( all( [ ( o, p, ) in rigid.includes, not( ( o, ) in state.started ), ] ) for ( o, ) in itertools.product( rigid.order, ) ):
			yield [ ( 'start__an__order__for', p, order, ), ( 'start__orders', p, ), ]

def done__starting__orders( state, p, rigid ):
	if all( any( [ not( ( o, p, ) in rigid.includes ), ( o, ) in state.started, ] ) for ( o, ) in itertools.product( rigid.order, ) ):
		yield [ ]

def make__a__product__1( state, rigid ):
	for o in rigid.order:
		for p in rigid.product:
			if all( [ ( o, p, ) in rigid.includes, not( ( o, ) in state.shipped ), not( ( p, ) in state.made ), ] ):
				yield [ ( 'make__product__complex', p, ), ]

def ship__an__order__1( state, order, rigid ):
	for avail in rigid.count:
		for new in rigid.count:
			if all( [ ( order, ) in rigid.goal__shipped, not( ( order, ) in state.shipped ), all( any( [ not( ( order, p, ) in rigid.includes ), ( p, ) in state.made, ] ) for ( p, ) in itertools.product( rigid.product, ) ), ( avail, ) in state.stacks__avail, ( avail, new, ) in rigid.next__count, ] ):
				yield [ ( 'ship__order', order, avail, new, ), ]

def make__product__complex__1( state, p, rigid ):
	yield [ ( 'start__orders', p, ), ( 'make__product', p, ), ]

def start__an__order__for__1( state, p, o, rigid ):
	for avail in rigid.count:
		for avail__prime in rigid.count:
			if all( [ ( o, p, ) in rigid.includes, not( ( o, ) in state.started ), ( avail, ) in state.stacks__avail, ( avail__prime, avail, ) in rigid.next__count, ] ):
				yield [ ( 'start__order', o, avail, avail__prime, ), ]

def start__an__order__1( state, order, rigid ):
	for count in rigid.count:
		for next in rigid.count:
			if all( [ ( next, ) in state.stacks__avail, ( count, next, ) in rigid.next__count, ] ):
				yield [ ( 'start__order', order, next, count, ), ]

def ship__products__1( state, order, rigid ):
	for count in rigid.count:
		for next in rigid.count:
			if all( [ ( count, ) in state.stacks__avail, ( count, next, ) in rigid.next__count, ] ):
				yield [ ( 'ship__order', order, count, next, ), ]

methods = Methods()
methods.declare_task_methods( 'plan', [ plan__method__1, ] )
methods.declare_task_methods( 'open__all__stacks', [ open__a__stack__and__recurse, done__opening__stacks, ] )
methods.declare_task_methods( 'open__new__stack__complex', [ open__new__stack__method__1, ] )
methods.declare_task_methods( 'plan__for__goals', [ ship__one__order, done__shipping__orders, ] )
methods.declare_task_methods( 'one__step', [ one__step__make__product, one__step__ship__order, ] )
methods.declare_task_methods( 'start__orders', [ start__an__order__and__recurse, done__starting__orders, ] )
methods.declare_task_methods( 'make__a__product', [ make__a__product__1, ] )
methods.declare_task_methods( 'ship__an__order', [ ship__an__order__1, ] )
methods.declare_task_methods( 'make__product__complex', [ make__product__complex__1, ] )
methods.declare_task_methods( 'start__an__order__for', [ start__an__order__for__1, ] )
methods.declare_task_methods( 'start__an__order', [ start__an__order__1, ] )
methods.declare_task_methods( 'ship__products', [ ship__products__1, ] )
