import numpy as np
import pickle
import streamlit as st
  

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def satisfaction_prediction(input_data):

    #input_data = (1,0,53,1,1,1976,2,4,2,3,2,2,2,2,3,4,4,5,5,2)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'Customer is Satisfied'
    else:
        return 'Customer is Dissatisfied'

def main():
    
    
    # giving a title

    #st.title('Satisfaction Prediction Web App')
    st.markdown("<h1 style='text-align: center; color: white;'>Satisfaction Prediction Web App</h1>", unsafe_allow_html=True)
    
    st.header("Check Customer Satisfaction")
    
    
    # getting the input data from the user
    
    form = st.form("Form 1")
    
    form.subheader("Personal Details")
    form.write('<style>div.Widget.row-widget.formRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


    gender_list = ['0=Female/1=Male',0,1]
    Gender = form.selectbox('Select Gender',gender_list)

    
    CustomerType = ['0=Loyal Customer/1=disloyal Customer',0,1]
    CustomerType = form.selectbox('Select Customer Type',CustomerType)

    Age = form.number_input('Age', max_value=100, min_value=1)
    

    TypeofTravel = ['0=Business travel/1=Personal Travel',0,1]
    TypeofTravel = form.selectbox('Select Travel Type',TypeofTravel)


    Class = ['0=Business/1=Eco/2=Eco plus',0,1,2]
    Class = form.selectbox('Select Class Type',Class)
    
    
    
    Flight_Distance = form.number_input('Flight Distance',min_value=1)
    
    form.subheader("Service Satisfaction")
    
    Seat_comfort = form.radio("Seat Comfort",('0','1','2','3','4','5'), horizontal=True)
    DepartureArrival_time_convenient = form.radio("Departure/Arrival time convenient",('0','1','2','3','4','5'), horizontal=True)
    Food_and_drink = form.radio("Food and drink",('0','1','2','3','4','5'), horizontal=True)
    Gate_location = form.radio("Gate location",('0','1','2','3','4','5'), horizontal=True)
    Inflight_wifi_service = form.radio("Inflight wifi service",('0','1','2','3','4','5'), horizontal=True)
    Inflight_entertainment = form.radio("Inflight entertainment",('0','1','2','3','4','5'), horizontal=True)
    Online_support = form.radio("Online support",('0','1','2','3','4','5'), horizontal=True)
    Ease_of_Online_booking = form.radio("Ease of Online booking",('0','1','2','3','4','5'), horizontal=True)
    Onboard_service = form.radio("On-board service",('0','1','2','3','4','5'), horizontal=True)
    Leg_room_service = form.radio("Leg room service",('0','1','2','3','4','5'), horizontal=True)
    Baggage_handling = form.radio("Baggage handling",('0','1','2','3','4','5'), horizontal=True)
    Checkin_service = form.radio("Checkin service",('0','1','2','3','4','5'), horizontal=True)
    Cleanliness = form.radio("Cleanliness",('0','1','2','3','4','5'), horizontal=True)
    Online_boarding = form.radio("Online boarding",('0','1','2','3','4','5'), horizontal=True)


    # code for Prediction
    satisfied = ''
    
    # creating a button for Prediction
    
    btnsubmit = form.form_submit_button('Satisfaction Result')
    
    if btnsubmit:
        if Age == '':
            form.error("Pleace enter age.")
            st.stop()
    
    if btnsubmit:
        if Flight_Distance == '':
            form.error("Pleace enter flight distance.")
            st.stop()
            
    if btnsubmit:
        try:
            int(Age)
            
        except ValueError:
           form.error("Pleace enter numeric values.")
           st.stop()
    
    if btnsubmit:
        try:
            int(Flight_Distance)
            
        except ValueError:
           form.error("Pleace enter numeric values.")
           st.stop()
           
           
    if btnsubmit:
        satisfied = satisfaction_prediction([Gender,CustomerType, Age,TypeofTravel, Class, Flight_Distance, Seat_comfort, DepartureArrival_time_convenient, Food_and_drink, Gate_location, Inflight_wifi_service, Inflight_entertainment, Online_support, Ease_of_Online_booking, Onboard_service, Leg_room_service, Baggage_handling, Checkin_service, Cleanliness, Online_boarding])
        
        
    form.success(satisfied)
    
    
    
    
    
if __name__ == '__main__':
    main()
