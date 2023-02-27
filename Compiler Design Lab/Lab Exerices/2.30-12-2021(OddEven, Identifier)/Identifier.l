%option noyywrap
%{
	#include<stdio.h>
%}

digit  [0-9]
letter  [a-zA-Z]

%%
{digit}+   printf("%s is a Digit", yytext);
{letter}+  printf("%s is a Alphabet", yytext);
{letter}({letter}|{digit})* printf("%s is a Identifier", yytext); 
%%
int main()
{
	yylex();
	return 0;
}