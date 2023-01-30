import re
from django.core.validators import RegexValidator

def func_re(a):
    r = []
    for i in a:


        res = bool(re.findall(r'[a-zA-Z]', i))

        r.append(res)

    if True in r:
        return False
    else:
        return True



