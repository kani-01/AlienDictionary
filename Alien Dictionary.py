# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 01:02:40 2020

@author: Srini
"""

from collections import OrderedDict

class AlienDictionary():
    
    '''
    Step 1: Find all edges and put them in reverse_adj_list.
    Check that second word isn't a prefix of first word.
    If PREFIX OF FIRST LETTER   -> means the dictionary is invalid
    eg: er comes after ert -> er is prefix of ert but comes later in 
    the dictionary order which is invalid.
    '''
    def alienOrder(self, words):
    
        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c : [] for word in words for c in word}
        
        print(reverse_adj_list)
    
        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            print('FS',first_word, second_word)
            for c, d in zip(first_word, second_word):
                print('c, d',c,d)
                if c != d: 
                    reverse_adj_list[d].append(c)
                    print('when the letter changes -> detect sequence != d \n'
                          ,reverse_adj_list)
                    break
                else: # Check that second word isn't a prefix of first word.
                    if len(second_word) < len(first_word): 
                            return ""
        '''
        Step 2: Depth-first search
        Cycle detection Return True if there are no cycles.
        If this node was grey (False), a cycle was detected.
        If this node was True, a cycle was not detected.
        '''
        # Step 2: Depth-first search.
        seen = {} # False = grey, True = black.
        output = []
        def visit(node):  # Return True iff there are no cycles.
            print('*****************************************')
            print('visit::',node)
            if node in seen:
                return seen[node] # If this node was grey (False), a cycle was detected.
            seen[node] = False # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result: 
                    return False # Cycle was detected lower down.
            seen[node] = True # Mark node as black.
            output.append(node)
            return True
    
        myboollist = []
        for node in reverse_adj_list:
            myboollist.append(visit(node))
        print('myboollist',myboollist)
        if not all(myboollist):
            return ""
    
        return "".join(output)
            
    
    
I = AlienDictionary()
Result = I.alienOrder(["wrt","wrf","er","ett","rftt"]) #["z","x","z"]
print(Result)


# (["rw","wrt","wrf","er","ett","rk","rftt"]) # Cycle Detected

# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Tue Apr 21 01:02:40 2020
# 
# @author: Srini
# """
# 
# from collections import OrderedDict
# 
# class AlienDictionary():
#     
#     def alienOrder(self, words):
#     
#         # Step 0: Put all unique letters into the adj list.
#         reverse_adj_list = {c : [] for word in words for c in word}
#         
#         print(reverse_adj_list)
#     
#         # Step 1: Find all edges and put them in reverse_adj_list.
#         for first_word, second_word in zip(words, words[1:]):
#             print('FS',first_word, second_word)
#             for c, d in zip(first_word, second_word):
#                 print('c, d',c,d)
#                 if c != d: 
#                     reverse_adj_list[d].append(c)
#                     print('when the letter changes -> detect sequence != d \n'
#                           ,reverse_adj_list)
#                     break
#                 else: # Check that second word isn't a prefix of first word.
#                     if len(second_word) < len(first_word): 
#                         return ""
#     
#         # Step 2: Depth-first search.
#         seen = {} # False = grey, True = black.
#         output = []
#         def visit(node):  # Return True iff there are no cycles.
#             if node in seen:
#                 return seen[node] # If this node was grey (False), a cycle was detected.
#             seen[node] = False # Mark node as grey.
#             for next_node in reverse_adj_list[node]:
#                 result = visit(next_node)
#                 if not result: 
#                     return False # Cycle was detected lower down.
#             seen[node] = True # Mark node as black.
#             output.append(node)
#             return True
#     
#         myboollist = []
#         for node in reverse_adj_list:
#             myboollist.append(visit(node))
#         print('myboollist',myboollist)
#         if not all(visit(node) for node in reverse_adj_list):
#             return ""
#     
#         return "".join(output)
#             
#     
#     
# I = AlienDictionary()
# Result = I.alienOrder(["wrt","wrf","er","ett","rk","rftt"]) #["z","x","z"]
# print(Result)
# =============================================================================
