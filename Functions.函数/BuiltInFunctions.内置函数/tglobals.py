"""
how globals locals works
"""


def fun_l1():
    school = "Bridge"
    city = "CA"
    print("fun_l1: globals", globals())
    print("fun_l1: locals", locals())
    def fun_l2():
        v_l21 = "vl21"
        v_l22 = "vl22"
        print("fun_l2: globals", globals())
        print("fun_l2: locals", locals())
    fun_l2()

print("outside: globals", globals())
print("outside: locals", locals())
fun_l1()
