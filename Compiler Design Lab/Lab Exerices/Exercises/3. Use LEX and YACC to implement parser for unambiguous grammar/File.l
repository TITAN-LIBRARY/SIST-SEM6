%{
	#include<stdlib.h>
	#include"y.tab.h"
	void yyerror(char *s);
	extern int yylval;
%}
%%
[0-9]+ {yylval=atoi(yytext); return INT;}
[-+*/\n] {return *yytext;}
"("       {return *yytext;}
\)       {return *yytext;}
[\t];
.       {yyerror("Syntax Error");}
%%
int yywrap()
{
return 1;
}
