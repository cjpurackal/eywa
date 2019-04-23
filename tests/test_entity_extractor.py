from eywa.nlu import EntityExtractor
import pytest


class TestEntityExtractor:

    def test_entity_extractor_basic(self):
        x = ['what is the weather in tokyo', 'what is the weather',
             'what is the weather like in kochi', 'will it be raining in koothapadi tomorrow?',
             'how hot is it in hawaii today?', 'will there be a thunderstorm tonight?']
        y = [{'intent': 'weather', 'place': 'tokyo', 'date': None}, {'intent': 'weather', 'place': 'here', 'date': None}, 
            {'intent': 'weather', 'place': 'kochi', 'date': None}, {'intent': 'weather', 'place': 'koothapadi', 'date': 'tomorrow'},
            {'intent': 'weather', 'place': 'hawaii', 'date': 'today'}, {'intent': 'weather', 'place': None, 'date': 'tonight'}]

        ex = EntityExtractor()
        ex.fit(x, y)

        x_test = 'what is the weather in london like'
        assert ex.predict(x_test) == {'intent': 'weather', 'place': 'london', 'date': None}


    def test_entity_extractor_serialization(self):
        x = ['what is the weather in tokyo', 'what is the weather', 'what is the weather like in kochi']
        y = [{'intent': 'weather', 'place': 'tokyo'}, {'intent': 'weather', 'place': 'here'}, {'intent': 'weather', 'place': 'kochi'}]

        ex1 = EntityExtractor()
        ex1.fit(x, y)

        config = ex1.serialize()
        ex2 = EntityExtractor.deserialize(config)

        test_inputs = ['what is the weather in london like']

        for test_input in test_inputs:
            ex1_out = ex1.predict(test_input)
            ex2_out = ex2.predict(test_input)
            ex2.predict(test_input, return_scores=True) # TODO
            assert ex1_out == ex2_out


if __name__ == '__main__':
    pytest.main([__file__])
