diconary = {
"fruit":"mango",
"colour":"pink", 
"bird":"sparrow"    
}
try :
    diconary["animal"]
except(KeyError) :
    print("key aniaml is not defined")