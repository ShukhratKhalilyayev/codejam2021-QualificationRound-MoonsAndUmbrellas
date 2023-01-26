answers = []
variation = False

testCases = input()
testCases = int(testCases)

for i in range(testCases):
    x,y,sequence = input().split()
    x = int(x)
    y = int(y)
    
    if(len(sequence)==1):
        #print("Case #" + str(i+1) + ": 0")
        answers.append(0)
        continue
    
    sequence = list(sequence)
    
    for w in range(len(sequence)):
        if(sequence[w]!='?'):
            variation = True
            break
    
    if(variation == False):
        #print("Case #" + str(i+1) + ": 0")
        answers.append(0)
        continue
        
    
    for j in range(len(sequence)):
        
        if(j == 0 and sequence[j] == '?' and sequence[j+1] != '?'):
            st = sequence[j+1]
            sequence[j] = st
            continue
        
        if(j == 0 and sequence[j] == '?' and sequence[j+1] == '?'):
            for k in range(len(sequence)):
                if(sequence[k] != '?'):
                    z = sequence[k]
                    break
            for l in range(len(sequence)):
                if(sequence[l] == '?'):
                    sequence[l] = z
                    continue
                if(sequence[l] != '?'):
                    j = l
                    break
        
        if(j == len(sequence)-1 and sequence[j]=='?'):
            sequence[j] = sequence[j-1]
        
        if(j == 0 and sequence[j] == 'J'):
            continue
        
        if(j != len(sequence)-1 and sequence[j-1]=='J' and sequence[j+1]=='C' and sequence[j]=='?'):
            sequence[j] = 'C'
            continue
        
        if(j != len(sequence)-1 and sequence[j-1]=='C' and sequence[j+1]=='J' and sequence[j]=='?'):
            sequence[j] = 'C'
            continue
        
        if(j != len(sequence)-1 and sequence[j-1]=='C' and sequence[j+1]=='C' and sequence[j]=='?'):
            sequence[j] = 'C'
            continue
        
        if(j != len(sequence)-1 and sequence[j-1]=='J' and sequence[j+1]=='J' and sequence[j]=='?'):
            sequence[j] = 'J'
            continue
        
        if(j != len(sequence)-1 and sequence[j-1]=='C' and sequence[j+1]=='?' and sequence[j]=='?'):
            sequence[j] = 'C'
            continue
        
        if(j != len(sequence)-1 and sequence[j-1]=='J' and sequence[j+1]=='?' and sequence[j]=='?'):
            sequence[j] = 'J'
            continue
    
    cjCount = 0
    jcCount = 0
    
    for w in range(len(sequence)-1):
        
        if(sequence[w]=='C' and sequence[w+1]=='J'):
            cjCount+=1
            continue
        if(sequence[w]=='J' and sequence[w+1]=='C'):
            jcCount+=1
            continue
        
    answerX = x * cjCount
    answerY = y * jcCount
    
    answers.append(answerX + answerY)
        
    #newSequence = ''.join(sequence)
    #print(newSequence)
    
for c in range(len(answers)):
    print("Case #" + str(c+1) + ": " + str(answers[c]))
    
    




