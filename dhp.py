from flask import Flask,render_template,request,jsonify
import numpy as np
import pickle 

with open('dt_hyp_model.pkl','rb') as f:
    model=pickle.load(f)
    
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('d_h_p.html')

@app.route('/house_price_prediction',methods=['POST'])
def prediction():
    area=np.array([float(request.form['area'])])
    latitude=np.array([float(request.form['latitude'])])
    longitude=np.array([float(request.form['longitude'])])
    Bedrooms=np.array([float(request.form['Bedrooms'])])
    Bathrooms=np.array([float(request.form['Bathrooms'])])
    Balcony=np.array([float(request.form['Balcony'])])
    Status=np.array([float(request.form['Status'])])
    neworold=np.array([float(request.form['neworold'])])
    Furnished_status=np.array([float(request.form['Furnished_status'])])
    type_of_building=np.array([float(request.form['type_of_building'])])
    Price_sqft=np.array([float(request.form['Price_sqft'])])
    
    city_name_arr=np.zeros(10)
    
    if request.method=='POST':
        
        city_name=request.form['city_name']
        if city_name=='Faridabad':
            city_name_arr[0]=1
        elif city_name=='Ghaziabad':
            city_name_arr[1]=1
        elif city_name=='Greater Noida':
            city_name_arr[2]=1
        elif city_name=='Gurgaon':
            city_name_arr[3]=1
        elif city_name=='New Delhi - Dwarka':
            city_name_arr[4]=1
        elif city_name=='New Delhi - East':
            city_name_arr[5]=1
        elif city_name=='New Delhi - South':
            city_name_arr[6]=1
        elif city_name=='New Delhi - West':
            city_name_arr[7]=1
        elif city_name=='Noida':
            city_name_arr[8]=1
        elif city_name=='uncommon':
            city_name_arr[9]=1
            
        data=np.concatenate([area,latitude,longitude,Bedrooms,Bathrooms,Balcony,Status,neworold,Furnished_status,type_of_building,Price_sqft,city_name_arr])
        result=float(model.predict([data])[0])
        print(result)
        return jsonify(result)
    
if __name__=='__main__':
    app.run(debug=True)
    
