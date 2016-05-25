# coding=utf8


def dict_from_model(model):
    setting = {}
    for key in dir(model):
        if key.isupper():
            setting[key.lower()] = getattr(model, key)
    return setting
