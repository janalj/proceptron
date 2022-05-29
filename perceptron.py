

# Test Date

# weights = [-0.5, 0, 0.5, 0, -0.5] 
# example = [[True,  [1,1,1,1,0]], 
#                        [False, [1,1,1,1,1]], 
#                        [False, [0,0,0,0,0]], 
#                      [False, [0,0,1,1,0]], 
#                        [False, [1,0,1,0,1]], 
#                        [False, [1,0,1,0,0]], 
#                        [False, [0,1,0,1,1]], 
#                        [False, [0,1,0,1,0]], 
#                       [False, [0,0,1,0,0]], 
#                        [False, [0,0,0,1,0]]]

# weights = [0.3, -0.6] 
# example =  [[True, [1,1]], 
#                      [False, [0,0]], 
#                      [True, [0,1]], 
#                      [True, [1,0]]] 




def perceptron(threshold, ajustmentFactor,weights,examples,passNum):
    weightlenth = len(weights)
    exampleslenth = len(examples)

    for i in range(passNum):
        print("\nPass ", i+1, "\n")
        for j in range(exampleslenth):  
            print("inputs: ",examples[j][1] )  # print each input array 
            Sum = 0
            for num1,num2 in zip(weights,examples[j][1]): # for each input array
                Sum += num1*num2                         #calculate their Sum
                                                        #compare Sum with threshold
            prediction = False                              #prediction represents peceptron's predition 
            if (Sum <= threshold):
                prediction = False
            else:
                prediction = True
            print("prediction: ", prediction, "  answer: ", examples[j][0])

            if(examples[j][0] != prediction):
                if (examples[j][0]):
                    for k in range(weightlenth):
                        if (examples[j][1][k]):
                            weights[k] += ajustmentFactor
                   
                else:
                    for a in range(weightlenth):
                        if (examples[j][1][a]):
                            weights[a] -= ajustmentFactor
            
            print("adjusted_weights: ", weights)




# perceptron(0.4, 0.09,weights,example,10)