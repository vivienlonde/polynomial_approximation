import math

def f_n(x):
    return (1+math.erf(x))/2

def get_polynomial_coefficients_from_string(string_input):
    
    # print(string_input)
    
    last_character_was_e = False
    coef_list = []
    coef_as_string = str()
    
    for c in string_input:
        
        if (c=="+" or c=="-") and (not last_character_was_e):
            try:
                coef_list.append( float(coef_as_string) )
            except ValueError:
                pass
            coef_as_string = str()
        
        if c=="*":
            try:
                coef_list.append( float(coef_as_string) )
            except ValueError:
                pass
            coef_as_string = str()
        
        if c=="e":
            last_character_was_e = True
        else:
            last_character_was_e = False       
        
        coef_as_string += c
        
    return coef_list

def main():
    coeffs = get_polynomial_coefficients_from_string(
        "5.e-1+1.7926252637112485e-1*x-5.1672372506536918e-50*x**2-1.5376264469909196e-3*x**3"
        )
    print(coeffs)

if __name__ == '__main__':
    main()



