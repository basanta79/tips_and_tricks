
cond1 = None
cond2 = 'Hola'
result = None

result = 'Hola' if cond1 is None and cond2 is not None else 'adios'
print(result)

actions = ['create_custodian', 'list_custodians', 'see_custodian_basic_data', 'manage_api_keys']
action_ok = 'see_custodian_basic_data'
action_ko = 'delete_custodian'
print('use in to check if a value is in an array or not.')
print(action_ok in actions)
print(action_ko in actions)

actions = ('create_custodian', 'list_custodians', 'see_custodian_basic_data', 'manage_api_keys')
action_ok = 'see_custodian_basic_data'
action_ko = 'delete_custodian'
print('use in to check if a value is in a set or not.')
print(action_ok in actions)
print(action_ko in actions)





