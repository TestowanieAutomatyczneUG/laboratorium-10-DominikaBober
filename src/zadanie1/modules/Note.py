
class Note:

    def __init__(self, name: str, note: float):

        try:
            if name is None:
                raise Exception("name can not be None")
            else:
                if name == "":
                    raise Exception("name can not be empty")
                else:
                    if type(name) is str:
                        if 2<=note<=6:
                            self._name = name
                            self._note = note
                        else:
                            raise Exception("note shoud be a number between 2 and 6")
                    else:
                        raise Exception("wrong name type")
        except TypeError:
            raise Exception("wrong note type")
        
    def get_name(self):
        return self._name
    
    def get_note(self):
        return self._note

