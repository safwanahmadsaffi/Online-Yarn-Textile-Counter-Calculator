import streamlit as st

# Unit conversion functions
def convert_weight(value, from_unit, to_unit):
    conversions = {
        'g': {'g': 1, 'kg': 0.001, 'mg': 1000, 'lb': 0.00220462, 'oz': 0.035274},
        'kg': {'kg': 1, 'g': 1000, 'mg': 1e6, 'lb': 2.20462, 'oz': 35.274},
        'mg': {'mg': 1, 'g': 0.001, 'kg': 1e-6, 'lb': 2.20462e-6, 'oz': 3.5274e-5},
        'lb': {'lb': 1, 'kg': 0.453592, 'g': 453.592, 'oz': 16, 'mg': 453592},
        'oz': {'oz': 1, 'g': 28.3495, 'kg': 0.0283495, 'lb': 0.0625, 'mg': 28349.5}
    }
    return value * conversions[from_unit][to_unit]

def convert_length(value, from_unit, to_unit):
    conversions = {
        'meters': {'meters': 1, 'yards': 1.09361},
        'yards': {'yards': 1, 'meters': 0.9144}
    }
    return value * conversions[from_unit][to_unit]

# System parameters
direct_systems = {
    'Tex': {'weight_unit': 'g', 'length_unit': 'meters', 'denominator': 1000},
    'Decitex': {'weight_unit': 'g', 'length_unit': 'meters', 'denominator': 10000},
    'Millitex': {'weight_unit': 'mg', 'length_unit': 'meters', 'denominator': 1000},
    'Kilotex': {'weight_unit': 'kg', 'length_unit': 'meters', 'denominator': 1000},
    'Denier': {'weight_unit': 'g', 'length_unit': 'meters', 'denominator': 9000},
    'Spindle': {'weight_unit': 'lb', 'length_unit': 'yards', 'denominator': 14400},
}

indirect_systems = {
    'English Cotton': {'length_per_hank': 840, 'length_unit': 'yards', 
                      'weight_per_unit': 1, 'weight_unit': 'lb'},
    'French Cotton': {'length_per_hank': 1000, 'length_unit': 'meters',
                     'weight_per_unit': 1, 'weight_unit': 'kg'},
    'Worsted': {'length_per_hank': 560, 'length_unit': 'yards',
               'weight_per_unit': 1, 'weight_unit': 'lb'},
    'Linen (Wet spun)': {'length_per_hank': 300, 'length_unit': 'yards',
                        'weight_per_unit': 1, 'weight_unit': 'lb'},
    'Metric': {'length_per_hank': 1000, 'length_unit': 'meters',
              'weight_per_unit': 1, 'weight_unit': 'kg'},
    'Woolen- Yorkshire Skein': {'length_per_hank': 1536, 'length_unit': 'yards',
                               'weight_per_unit': 6, 'weight_unit': 'lb'},
}

st.title('Universal Yarn Count Calculator')

# System type selection
system_type = st.radio("Select Count System Type", ['Direct', 'Indirect'])

if system_type == 'Direct':
    selected_system = st.selectbox('Select Direct System', list(direct_systems.keys()))
    params = direct_systems[selected_system]
else:
    selected_system = st.selectbox('Select Indirect System', list(indirect_systems.keys()))
    params = indirect_systems[selected_system]

# Input fields
col1, col2 = st.columns(2)
with col1:
    length = st.number_input('Length', min_value=0.0, value=1000.0, step=0.1)
    length_unit = st.selectbox('Length Unit', ['meters', 'yards'])

with col2:
    weight = st.number_input('Weight', min_value=0.0, value=1.0, step=0.1)
    weight_unit = st.selectbox('Weight Unit', ['g', 'kg', 'mg', 'lb', 'oz'])

if st.button('Calculate'):
    try:
        # Convert length to system's unit
        converted_length = convert_length(length, length_unit, params['length_unit'])
        
        # Convert weight to system's unit
        converted_weight = convert_weight(weight, weight_unit, params['weight_unit'])
        
        if system_type == 'Direct':
            # Direct system calculation
            denominator = params['denominator']
            if converted_length <= 0:
                st.error("Length must be greater than zero")
            else:
                count = (converted_weight * denominator) / converted_length
                result = f"**{selected_system} Count**: {count:.2f}"
        else:
            # Indirect system calculation
            lph = params['length_per_hank']
            wpu = params['weight_per_unit']
            if converted_weight <= 0:
                st.error("Weight must be greater than zero")
            else:
                count = (converted_length * wpu) / (converted_weight * lph)
                result = f"**{selected_system} Count**: {count:.2f}'s"
        
        st.success(result)
        
    except ZeroDivisionError:
        st.error("Cannot divide by zero - check your input values")
    except Exception as e:
        st.error(f"Error in calculation: {str(e)}")