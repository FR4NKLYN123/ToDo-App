from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task:
            tasks[index] = new_task
        return redirect('/')
    else:
        if 0 <= index < len(tasks):
            return render_template('edit.html', index=index, task=tasks[index])
        return redirect('/')
    
if __name__ == '__main__':
app.run(host="0.0.0.0", port=port)

s
