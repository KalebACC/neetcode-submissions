class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Group anagrams by key value?
        #anagram grouping list [a1,a2,a3]
        #dict that contains the truthseet and its index in the grouping list
        
        lookup = dict()
        groupings = []

        #loop over strings
        for message in strs:
            
            #Save a dict of the letters
            letters = dict()
            for char in message:

                #build character list
                if char in letters:
                    letters[char] += 1
                else:
                    letters[char] = 1
                
            
            #if the dict matches one in the lookup
            key = frozenset(letters.items())
            if key in lookup.keys() :
                #add it to the grouping
                groupings[lookup[key]].append(message) 
            #if dict is not in lookup
            else:
                index = len(lookup)
                lookup[key] = index #add to lookup
                groupings.append([message]) #add to letters
        
        return groupings