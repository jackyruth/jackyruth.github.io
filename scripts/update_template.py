import os

def apply_changes(filename):
	if(filename.strip()[-4:] == "html"):
		print(filename)
	return 0;

def loop_thro_html(path_to_file):
	if(path_to_file[-2:] == "/*"):
		for dirName, subdirList, fileList in os.walk("../"+path_to_file[:-2]):
			for fname in fileList:
				path = dirName + "/" + fname
				apply_changes(path.replace("\\","/"))
	else:
		apply_changes("../" + path_to_file)



filepath = "../metadata/list_of_html.txt"
replace_above_cw = "<!-- Page Header -->"
replace_below_cw = "<!-- Footer -->"

list_of_paths = []
with open(filepath) as fp:
	list_of_paths = fp.read().strip().split("\n")


for path in list_of_paths:
	loop_thro_html(path)
