import inspect
from typing import List

generic_alias_cls = type(List)
list_origin = List.__origin__
def list_subtype(cls):
    if not issubclass(type(cls), generic_alias_cls):
        return None
    if getattr(cls, "__extra__", getattr(cls, "__origin__", None)) is list_origin and cls.__args__:
        return cls.__args__[0]
    return None

class BaseType:
    def _get_attrs(self):
        classes = inspect.getmro(self.__class__)
        props = dict()
        for c in classes:
            if not getattr(c, "__annotations__", None):
                continue
            props.update(
            {
                k:v
                for k, v in c.__annotations__.items()
                if ((inspect.isclass(v) and issubclass(v, BaseType)) 
                    or v in [str, int, float, bool] 
                    or list_subtype(v))
            })

        return props

    def __init__(self, **kwargs):
        attrs = self._get_attrs()

        for k, v in kwargs.items():
            if k in attrs:
                attr_type = attrs[k]
                if inspect.isclass(attr_type) and issubclass(attr_type, BaseType):
                    v = attrs[k](**v)
                    
                subtype = list_subtype(attr_type)
                if subtype and issubclass(subtype, BaseType):
                    v = [subtype(**x) for x in v]
                    print(v)
                setattr(self, k, v)