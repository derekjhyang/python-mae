#!/usr/bin/env python

def mae(pred_list, true_list):
    if len(pred_list) != len(true_list):
        raise Exception('Error: number of elements not match!')
    return sum(map(lambda t:float(t[0]-t[1]),zip(pred_list, true_list)))/len(true_list)
    
if __name__ == "__main__":
    a = [1,2,3]
    b = [4,5,6]
    print mae(a,b)
