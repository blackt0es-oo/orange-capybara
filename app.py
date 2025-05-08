from flask import Flask, request, render_template



app=Flask(__name__)
history = []

class Task:
    def __init__(self, action, due):
        self.action=action
        self.due=due
    
    def format(self):
        return [self.action,self.due]




@app.route('/', methods=['GET','POST'])
def task_info():
    global history
    
    if request.method == 'POST':
        action = request.form['action']
        due = request.form['due']
        task=Task(action=action, due=due).format()
        history.append(task)
    print(f"history: {history}")
    return render_template('home.html', history=history)
    


@app.route('/clear-history', methods=['POST'])
def clear_history():
    global history 
    
    data = request.get_json()
    print(f'Recieved clear-history info: {data['clearHistory']} ')
    if data:
        terminate = data['clearHistory']
        spacer = '|'
        return_len = 0
        for x in range(len(terminate)):
            return_len+=1
        
        index = terminate.index(spacer)
        task=terminate[6:index-1]
        date=terminate[index+1:return_len]
        print(f"task:{task}")
        print(f"date:{date}")

        

        if task in history[0]: # code works however have to work on this section of the code (also have to add in date) (could possibly make a for loop ex: for task, date in history : then we terminate that data)
            print(True)
        else:
            print(False)
        
    print(f"Terminate history: {terminate}")
    return 'Clear history information recieved'

    


if __name__ == "__main__":
    app.run(debug=True)

