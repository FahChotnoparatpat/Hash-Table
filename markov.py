from hashtable import Hashtable
from math import log

HASH_CELLS = 57
TOO_FULL = 0.5
GROWTH_RATIO = 2

class Markov:
    def __init__(self, k, text, use_hashtable):
        """
        Construct a new k-order markov model using the text 'text'.0
        """
        original_len = len(text)
        text = text + text[0:k + 1]     # Wrap around the text
        self.k = k
        self.char_set = set()
        self.is_hash = use_hashtable

        # Hash table approach
        if self.is_hash == True:
            self.k_table = Hashtable(HASH_CELLS, 0, TOO_FULL, GROWTH_RATIO)
            
            for i in range(original_len):
                substr = text[i:i + k]      # For K string
                substr1 = text[i:i + k + 1]     # For K+1 string
                self.char_set.add(text[i])
                
                if self.k_table[substr] == 0:
                    self.k_table[substr] = 1
                else:
                    self.k_table[substr] += 1
                
                if self.k_table[substr1] == 0:
                    self.k_table[substr1] = 1
                else:
                    self.k_table[substr1] +=1

        # Dictionary approach
        else:
            self.k_table = dict()

            for i in range(original_len):
                substr = text[i:i + k]     # For K string 
                substr1 = text[i:i + k + 1]     # For K+1 string
                self.char_set.add(text[i])

                if substr not in self.k_table:
                    self.k_table[substr] = 1
                else:
                    self.k_table[substr] +=1
                
                if substr1 not in self.k_table:
                    self.k_table[substr1] = 1
                else:
                    self.k_table[substr1] +=1
               

    def log_probability(self, s):
        """
        Get the log probability of string "s", given the statistics of
        character sequences modeled by this particular Markov model
        This probability is *not* normalized by the length of the string.
        """
        unique_char = len(self.char_set)
        text = s + s[0:self.k + 1]

        if self.is_hash == True:
            m_vals = [self.k_table[text[i:i + self.k + 1]] for i in range(len(s))]
            n_vals = [self.k_table[text[i:i + self.k]] for i in range(len(s))]
            return sum([log((m + 1) / (n + unique_char)) for (m, n) in zip(m_vals, n_vals)])
        else:
            m_vals = [self.k_table[text[i:i + self.k + 1]] if text[i:i + self.k + 1] in self.k_table else 0 for i in range(len(s))]
            n_vals = [self.k_table[text[i:i + self.k]] if text[i:i + self.k] in self.k_table else 0 for i in range(len(s))]
            return sum([log((m + 1) / (n + unique_char)) for (m, n) in zip(m_vals, n_vals)])

def identify_speaker(speech1, speech2, speech3, k, use_hashtable):
    """
    Given sample text from two speakers (1 and 2), and text from an
    unidentified speaker (3), return a tuple with the *normalized* log probabilities
    of each of the speakers uttering that text under a "order" order
    character-based Markov model, and a conclusion of which speaker
    uttered the unidentified text based on the two probabilities.
    """
    a = Markov(k, speech1, use_hashtable)
    b = Markov(k, speech2, use_hashtable)
    norm_prob1 = a.log_probability(speech3) / len(speech3)
    norm_prob2 = b.log_probability(speech3) / len(speech3)
    if norm_prob1 > norm_prob2:
        return norm_prob1, norm_prob2, "A"
    else:
        return norm_prob1, norm_prob2, "B"

