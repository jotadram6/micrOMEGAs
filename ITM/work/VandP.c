#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../CalcHEP_src/include/extern.h"
#include "../../CalcHEP_src/include/V_and_P.h"
#include "autoprot.h"
extern int  FError;
/*  Special model functions  */

int nModelParticles=19;
ModelPrtclsStr ModelPrtcls[19]=
{
  {"A","A", 22, "0","0",2,1,0}
, {"Z","Z", 23, "MZ","wZ",2,1,0}
, {"G","G", 21, "0","0",2,8,0}
, {"W+","W-", 24, "MW","wW",2,1,3}
, {"n1","N1", 12, "0","0",1,1,0}
, {"e1","E1", 11, "0","0",1,1,-3}
, {"n2","N2", 14, "0","0",1,1,0}
, {"e2","E2", 13, "Mm","0",1,1,-3}
, {"n3","N3", 16, "0","0",1,1,0}
, {"e3","E3", 15, "Mt","0",1,1,-3}
, {"u","U", 2, "Mup","0",1,3,2}
, {"d","D", 1, "Mdo","0",1,3,-1}
, {"c","C", 4, "Mc","0",1,3,2}
, {"s","S", 3, "Ms","0",1,3,-1}
, {"t","T", 6, "Mtop","wtop",1,3,2}
, {"b","B", 5, "Mb","0",1,3,-1}
, {"H","H", 37, "MH","wH",0,1,0}
, {"~T+","~T-", 37, "MTc","wTc",0,1,3}
, {"~T0","~T0", 36, "MT0","wT0",0,1,0}
};
int nModelVars=25;
int nModelFunc=15;
int LastVar=25;
char*varNames[40]={
 "EE","SW","s12","s23","s13","MZ","wZ","wW","Mm","Mt"
,"Mup","Mdo","Mc","Ms","Mtop","wtop","Mb","MH","wH","MTc"
,"wTc","MT0","wT0","La2","La3","Sqrt2","CW","c12","c23","c13"
,"Vud","Vus","Vub","Vcd","Vcs","Vcb","Vtd","Vts","Vtb","MW"
};
double varValues[40]={
   3.133300E-01,  4.740000E-01,  2.210000E-01,  4.000000E-02,  3.500000E-03,  9.118700E+01,  2.502000E+00,  2.094000E+00,  1.057000E-01,  1.777000E+00
,  3.000000E-03,  6.000000E-03,  8.290000E-01,  2.000000E-01,  1.700000E+02,  1.442000E+00,  3.010000E+00,  1.300000E+02,  1.461000E+00,  2.660000E+02
,  1.000000E+00,  1.000000E+02,  1.000000E+00,  3.000000E+00, -4.000000E-01};
int calcMainFunc(void)
{
   int i;
   static double * VV=NULL;
   static int iQ=-1;
   static int cErr=0;
   double *V=varValues;
   FError=0;
   if(VV&&!cErr)
   { for(i=0;i<nModelVars;i++) if(i!=iQ && VV[i]!=V[i]) break;
     if(i==nModelVars)     return 0;
   }
  cErr=1;
   V[25]=sqrt(2);
 LastVar=25;    if(!finite(V[25]) || FError) return 25;
   V[26]=sqrt(1-pow(V[1],2));
 LastVar=26;    if(!finite(V[26]) || FError) return 26;
   V[27]=sqrt(1-pow(V[2],2));
 LastVar=27;    if(!finite(V[27]) || FError) return 27;
   V[28]=sqrt(1-pow(V[3],2));
 LastVar=28;    if(!finite(V[28]) || FError) return 28;
   V[29]=sqrt(1-pow(V[4],2));
 LastVar=29;    if(!finite(V[29]) || FError) return 29;
   V[30]=V[27]*V[29];
 LastVar=30; 
   V[31]=V[2]*V[29];
 LastVar=31; 
   V[32]=V[4];
 LastVar=32; 
   V[33]=-V[27]*V[3]*V[4]-V[2]*V[28];
 LastVar=33; 
   V[34]=V[27]*V[28]-V[2]*V[3]*V[4];
 LastVar=34; 
   V[35]=V[3]*V[29];
 LastVar=35; 
   V[36]=V[2]*V[3]-V[27]*V[28]*V[4];
 LastVar=36; 
   V[37]=-V[2]*V[28]*V[4]-V[27]*V[3];
 LastVar=37; 
   V[38]=V[28]*V[29];
 LastVar=38; 
   V[39]=V[5]*V[26];
 LastVar=39; 
   if(VV==NULL) 
   {  VV=malloc(sizeof(double)*nModelVars);
      for(i=0;i<nModelVars;i++) if(strcmp(varNames[i],"Q")==0) iQ=i;
   }
   for(i=0;i<nModelVars;i++) VV[i]=V[i];
   cErr=0;
return 0;
}
