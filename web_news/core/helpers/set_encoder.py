def set_encoder(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError
