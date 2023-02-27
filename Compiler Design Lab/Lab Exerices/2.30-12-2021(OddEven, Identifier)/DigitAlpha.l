%option noyywrap
%{
	#include<stdio.h>
%}

digit  [0-9]
letter  [a-zA-Z]

%%
{digit}+   {printf("%s is a Digit\n", yytext);}
{letter}+  {printf("%s is a Alphabet", yytext);} 
%%
int main()
{
	yylex();
	return 0;
}