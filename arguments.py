def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
# Now we can use both *args ,**kwargs
# to pass arguments to this function :

myFun('These','are','Non-keyword',first="These",mid="are",last="keyword")

