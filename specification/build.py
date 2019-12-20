from os import listdir
from os.path import isfile, join

# compiles the properties and checks all of them

output_name = 'formulas'
properties_path = './properties/'
properties = [f for f in listdir(properties_path) if isfile(join(properties_path, f))]
properties.sort()

new_file_content = list()
for i in range(len(properties)):
    act_prop_string = '('
    f_handler = open(properties_path + properties[i], 'r')
    for l in f_handler.read().splitlines():
            act_prop_string = act_prop_string + l + '\n'
    act_prop_string = act_prop_string + ')\n\n'
    if i < len(properties) - 1:
        act_prop_string = act_prop_string + '&&\n\n'
    f_handler.close()
    new_file_content.append(act_prop_string)

output_handler = open(output_name, 'w')
output = '\n'.join(new_file_content)
output_handler.write(output)
output_handler.close()