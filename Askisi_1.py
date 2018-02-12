import random
#prin tin epenali4i 1000
metritis=0
metrgiron=0

for m in range(1000):
    #kata tin epanali4i 1000
    q=0
    metrgiron +=1

    lista=[]
    def fun():
        for i in range(1,81):
            lista.insert(i,i)
        return lista

    #dimiourgia pexton me 5 ari8mous alla xoris onoma
    pextes=[]
    copypextes=[]
    for i in range (100):
        lista=[]
        fun()
        fivenum=[]
        for j in range(5):
            pick=(random.choice(lista))
            lista.remove(pick)
            fivenum.insert(j,pick)
        pextes.insert(i,fivenum)
        copypextes.insert(i,str(fivenum))

    """
    o logos pou iparxi i dilosi str ine gt gia kapio logo antika8ista ke se aftin
    tin lista tous ari8mous pou kliro8ikan me to 0
    """

    #peristrofi "mpalas" (klirosi ari8mon)
    lista=[]
    fun()
    countlen=0
    for i in range(80):
        if (q==1):
            break
        lucknum=(random.choice(lista))
        lista.remove(lucknum)
        metritis +=1

        # elenxos tou lucknum an iparxi stis listes ton pexton
        for j in range(100):
            if (q==1):
                break
            countlen=len(pextes[j])
            checker=countlen
            for k in range(checker):
                if (q==1):
                    break
                take=pextes[j][k]
                # antikatastaassi ton ari8mon me to 0 opou entopistoun
                if (take==lucknum):
                    pextes[j].remove(take)
                    pextes[j].insert(k,0)

                    # elenxos gia nikiti
                    if (pextes[j][0]==0):
                        if (pextes[j][1]==0):
                            if (pextes[j][2]==0):
                                if (pextes[j][3]==0):
                                    if (pextes[j][4]==0):
                                        q=1
                                        nikitis=copypextes[j]
                                        print "o nikitis sto ", metrgiron ," pexnidi einai"
                                        print "o pextis ", j+1
                                        print "me ari8mous", copypextes[j]
                                        # den ektiponno tous kliroteous ari8mous se ka8e pexnidi giati perni arketi ora
                                        print ""
                                        print ""

mesosoros=metritis/1000
print metritis
print "o mesos oros ton ari8mon pou prepi na anaggel8oun wste na exoume BINGO einai: ", mesosoros
