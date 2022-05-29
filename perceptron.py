"""
The perceptron function updates weights every time the prediction and answers don't align. It then adjusts the weights recursively until there's no disagreement between them two.
The 5 expected arguments for the function are threshold(float), ajustment factor(float), weights(list), examples(3D list), and number of pass(integer).
The returned result is formmated in Python dictionary as required in output_template.txt (initial arguments values and inputs(list),prediction(boolean), answer(boolean), adjusted_weights(list) for every pass)

"""

def perceptron(threshold, ajustmentFactor,weights,examples,passNum):
    weightlength = len(weights)
    exampleslength = len(examples)
    result = {'init': {'weights': weights, 'threshold': threshold, 'adjustment': ajustmentFactor}} # initialize result 

    for i in range(passNum):
        result[i+1] = []    #initialize pass key
        for j in range(exampleslength):
            dic = {}                                      # initialize/ reset dictionary dic
            Sum = 0
            for num1,num2 in zip(weights,examples[j][1]): # Calculate each input array's sum
                Sum += num1*num2                         
                                                        
            prediction = False                            #prediction represents peceptron's predition 
            if (Sum <= threshold):                        #compare Sum with threshold
                prediction = False
            else:
                prediction = True

            if(examples[j][0] != prediction):             #if answer and prediction don't agree with each other, increase or decrease the weight accordinly
                new_weights = weights[:]                  #new_weights serves as a copy of the weights to prevent updating previous adjected_weights values
                if (examples[j][0]):                      #if the answer is true but the prediction is false, increase the weights by the amount of ajustmentFactor for every 1 input position
                    for k in range(weightlength):
                        if (examples[j][1][k]):
                            new_weights[k] += ajustmentFactor                  
                else:                                     #if the prediction is true but the answer is false, decrease the weights by the amount of ajustmentFactor for every 1 input position
                    for a in range(weightlength):
                        if (examples[j][1][a]):
                            new_weights[a] -= ajustmentFactor

            dic['inputs'] = examples[j][1]                #push the updated input, prediction, answer, adjested-weights to the dictionary dic
            dic['prediction'] = prediction
            dic['answer'] = examples[j][0]
            dic['adjusted_weights'] = new_weights
            
            result[i+1].append(dic)                       #append dic in the value array for the pass key
            weights = new_weights[:]                      
        
    return result    


