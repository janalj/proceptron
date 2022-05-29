def perceptron(threshold, ajustmentFactor,weights,examples,passNum):
    weightlenth = len(weights)
    exampleslenth = len(examples)
    initialweights = weights
    result = {'init': {'weights': initialweights, 'threshold': threshold, 'adjustment': ajustmentFactor}}

    for i in range(passNum):
        result[i+1] = []
        for j in range(exampleslenth):
            dic = {} 

            dic['inputs'] = examples[j][1]
            Sum = 0
            for num1,num2 in zip(weights,examples[j][1]): # for each input array
                Sum += num1*num2                         #calculate their Sum
                                                        #compare Sum with threshold
            prediction = False                              #prediction represents peceptron's predition 
            if (Sum <= threshold):
                prediction = False
            else:
                prediction = True

            dic['prediction'] = prediction
            dic['answer'] = examples[j][0]

            if(examples[j][0] != prediction):
                new_weights = weights[:]
                if (examples[j][0]):
                    for k in range(weightlenth):
                        if (examples[j][1][k]):
                            new_weights[k] += ajustmentFactor                  
                else:
                    for a in range(weightlenth):
                        if (examples[j][1][a]):
                            new_weights[a] -= ajustmentFactor
                 
            dic['adjusted_weights'] = new_weights
            
            result[i+1].append(dic)
            weights = new_weights[:]
        

    return result    
