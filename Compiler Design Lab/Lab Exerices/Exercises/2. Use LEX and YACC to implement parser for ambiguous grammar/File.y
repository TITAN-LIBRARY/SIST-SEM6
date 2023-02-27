%{
	#include<stdio.h>
	extern int yylex(void);
	void yyerror(char *);
%}
%token NUM
%% 
S:
S expr '\n'   {printf("%d\n",$2);}
|
;
expr:
expr '+' expr	{$$=$1+$3;}
|expr '-' expr	{$$=$1-$3;}
|expr '*' expr	{$$=$1*$3;}
|expr '/' expr	{$$=$1/$3;}
|NUM          	{$$=$1;}
| '(' expr ')' 	{$$=$2;}
;
%%
void yyerror(char *s)
{
printf("%s\n",s);
}

int main()
{
yyparse();
return 0;
} 
