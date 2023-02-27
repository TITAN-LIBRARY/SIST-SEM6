%option noyywrap
%{
	#include<stdio.h>
	#include "y.tab.h"
	void yyerror(char *s);
	extern int yylval;
%}

%%
[0-9]+ {yylval=atoi(yytext); 
return NUM;}
[-+*/\n] {return *yytext;}
"("       {return *yytext;}
")"       {return *yytext;}
[\t];
.       {yyerror("Syntax Error");}
%%
intyywrap()
{
return 1;
}
