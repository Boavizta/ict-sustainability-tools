import re
tools_data_file = open('./ictst/data/tools.csv', 'r')
tools_data_raw = tools_data_file.read()
tools_data_file.close()
tools_data_raw = re.sub(r'"[^"]*(?:""[^"]*)*"', lambda m: m.group(0).replace('\n', '||').replace('\r\n', '||'), tools_data_raw)
tools_data_file = open('./ictst/data/tools.csv', 'w')
tools_data_file.write(tools_data_raw)
tools_data_file.close()