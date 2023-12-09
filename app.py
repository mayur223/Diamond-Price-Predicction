from flask import Flask, request, render_template

import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    message = "Welcome to my first flask based web application ... !!!"
    return render_template("home.html", message = message)

@app.route('/getResponseRandomForestReg',methods=["GET","POST"])
def getResponseRandomForestReg():
    SIZE = request.form["size"]
    COLOR = request.form["color"]
    CLARITY = request.form["clarity"]
    CUT = request.form['cut']
    POLISH = request.form['polish'] 
    SYMMETRY = request.form['symmetry']
    FLUOR_INTENSITY = request.form["fluor_intensity"]
    DEPTH_PERCENT = request.form["depth_percent"]
    TABLE_PERCENT = request.form["table_percent"]
    RATIO = request.form['ratio']
    # MEAS_LENGTH = request.form['meas_length']
    # MEAS_WIDTH = request.form['meas_width']
    GIRDLE_MIN = request.form['girdle_min']
    GIRDLE_MAX = request.form['girdle_max']
    CULET_SIZE = request.form['culet_size']


    if COLOR == 'Not Selected':
        pass
    elif COLOR == 'D':
        COLOR = 0
    elif COLOR == 'E':
        COLOR = 1
    elif COLOR == 'F':
        COLOR = 2
    elif COLOR == 'G':
        COLOR = 3
    elif COLOR == 'H':
        COLOR = 4
    elif COLOR == 'I':
        COLOR = 5
    elif COLOR == 'J':
        COLOR = 6
    elif COLOR == 'K':
        COLOR = 7
    elif COLOR == 'L':
        COLOR = 8
    elif COLOR == 'M':
        COLOR = 9

    if CLARITY == 'Not Selected':
        pass
    elif CLARITY == 'FL':
        CLARITY = 0
    elif CLARITY == 'IF':
        CLARITY = 1
    elif CLARITY == 'VVS1':
        CLARITY = 2
    elif CLARITY == 'VVS2':
        CLARITY = 3
    elif CLARITY == 'VS1':
        CLARITY = 4
    elif CLARITY == 'VS2':
        CLARITY = 5
    elif CLARITY == 'SI1':
        CLARITY = 6
    elif CLARITY == 'SI2':
        CLARITY = 7
    elif CLARITY == 'SI3':
        CLARITY = 8
    elif CLARITY == 'I1':
        CLARITY = 9
    elif CLARITY == 'I2':
        CLARITY = 10
    elif CLARITY == 'I3':
        CLARITY = 11
    
    if FLUOR_INTENSITY == 'Not Selected':
        pass
    elif FLUOR_INTENSITY == 'NON':
        FLUOR_INTENSITY = 0
    elif FLUOR_INTENSITY == 'FNT':
        FLUOR_INTENSITY = 1
    elif FLUOR_INTENSITY == 'MED':
        FLUOR_INTENSITY = 2
    elif FLUOR_INTENSITY == 'STG':
        FLUOR_INTENSITY = 3
    elif FLUOR_INTENSITY == 'VST':
        FLUOR_INTENSITY = 4
    
    if CUT == 'Not Selected':
        pass
    elif CUT == 'EX':
        CUT = 0
    elif CUT == 'VG':
        CUT = 1
    
    if POLISH == 'Not Selected':
        pass
    elif POLISH == 'EX':
        POLISH = 0
    elif POLISH == 'VG':
        POLISH = 1

    if SYMMETRY == 'Not Selected':
        pass
    elif SYMMETRY == 'EX':
        SYMMETRY = 0
    elif SYMMETRY == 'VG':
        SYMMETRY = 1

    if GIRDLE_MIN == 'Not Selected':
        pass
    elif GIRDLE_MIN == 'M':
        GIRDLE_MIN = 0
    elif GIRDLE_MIN == 'STK':
        GIRDLE_MIN = 1
    elif GIRDLE_MIN == 'STN':
        GIRDLE_MIN = 2
    elif GIRDLE_MIN == 'TK':
        GIRDLE_MIN = 3
    elif GIRDLE_MIN == 'TN':
        GIRDLE_MIN = 4
    elif GIRDLE_MIN == 'VTK':
        GIRDLE_MIN = 5
    elif GIRDLE_MIN == 'VTN':
        GIRDLE_MIN = 6
    elif GIRDLE_MIN == 'XTK':
        GIRDLE_MIN = 7
    elif GIRDLE_MIN == 'XTN':
        GIRDLE_MIN = 8

    if GIRDLE_MAX == 'Not Selected':
        pass
    elif GIRDLE_MAX == 'M':
        GIRDLE_MAX = 0
    elif GIRDLE_MAX == 'STK':
        GIRDLE_MAX = 1
    elif GIRDLE_MAX == 'STN':
        GIRDLE_MAX = 2
    elif GIRDLE_MAX == 'TK':
        GIRDLE_MAX = 3
    elif GIRDLE_MAX == 'TN':
        GIRDLE_MAX = 4
    elif GIRDLE_MAX == 'VTK':
        GIRDLE_MAX = 5
    elif GIRDLE_MAX == 'VTN':
        GIRDLE_MAX = 6
    elif GIRDLE_MAX == 'XTK':
        GIRDLE_MAX = 7
    elif GIRDLE_MAX == 'XTN':
        GIRDLE_MAX = 8

    if CULET_SIZE == 'Not Selected':
        pass
    elif CULET_SIZE == 'M':
        CULET_SIZE = 0
    elif CULET_SIZE == 'N':
        CULET_SIZE = 1
    elif CULET_SIZE == 'S':
        CULET_SIZE = 2
    elif CULET_SIZE == 'VS':
        CULET_SIZE = 3
    

    inputList = [SIZE,COLOR,CLARITY,CUT,SYMMETRY,POLISH,FLUOR_INTENSITY,DEPTH_PERCENT,TABLE_PERCENT,RATIO,GIRDLE_MIN,GIRDLE_MAX,CULET_SIZE]


    if float(SIZE) < 1:
        pickle_in = open('ptr_model1.pkl', 'rb')
        m = pickle.load(pickle_in)
        y_pred_from_pkl = m.predict([inputList])
        y_pred_from_pkl[0] = int(y_pred_from_pkl[0])
        print(y_pred_from_pkl)
    elif float(SIZE) >= 1 and float(SIZE) < 5:
        pickle_in = open('one_up_model1.pkl', 'rb')
        m = pickle.load(pickle_in)
        y_pred_from_pkl = m.predict([inputList])
        y_pred_from_pkl[0] = int(y_pred_from_pkl[0])
        print(y_pred_from_pkl)
    return str(y_pred_from_pkl[0])

if __name__ == '__main__':
    app.run(debug=True)