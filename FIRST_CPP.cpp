#include<stdio.h>
#include<string.h>
void FindFirst(char,int,int);
void ComputeFirst(char);
int main(){
	char Productions[10][10];
	char NonTerm,LeftSide,firstchar,FirstSet;
	int i,j,n,count=0;
	printf("Enter the number of productions: ");
	scanf("%d",&n);
	printf("\n Enter the context free grammar: (in the form { S->E-A } )\n");
	for(i=0;i<n;i++)
	{
		printf("Production rule %d: ",i);
		scanf("%s",Productions[i]);
		if(Productions[i][1]!='-' || Productions[i][2]!='>' || (Productions[i][3]=='\0'))
			{
				printf("Invalid Production");
				return 0;
			}	
	}
	printf("Enter the Non Terminal to find the first of: ");
	scanf(" %c",&NonTerm);
	for(i=0;i<n;i++){
		LeftSide=Productions[i][0];
		if(LeftSide==NonTerm)
		count=1;
	}
	if (count==1)
	{
		//Breaking down the productions
		for(i=0;i<n;i++)
		{
			firstchar=Productions[i][3];
			if (firstchar>=97 && firstchar<=122)
			{
			FirstSet=firstchar;
			printf("First = %c",FirstSet);
			}
			else if(firstchar>=65 && firstchar<=90)
			ComputeFirst(firstchar);
		}
	}
	else
	printf("The First of %c is \n %c->$",NonTerm,NonTerm);
	
	return 0;
}
void ComputeFirst(char Productions)
{
	printf("Called this function");
}
