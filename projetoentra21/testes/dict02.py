#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[19]:


def verifica(base,empresa):
    ret='None'
    for a,b in base.items():
        if (a == empresa):
            ret = b                        
            
    return ret

        
base8 = {
'A' : 'Empresa1',
'B':'Empresa2',
'C' : 'Empresa3'
}

if empresa == 8: 
    novo_nome = verifica(base8,'Philips')
    print(novo_nome)
    
    






# In[ ]:




