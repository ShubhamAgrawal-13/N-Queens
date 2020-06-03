#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod 1000000007
#define vi vector<int>
#define vvi vector<vector<int>>
#define vii vector<pair<int,int>>
#define pb push_back

int count1=0;

void printboard(vvi &board,int n)
{
	count1++;
	cout<<"Solution "<<count1<<endl;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<board[i][j]<<" ";
		}
		cout<<endl;
	}
}

bool check_move(vvi &board,int n,int r,int col)
{
	//1:for row
	for(int i=col-1;i>=0;i--)
	{
		if(board[r][i]==1)
		{
			return false;
		}
	}

	//2:for left up diagonal
	for(int i=r-1,j=col-1;i>=0 && j>=0;i--,j--)
	{
		if(board[i][j]==1)
		{
			return false;
		}
	}

	//3:for left down diagonal
	for(int i=r+1,j=col-1;i<n && j>=0;i++,j--)
	{
		if(board[i][j]==1)
		{
			return false;
		}
	}

	return true;
}

void func(vvi &board,int n,int col)
{
	if(col==n)
	{
		printboard(board,n);
		return;
	}
	int r=0;
	while(r<n)
	{
		if(check_move(board,n,r,col))
		{
			board[r][col]=1;
			func(board,n,col+1);
			board[r][col]=0;
		}
		r++;
	}
}

int main(){
	int n;
	cin>>n;
	vvi board(n,vector<int>(n,0));
	func(board,n,0);
	return 0;
}