def multiply(lho, rho):
    if rho >= 3:
        lho_sum = lho + lho
        for x in range(rho):
            lho_sum = lho_sum + lho
    elif rho == 0:
        lho_sum = 0
    elif rho == 1: 
        lho_sum = lho
    elif rho == 2:
        lho_sum = lho + lho
    return lho_sum

print("ssssssss")
v = 200
def multiply2(lho, rho):
    lho_rho_times = 0
    for _ in range(rho):
        lho_rho_times += lho
    return lho_rho_times


def div(lho, rho):
    x = 0
    one_act_difference = lho
    while not one_act_difference == 0:
            one_act_difference += rho  
            x += 1

    return x