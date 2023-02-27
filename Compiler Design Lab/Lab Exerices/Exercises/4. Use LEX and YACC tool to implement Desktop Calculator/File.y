%{
	#include<stdio.h>
	extern int yylex(void);
	void yyerror(char *);
	int x=0;
	int val[26];
%}
%token INT ID
%%
mohnish:
mohnish expr '\n'                 	{x=$2; printf("%d\n",$2);}
|mohnish ID '=' expr '\n'             	{val[$2]=$4;}
|        
;    
expr:          
expr '+' T						{$$=$1+$3;}
|expr '-' T                  		{$$=$1-$3;}
|T                       			{$$=$1;}
|'+' T                  			{$$=x+$2;}
|'-' T                  			{$$=x-$2;}
;
T:
F                               		{$$=$1;}
|T '*' F						{$$=$1*$3;}
|T '/' F                  			{$$=$1/$3;}
|'*' F        					{$$=x*$2;}
|'/' F        					{$$=x/$2;}
;
F:
INT                             		{$$=$1;}
|ID                            		{$$=val[$1];}
| '(' expr ')'                  		{$$=$2;}
;
%%

void yyerror(char* s)
{
printf("%s",s);
}

int main()
{
yyparse();
return 0;
} 
