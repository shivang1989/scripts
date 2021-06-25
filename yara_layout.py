
'''
@Author : Shivang 
@Pre-requisite :  Collect strings required for yara rule and save it in a file. (Use this file as input to the script)
@Description : This script automates following - 
	- Opens strings file and prepares yara rule wrapper. 
	- Saves the wrapper in new file. 
	- Opens this new file in sublime.
	
@syntax :
       > python3 yara_layout.py
'''

import subprocess
from colorama import Fore


wrapper_1 = """
rule test_rule : tag1
{
	meta:
		author = "Shivang"
		sample = "XXXXXXXXXXXXXXXXXXXXXX"
	
	strings:"""
wrapper_2 = """
	condition:
		<your condition>
}"""


try:
	strings_file = input("Filename with strings: ")
	f_obj = open(strings_file, "r")
	strings = f_obj.readlines()
	string_buffer = ""

	for item in strings:
		string_buffer = string_buffer + '$str_ = \"'+item.strip("\n")+'\"\n'


	final_wrapper = wrapper_1 + "\n" + string_buffer + "\n" + wrapper_2
	f_obj.close()


	#writing final output back in same file
	output_file = strings_file + "_.yara"
	f_obj2 = open(output_file,"w")
	f_obj2.write(final_wrapper)
	f_obj2.close()


	# firing command to open sublime with yara rule wrapper 
	#if you don't have sublime then use notepad/vim/vi or any other text editor of your choice. 
	command = subprocess.run(["subl", output_file]) 
	print(Fore.CYAN + "New file with extension .yara is now opened with yara rule wrapper!")

except Exception as e:
	print(Fore.RED + "Exception Generated : " + str(e))
