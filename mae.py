#!/usr/bin/env python

def mae(pred_list, true_list):
    if len(pred_list) != len(true_list):
        raise Exception('Error: elements amount not match!')
    return sum(map(lambda a,b: a-b,zip(pred_list, true_list))/len(true_list)
    
if __name__ == "__main__":
   pass
