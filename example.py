char_group = 'Task: work out | Due: tomorrow'

new_list =[]
for char in char_group:
    new_list.append([char])

print(new_list)

due_list = []
for chara in new_list:
   if new_list[0] != "|":
      new_list.pop(0)
   else:
      due_list.extend(new_list)

      
    


