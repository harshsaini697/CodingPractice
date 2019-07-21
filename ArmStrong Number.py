def Amr(inte):
    inte=str(inte)
    final_sum=0
    for c in inte:
        final_sum += amer(c)

    if final_sum==int(inte):
        print("Yes")
    else:
        print("No")


def amer(c):
    c=int(c)
    ca=c*c*c
    return ca

Amr(678)

