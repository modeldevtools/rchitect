from ctypes import c_int
from .internals import PROTECT, UNPROTECT, Rf_mkString, R_ParseVector, R_NilValue
from .internals import TYPEOF, EXPRSXP, LENGTH, Rf_eval, VECTOR_ELT


def R_ParseEvalString(buf, env):
    s = PROTECT(Rf_mkString(buf))
    status = c_int()
    ps = PROTECT(R_ParseVector(s, -1, status, R_NilValue))
    if (status.value != 1 or TYPEOF(ps) != EXPRSXP or LENGTH(ps) != 1):
        UNPROTECT(2)
        raise Exception("parse error")

    val = Rf_eval(VECTOR_ELT(ps, 0), env)
    UNPROTECT(2)
    return val