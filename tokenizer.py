# identifiable tokens are numbers , identifiers , literal strings , keywords , new lines ,sympols 



class reserved_keywords:



    def __init__(self):

        self.keywords={"if":1,"for":1,"while":1,"None":1,"main":1,"def":1,"return":1}

    

    def is_exist(self,str):

        
        return self.keywords.get(str,0)



class token:

    def __init__(self,type,value,line_number):

        self.type=type 
        self.value=value
        self.line_number=line_number




class tokenizer:

    def __init__(self,source_code,output_method):

        self.source_code=source_code  

        self.start=0  #start of the next token 

        self.current_char=0   #next char that will be processed  

        self.line_number=0    #the line the token exist in 

        self.tokens=[]   #list with all tokens 

        self.reserved_keys=reserved_keywords()

        self.c=0 

        self.nextc=0


        self.output_method=output_method


    def possible_space(self):

            if self.c==" ":

                self.make_token("space",None)

                return 1
            

            return 0
    

    def possible_newline(self):

            if self.c=="\n":

                self.make_token("New line",None)
                self.line_number+=1

                return 1

            return 0
    
    def case1_float_point_number(self):


        # int.int
        self.c=self.next_char()

        # print("there"," ",self.c," ",self.current_char," ")

        if self.possible_integer(1):


            
            self.make_token("floating point number ",1)
        

        else:
            

            self.wrong_number()

            self.make_token("wrong number representation",1)



    def case2_float_point_number(self):
        
        # .int 
        if self.c=='.':

            self.c=self.next_char()

            if self.possible_integer(2):

                self.make_token("floating point number ",1)
            
            else:

                self.wrong_number()

                self.make_token("wrong floating point number ",1)
            
            return 1 
        return 0
    

    def case3_float_point_number(self):

        # int.
        if self.nextc==' ' or self.nextc=="None" or self.nextc=='\n':

            self.c=self.next_char()
            
            self.make_token("floating point number ",1)

            return 1

        return 0


    def possible_float_point_number(self):

            #float point numbers    int.int or .int or int.     three cases 


                        # .int                                  the int.int and int. case will be detected from the int token
            return  self.case2_float_point_number()   

                   
              

    def possible_integer(self,caller):

            # the caller might be the next_token function   caller=0
            # the caller might be the case 1 float point number int.int caller=1
            # the caller might be the case 2 float point number .int caller=2
            

            if (self.is_digit(self.c)):

                while (self.is_digit(self.c)):

                    self.c=self.next_char()
                    self.nextc=self.next_char()
                    

                    if self.nextc!="None":

                        self.current_char-=1
                    # print(self.c," ",self.nextc," ",self.current_char)

                

                if self.current_char<len(self.source_code) and self.c!='.':
                    self.current_char-=1
            

                if self.c ==' ' or self.c=="None" or self.c=="\n":
                    

                    if caller==1 or caller==2:
                        return 1

                    else:    
                        self.make_token("integer",1)

                        return 1
                
                # the caller is 2 .int and what after . is not int so it wrong case 2 float point number 
                elif caller==2:
                    
                    return 0


                elif self.c=='.':


                    
                    if self.case3_float_point_number() and caller==0:

                        return 1
                    

                    
                    # if the caller=1  the int.int case float number so this will be wrong number 
                    # else the caller=0 the next_token function this might be a int.int case float point number   

                    if caller==1:

                       

                        return 0
                    

                    elif caller==0:
                        # print("here")

                        self.case1_float_point_number()

                else:
                    # case 1 float point number function 
                    if caller==1:

                        return 0

                    self.wrong_number()

                    self.make_token("wrong number representation",1)

                
                return 1 

                    

                    
            
            return 0
    

    def possible_string(self):

            #string 


            if self.c=='"' or self.c =="'":
                start=self.c
                self.c=self.next_char()

                while self.c!=start:

                    self.c=self.next_char()
                

                self.start+=1

                self.make_token("string",1)

                return 1 
            

            return 0


    

    def possible_identifier(self):

            #identifier 

            if self.potential_indetifier_char(self.c):
            

                
                while self.c !=' ' and self.c!="None" and self.c!='\n' and (self.potential_indetifier_char(self.c) or self.is_digit(self.c)):



                        self.c=self.next_char()
                    



                if self.c!="None":

                    self.current_char-=1            

                
                result_token=self.source_code[self.start:self.current_char]


                if self.reserved_keys.is_exist(result_token):

                    self.make_token("reserved_keyword",1)
                

                else:

                    self.make_token("identifier",1)
                

                return 1
            
            return 0
    

    def possible_one_char_symbol(self):

        
            #one char sympols 
            if self.c=="=" and self.nextc!="=":

                self.make_token("equal",None)

                return 1 
            
            

            elif self.c==">" and self.nextc!="=":

                self.make_token("greater than",None)

                return 1 
            
            elif self.c=="<" and self.nextc!="=":

                self.make_token("less than",None)

                return 1
            
            elif self.c=="(":
                
                self.make_token("left Parentheses",None)
            
                return 1 
            
            elif self.c==")":

                self.make_token("right Parenthese",None)

                return 1

            elif self.c=="{":

                
                self.make_token("left brace",None)
                
                return 1 

            elif self.c=="}":

                self.make_token("right brace",None)

                return 1

            elif self.c=="+":

                self.make_token("plus sign",None)

                return 1

            elif self.c=="-":

                self.make_token("minus sign",None)

                return 1

            elif self.c=="/":

                self.make_token("slash",None)

                return 1

            elif self.c==":":

                self.make_token("double colon",None)

                return 1

            else:

                return 0

    def possible_2_chars_symbol(self):

            #2 chars sympols 

            if self.c==">" and self.nextc=="=":

                self.make_token("greater or equal",None)
                self.c=self.next_char()
                return 1
            

            elif self.c=="<" and self.nextc=="=":

                self.make_token("less or equal",None)
                self.c=self.next_char()

                return 1 

            elif self.c=="!" and self.nextc=="=":

                self.make_token("not equal",None)
                self.c=self.next_char()

                return 1
            
            elif self.c=="=" and self.nextc=="=":

                self.make_token("is equal",None)
                self.c=self.next_char()

                return 1 


            else:

                return 0



    def next_token(self):

        self.check_for_eof()


        if self.c!=None:

            self.c=self.next_char()   
            self.nextc=self.next_char()
            self.current_char-=1
            # print(self.c," ",self.current_char)

        

            if self.possible_integer(0):

                return 
            

            elif self.possible_float_point_number():

                return 
            
            elif self.possible_identifier():

                return 
            
            elif self.possible_string():

                return 
            
            elif self.possible_one_char_symbol():

                return 
            
            elif self.possible_2_chars_symbol():

                return 
            

            elif self.possible_newline():

                return 
            
            elif self.possible_space():

                return 
            

            else:

                
                self.wrong_number()

                self.make_token("us supported token",1)





            

    def emit_all_tokens(self):

        

        while True :
            
            
            if len(self.tokens):

                tok=self.tokens[-1]

                if tok.type=="End of file":

                    break
            
            
            self.next_token()


    def next_char(self):


        if self.current_char==len(self.source_code):

            return "None"
        

        self.current_char+=1
        return self.source_code[self.current_char-1]
        
    

    def is_digit(self,c):


        return c>=("0") and c <=("9")
    


    def make_token(self,type,value):

        if value is not None:

            if value==1:

                value=self.source_code[self.start:self.current_char]

            

            token_=token(type,value,self.line_number)
        

        else:

            token_=token(type,None,self.line_number)

        self.start=self.current_char

        self.tokens.append(token_)

    


    


    def potential_indetifier_char(self,c):

        if (c>=("a") and c<=("z")) or (c>=("A")and c<=("Z")) or (c==("_")):
            return 1


        return 0
    


    def check_for_eof(self):

        if self.current_char==len(self.source_code):

            self.make_token("End of file",None)
            self.c=None

            
    

    def wrong_number(self):

        while self.c!=' ' and self.c!='\n' and self.c!="None":

            self.c=self.next_char()
        

        if self.c!="None":

            self.current_char-=1
        

            
    def wrong_identifier_representation(self):

        while self.c!=' ' and self.c!='\n' and self.c!="None":

            self.c=self.next_char()
        


        if self.c!="None":

            self.current_char-=1

        self.make_token("wrong identifier",1)


    
    def generate_all_tokens(self):

        self.emit_all_tokens()
        self.output_method.print(self.tokens)


class output_method:

    def __init__(self,method):

        self.method=method
    

    def print(self,list):

        self.method.out(list)


class terminal_output:

    def __init__(self):

        ...
    

    def out(self,list):

        for tok in list:

            if tok.value is not None:

                print(f"the token type is {tok.type} and its value is {tok.value} and exist in line number {tok.line_number+1}")
    
            else:

                print(f"the token type is {tok.type} and exist in line number {tok.line_number+1}")




class file_output:

    def __init__(self,file_name):

        self.file_name=file_name

    

    def out(self,list):

        

        with open(self.file_name,"w") as f:

            for tok in list:

                if tok.value is not None:

                    f.write(f"the token type is {tok.type} and its value is {tok.value} and exist in line number {tok.line_number+1}\n")

                else:

                    f.write(f"the token type is {tok.type} and exist in line number {tok.line_number+1}\n")










if __name__=='__main__':

    source_code=input("the name of the file ")

    with open(source_code,"r") as file:

        source_code=(file.read()) 





    output_method_=input("""choase the output method of the tokens
                        
                        1-terminal

                        2-file
                        
                         """)
    
    if output_method_=="1":

        
        term=terminal_output()

        output_method_obj=output_method(term)

        tok=tokenizer(source_code,output_method_obj)

        tok.generate_all_tokens()


    
    elif output_method_=="2":

        
        out_file=input("enter the name of the output file ")

        file_output_obj=file_output(out_file)

        output_method_obj=output_method(file_output_obj)

        tok=tokenizer(source_code,output_method_obj)

        tok.generate_all_tokens()
    

    else:

        print("unsupported option ")



