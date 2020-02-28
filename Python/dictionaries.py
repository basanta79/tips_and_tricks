import json


class DictionariesTest:

    dict1 = dict(
            one='one',
            two=dict(
                one_='one_',
                two_='two_'
            ),
            three='trhee'
        )

    @classmethod
    def _test_has_key(cls):
        dict2 = dict(
            one='one',
            two='two',
            three='trhee'
        )
        print('two' in dict2.keys())
        print('four' in dict2.keys())

    @classmethod
    def _test_get_multimple_dimension(cls):
        print(cls.dict1.get('two').get('one_'))

    @classmethod
    def _serialize_dictionary(cls):
        print(str(cls.dict1))
        print(json.dumps(cls.dict1))
    
    @classmethod
    def _propagation(cls):
        print(json.dumps(dict1))
        dict1=dict(
            ...,
            
        )


DictionariesTest._test_has_key()
DictionariesTest._test_get_multimple_dimension()
DictionariesTest._serialize_dictionary()

test_none = None

att = test_none.ligth

print(att)
