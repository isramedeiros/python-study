def procure_pela_chave(): #def function
    pilha = main_box.crie_uma_pilha_para_busca()
    #       ↑        ↑
    #    object   method
    while pilha is not None:
        caixa = pilha.pegue_caixa()

        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print("achei a chave!")