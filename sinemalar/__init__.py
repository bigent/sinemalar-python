def str2bool(v, call=False):
    if not call:
        return v.lower() in ("yes", "true", "t", "1")
    else:
        if not v.lower() in ("false", 'null'):
            return v
        else:
            return False