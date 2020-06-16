from planner_engine import PlannerEngine


engine = PlannerEngine()
print('Test case 1:')
engine.travel('Paris', 'Warsaw', ['tue', 'wed'])

engine = PlannerEngine()    # Instantiating another planning engine to renew our knowledge base (data object)
print('Test case 2:')
engine.travel('Hamburg', 'Warsaw', ['tue', 'wed'])

engine = PlannerEngine()    # Instantiating another planning engine to renew our knowledge base (data object)
print('Test case 3:')
engine.travel('Brussels', 'Hamburg', ['tue', 'thu'])

engine = PlannerEngine()    # Instantiating another planning engine to renew our knowledge base (data object)
print('Test case 4:')
engine.travel('Paris', 'Hamburg', ['wed'])


