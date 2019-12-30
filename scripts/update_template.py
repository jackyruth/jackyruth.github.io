import os
filepath = "../metadata/list_of_html.txt"
template_path = "../metadata/templates/template_code.html"
replace_above_cw = "<!-- Page Header -->"
replace_below_cw = "<!-- Footer -->"

def get_middle (filename):
	middle = []
	with open(filename, "r", encoding= 'utf-8') as fp:
		line = fp.readline()
		while(replace_above_cw not in line):
			line = fp.readline()
		line = fp.readline()
		middle.append(line)
		while(replace_below_cw not in line):
			line = fp.readline()
			middle.append(line)
	middle_str = ''.join(middle[:-1])
	return middle_str

def get_title(filename):
	with open(filename, "r", encoding= 'utf-8') as fp:
		line = fp.readline()
		title = line[4:-4]
	return (title,line)

def get_template(filename):
	top = []
	bottom = []
	(title,line) = get_title(filename)
	top.append(line)
	with open(template_path, "r", encoding= 'utf-8') as fp:
		line = fp.readline()
		while("<title>" not in line and "</title>" not in line):
			top.append(line)
			line = fp.readline()
		top.append("<title>" + title + "</title>")
		line = fp.readline()
		while(replace_above_cw not in line):
			top.append(line)
			line = fp.readline()
		top.append(line)
		while(replace_below_cw not in line):
			line = fp.readline()
		while(line):
			bottom.append(line)
			line=fp.readline()
	top_str  = ''.join(top)
	bottom_str = ''.join(bottom)

	return (top_str,bottom_str)

def apply_changes(filename):
	middle_str = get_middle(filename)
	(top_str,bottom_str) = get_template(filename)
	if(filename.strip()[-4:] == "html"):
		with open(filename, "w", encoding= 'utf-8') as fp:
			fp.write(top_str)
			fp.write(middle_str)
			fp.write(bottom_str)
		return 1
	else:
		return 0

def loop_thro_html(path_to_file):
	changed_files = 0
	list_of_changed_files = []
	if(path_to_file[-2:] == "/*"):
		for dirName, subdirList, fileList in os.walk("../"+path_to_file[:-2]):
			for fname in fileList:
				path = dirName + "/" + fname
				list_of_changed_files.append(path.replace("\\","/"))
				changed_files += apply_changes(path.replace("\\","/"))
	else:
		list_of_changed_files.append("../" + path_to_file)
		changed_files += apply_changes("../" + path_to_file)
	print("Done, number of changed files: " + str(changed_files))
	print("List of changed files")
	print('\n'.join(list_of_changed_files))
	print("\n")

list_of_paths = []
with open(filepath, "r") as fp:
	list_of_paths = fp.read().strip().split("\n")
for path in list_of_paths:
	loop_thro_html(path)
