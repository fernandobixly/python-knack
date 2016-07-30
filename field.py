class Field(object):
  def __init__(self, data):
    self.data = data
  
  def __getattr__(self, name):
    try:
      return self.data[name]
    except(KeyError):
      raise AttributeError("'{object_name}' object has no attribute '{attr_name}'"\
        .format(object_name=self.__class__.__name__, attr_name=name))

  def __repr__(self):
    return "<{context_name}.{class_name}({data_str})>".format(context_name=__name__,\
      class_name=self.__class__.__name__,\
      data_str=str(self.data))
