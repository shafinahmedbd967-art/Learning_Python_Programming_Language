# boolean conversion example

value1 = bool(1)   # 1 ke boolean e convert korle True hoy, karon 1 holo non-zero number
value2 = bool(0)   # 0 ke boolean e convert korle False hoy, karon 0 holo zero number

print(value1)      # value1 er value
print(value2)      # value2 er value
print(bool(""))    # empty string ke boolean e convert korle False hoy, karon empty string holo falsey value
print(bool("Hello")) # non-empty string ke boolean e convert korle True hoy, karon non-empty string holo truthy value


"""
output:
True
False
False
True
"""
