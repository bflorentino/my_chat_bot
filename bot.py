import re
import random

class Response:
    
    def __init__(self, 
                 possible_response :str, 
                 list_of_words:list, 
                 single_response = False, 
                 required_words = []
                 ) -> None:

        self.possible_response = possible_response
        self.list_of_words = list_of_words
        self.single_response = single_response
        self.required_words = required_words
    
    # Probability of being an specific response
    def message_probability(self, message) -> int:
        message_certainty = 0
        has_required_words = True

        for word in message:
            if word in self.list_of_words:
                message_certainty +=1

        percentage = float(message_certainty) / float (len(self.list_of_words))

        for word in self.required_words:
            if word not in message:
                has_required_words = False
                break
        if has_required_words or self.single_response:
            return int(percentage * 100)
        else:
            return 0


class Bot():

    def __init__(self, name: str = "Shiara") -> None:
        self.__highest_prob = {}
        self.responsesList:Response = []
        self.name = name

    def get_response(self, user_input:str) -> str:
        split_message = re.split(r'\s|[,:;.¿?!-_]\s*', user_input.lower())
        response = self.__check_all_messages(split_message)
        return response

    def __check_all_messages(self, message) -> str:

        for res in self.responsesList : 
            self.__highest_prob[res.possible_response] = res.message_probability(message)

        best_match = max(self.__highest_prob, key=self.__highest_prob.get)

        return self.__unknown() if self.__highest_prob[best_match] < 1 else best_match
    
    def __unknown(self) -> str:

       response = ['puedes decirlo de nuevo?', 
                   'No estoy seguro de lo quieres', 
                   'No etendí',
                   'No comprendo lo que me preguntas',
                   '¿Serías tan amable de repetir lo que quires de otra forma?'][random.randrange(5)]
                   
       return response