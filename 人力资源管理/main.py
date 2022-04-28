from concurrent.futures import ProcessPoolExecutor
from flask import*
import glob
import pickle

app = Flask(__name__)



@app.route('/')
def index():
    global people,q
    people = {}
    qerry_in = request.values.get('qerry_in')
    print(qerry_in)

    file = open('q','wb')
    pickle.dump(qerry_in,file)

    i = 0
    for file in glob.glob('*.pkl'):
        ifile = open(file,'rb')
        pe = pickle.load(ifile) 
        people[i+1] = pe
        i = i + 1
    print(people)
    

    return render_template('index.html',new = people) 

@app.route('/qerry')

def qerry():
    file = open('q','rb')
    qerry_in = pickle.load(file)
    

    n = 0

    for j in people:
        n = n + 1
        if people[j]['name'] == qerry_in:
            q_people = people[j]
            break

        if n == len(people):
            q_people = []
          
    return render_template('index_qerry.html',q = q_people)




app.run(debug = True)