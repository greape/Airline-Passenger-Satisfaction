import streamlit as st
import pickle
import json
import pandas as pd
import numpy as np

with open("list_num_columns.txt", 'r') as file_1:
    list_num_skew_columns = json.load(file_1)

with open("list_cat_nominal_columns.txt", "r") as file_2:
    nom_col_skew = json.load(file_2)

with open("list_cat_ordinal_columns.txt", "r") as file_3:
    ord_col_skew = json.load(file_3)

with open("best_pipeline.pkl", "rb") as file_4:
    best_pipeline = pickle.load(file_4)

def run():
    # create form 
    with st.form("form"):
        age = st.number_input("age",
                            min_value= 5,
                            max_value= 90,
                            value=30,
                            step=2) 
        flight_distance = st.number_input("flight distance",
                            min_value= 31,
                            max_value= 5000,
                            value=850,
                            step=10) 
        departure_delay_in_minutes = st.number_input("departure delay in minutes",
                            min_value= 0,
                            max_value= 1600,
                            value=200,
                            step=10) 
        arrival_delay_in_minutes = st.number_input("arrival delay in minutes",
                            min_value= 0,
                            max_value= 1600,
                            value=200,
                            step=10) 

        st.markdown("---")
        gender = st.radio("gender",("Male","Female"),index= 0)
        customer_type = st.radio("customer type",("Loyal customer","disloyal customer"),index= 0)
        type_of_travel = st.radio("type of travel",('Personal Travel', 'Business travel'),index= 0)
        class_flight = st.radio("class flight",('Eco Plus', 'Business', 'Eco'),index= 0)
        
        st.markdown("---")
        inflight_wifi_service = st.radio("inflight_wifi_service",(0,1,2,3,4,5),index= 0)
        departure_arrival_time_convenient = st.radio("departure/arrival_time_convenient",(0,1,2,3,4,5),index= 0)
        ease_of_online_booking = st.radio("ease_of_online_booking",(0,1,2,3,4,5),index= 0)
        gate_location = st.radio("gate_location",(0,1,2,3,4,5),index= 0)
        food_and_drink = st.radio("food_and_drink",(0,1,2,3,4,5),index= 0)
        online_boarding = st.radio("online_boarding",(0,1,2,3,4,5),index= 0)
        seat_comfort = st.radio("seat_comfort",(0,1,2,3,4,5),index= 0)
        inflight_entertainment = st.radio("inflight_entertainment",(0,1,2,3,4,5),index= 0)
        on_board_service = st.radio("on_board_service",(0,1,2,3,4,5),index= 0)
        leg_room_service = st.radio("leg_room_service",(0,1,2,3,4,5),index= 0)
        baggage_handling = st.radio("baggage_handling",(0,1,2,3,4,5),index= 0)
        checkin_service = st.radio("checkin_service",(0,1,2,3,4,5),index= 0)
        inflight_service = st.radio("inflight_service",(0,1,2,3,4,5),index= 0)
        cleanliness = st.radio("cleanliness",(0,1,2,3,4,5),index= 0)
        st.markdown("---")

        submitted = st.form_submit_button("predict")

    data_inf = {
        "gender" : gender,
        "customer type" : customer_type,
        "age" : age,
        "type of travel" : type_of_travel,
        "class" : class_flight,
        "inflight wifi service" : inflight_wifi_service, 
        "departure/arrival time convenient" : departure_arrival_time_convenient, 
        "ease of online booking" : ease_of_online_booking, 
        "gate location" : gate_location, 
        "food and drink" : food_and_drink, 
        "online boarding" : online_boarding,
        "seat comfort" : seat_comfort, 
        "inflight entertainment" : inflight_entertainment,
        "on-board service" : on_board_service, 
        "leg room service" : leg_room_service, 
        "baggage handling" : baggage_handling, 
        "checkin service" : checkin_service, 
        "inflight service" : inflight_service, 
        "cleanliness" : cleanliness,
        "flight distance" : flight_distance,
        "departure delay in minutes" : departure_delay_in_minutes,
        "arrival delay in minutes" : arrival_delay_in_minutes
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)


    age_category = []
    for x in data_inf["age"]:
        if 6 <= x <= 21:
            age_category.append('Generation z') 
        elif 22 <= x <= 36:
            age_category.append('Millennials')
        elif 37 <= x <= 52:
            age_category.append('Generation X')
        elif 53 <= x <= 73:
            age_category.append('Baby Boomers')
        else:
            age_category.append('Silent Generation')

    data_inf["generation"] = age_category

    if submitted:
        data_inf_num_skew = data_inf[list_num_skew_columns]
        data_inf_cat_nom = data_inf[nom_col_skew]
        data_inf_cat_ord = data_inf[ord_col_skew]
        y_predict_inf = best_pipeline.predict(data_inf)

        st.write("# Satisfaction: ", str(y_predict_inf[0]))

if __name__=="__main__":
    run()