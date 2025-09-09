%{
#include "y.tab.h"
#include <stdlib.h>
%}

[0-9]+      { yylval.ival = atoi(yytext); return NUMBER; }
[ \t]+      ;      /* skip spaces and tabs */
\n          { return 0; }   /* End of expression */
.           { return yytext[0]; }
%%
