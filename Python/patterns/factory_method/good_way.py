# In this example we are goind to follow several steps to create a set of generic serializers in order to apply to other created objcts


class serializer_JSON:

    def __init__:
        self.current_object = dict()
    
    def add_element(self, key, value):
        self.current_object[key] = value

    def to_str(self):
        return json.dumps(self.current_object)

