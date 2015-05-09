# Challenge Level: Beginner

# Background: You have a text file with all of the US state names:
#       states.txt: See section_07_(files).  
#
#       You also have a spreadsheet in comma separated value (CSV) format, state_info.csv.  See also section_07_(files)
#       state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py

with open("/Users/graceturke/Documents/hear_me_code/states.txt", "r") as states_txt:
	states = states_txt.read().split("\n")

fullnames = []
abbrevs = []

for index,state in enumerate(states):
	states[index] = state.split("\t")
	abbrevs.append(states[index][0])
	fullnames.append(states[index][1])
#I've created two lists: one of abbreviations and one of full nmaes and transformed states into a list of lists

#HTML for a drop-down menu:
# <select>
# 			<option value="state_abbreviation">Full state name</option>
# </select>

#Print to screen (step 1)
"""
print "<select name=\"states\">"

for i in range(0, len(states)):
	print "\t<option value=\'%s\'>%s</option>" %(states[i][0],states[i][1])

print "</select>"
"""

# Challenge 2: Save the HTML as states.html instead of printing it to screen.  
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.

with open("states.html", "w") as states_html:
	states_html.write("<select name=\"states\">\n")
	for i in range(0, len(states)):
		states_html.write("\t<option value=\'%s\'>%s</option>\n" %(states[i][0],states[i][1]))
	states_html.write("</select>")
	states_html.close()

# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

with open("state_info.csv","r") as state_info_file:
	state_info = state_info_file.read().split("\n")
	state_info.pop(0) #remove header

#print state_info

with open("state_info.html", "w") as state_info_html:
	for index,state in enumerate(state_info):
		state_info[index] = state.split(",")
		state_info_html.write("\n<table border=\"1\">\n<tr>\n<td colspan=\"2\"> %s </td>\n</tr>\n<tr>\n<td> Rank: %s </td>\n<td> Percent: %s </td>\n</tr>\n<tr>\n<td> US House Members: %s </td>\n<td> Population: %s </td>\n</tr>\n</table>\n\n" %(state_info[index][1], state_info[index][0], state_info[index][4], state_info[index][3], state_info[index][2]))
	state_info_html.close()

#To fix: add spaces between tables, remove quotes from display, add commas to numbers, replace "-" with "n/a" for non-states

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>
