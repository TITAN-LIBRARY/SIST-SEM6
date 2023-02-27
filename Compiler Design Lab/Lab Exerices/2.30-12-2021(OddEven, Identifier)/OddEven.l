%option noyywrap
%{
	#include<stdio.h>
	int i;
%}

%%
[0-9]+  {i=atoi(yytext);
	 if(i%2==0)
	    printf("Even Number");
	 else
	    printf("Odd Number");
	 };

%%
int main()
{
	yylex();
	return 0;
}