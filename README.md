# Markov Models with Hash Table
This is a modeling system project using Markov Models to capture the statistical relationships present in speeches. The model is used in analyzing actual text and assessing the likelihood of a specific word uttered by the speaker.  

Markov Class includes the following methods:
* Identify Speaker: Given sample text from two speakersand text from an unidentified speaker, conclusion of which speaker uttered the unidentified text is given based on the two probabilities.

* Log Probability: The log probability of a speech is calculated given the statistics of character sequences modeled by the Markov model


The project involves a hash tables module, which creates data structures that store associations between keys and values. The hash table is used to store probabilities associated with specific letters to help us form words likely to be spoken in a speech. 

Hashtable Class includes the following methods:

* Set: A hashtable is set up with a specified length and key-value pairs

* Get: Values are extracted from the hash table using linear probing, if the keys exist.

* Rehashing: Using linear probing, the size of hash table is expanded and key-value pairs are migrated into their proper locations in the newly-expanded hash table 

* Deletion: Each key-value pair is marked with a binary value to indicate if the pair has been deleted from the hash table.

