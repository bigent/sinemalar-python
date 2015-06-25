def str2bool(v, call=False):
    if not call:
        return v.lower() in ("yes", "true", "t", "1")
    else:
        try:
            if not v.lower() in ("false", 'null'):
                return v
            else:
                return False
        except:
            if type(v) is list or type(v) is dict:
                return v
            elif type(v) is not list or type(v) is not dict:
                return False