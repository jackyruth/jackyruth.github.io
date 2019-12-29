import os
filepath = "../metadata/list_of_html.txt"
template_path = "../design/template_code.html"
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


def get_template():
	top = []
	bottom = []
	with open(template_path, "r", encoding= 'utf-8') as fp:
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

def apply_changes(filename,top_str,bottom_str):
	middle_str = get_middle(filename)
	if(filename.strip()[-4:] == "html"):
		print(filename)
		print(top_str)
		print(middle_str)
		print(bottom_str)
		#with open(filename, "w", encoding= 'utf-8') as fp:

		#return 1
	else:
		return 0

def loop_thro_html(path_to_file,top_str,bottom_str):
	if(path_to_file[-2:] == "/*"):
		for dirName, subdirList, fileList in os.walk("../"+path_to_file[:-2]):
			for fname in fileList:
				path = dirName + "/" + fname
				apply_changes(path.replace("\\","/"),top_str,bottom_str)
	else:
		apply_changes("../" + path_to_file,top_str,bottom_str)


(top_str, bottom_str) = get_template()
list_of_paths = []
with open(filepath, "r") as fp:
	list_of_paths = fp.read().strip().split("\n")
for path in list_of_paths:
	loop_thro_html(path,top_str,bottom_str)
