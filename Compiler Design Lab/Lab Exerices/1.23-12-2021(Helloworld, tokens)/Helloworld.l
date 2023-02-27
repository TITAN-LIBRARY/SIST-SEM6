%option noyywrap
%{
	#include<stdio.h>
%}

%%
[\n] {
printf("Hello world\n");
}
%%
int main()
{
	yylex();
	return 0;
}