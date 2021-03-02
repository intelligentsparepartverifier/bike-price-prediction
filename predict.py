
import numpy as np
import pickle


gbr = pickle.load(open("models/gbr.pickle.dat", "rb"))

cols = ['Bike_company',
 'Manufactured_year',
 'Engine_warranty',
 'CC(Cubic capacity)',
 'Fuel_Capacity',
 'Engine_type_Boxer',
 'Engine_type_Dual_Stroke',
 'Engine_type_Oxidiser_Air_inlet',
 'Engine_type_Single',
 'Engine_type_Two-Stroke',
 'Engine_type_V-twin',
 'Fuel_type_Electricity',
 'Fuel_type_Petrol',
 'Speedometer_Analog',
 'Speedometer_Digital',
 'Electric_Start_No',
 'Electric_Start_Yes',
 'Number_of_Gears_4_Manual',
 'Number_of_Gears_5_Manual',
 'Number_of_Gears_6_Manual',
 'Number_of_Gears_Automatic']



#setting the inputs to fit the model to predict
def input_to_one_hot(data):
    # initialize the target vector with zero values
    enc_input = np.zeros(21)
    # set the numerical input as they are
    enc_input[0] = data['Bike_company']
    enc_input[1] = data['Manufactured_year']
    enc_input[2] = data['Engine_warranty']
    enc_input[3] = data['CC(Cubic capacity)']
    enc_input[4] = data['Fuel_Capacity']

    ##################### Engine_type #########################
    # redefine the the user inout to match the column name
    redefinded_user_input = 'Engine_type_' + data['Engine_type']
    # search for the index in columns name list
    Engine_type_column_index = cols.index(redefinded_user_input)
    # fullfill the found index with 1
    enc_input[Engine_type_column_index] = 1

    ##################### Fuel_type ####################
    # redefine the the user inout to match the column name
    redefinded_user_input = 'Fuel_type_' + data['Fuel_type']
    # search for the index in columns name list
    Fuel_type_column_index = cols.index(redefinded_user_input)
    # fullfill the found index with 1
    enc_input[Fuel_type_column_index] = 1

    ##################### Speedometer ####################
    # redefine the the user inout to match the column name
    redefinded_user_input = 'Speedometer_' + data['Speedometer']
    # search for the index in columns name list
    Speedometer_column_index = cols.index(redefinded_user_input)
    # fullfill the found index with 1
    enc_input[Speedometer_column_index] = 1

    ##################### Electric_Start ####################
    # redefine the the user inout to match the column name
    redefinded_user_input = 'Electric_Start_' + data['Electric_Start']
    # search for the index in columns name list
    Electric_Start_column_index = cols.index(redefinded_user_input)
    # fullfill the found index with 1
    enc_input[Electric_Start_column_index] = 1

    ##################### Number_of_Gears ####################
    # redefine the the user inout to match the column name
    redefinded_user_input = 'Number_of_Gears_' + data['Number_of_Gears']
    # search for the index in columns name list
    Number_of_Gears_column_index = cols.index(redefinded_user_input)
    # fullfill the found index with 1
    enc_input[Number_of_Gears_column_index] = 1
    
    return enc_input


def predict_price(data):
    a = input_to_one_hot(data)

    price_pred = gbr.predict([a])
    return(price_pred[0])
