#include <bits/stdc++.h>

using namespace std;

int mintwo(int a, int b){
    //cout<<"h";
    if(a > b){
        return b;
    }
    return a;
}

int minthree(int a, int b, int c){
    int d = 0;
    int temp = a < d ? a : b < c ? b : c;
    return temp;
}

int main(){
    int n(0);
    cin>>n;
    int arr[n+1];
    arr[0] = 0;
    arr[1] = 0;
    arr[2] = 1;
    arr[3] = 1;
    //cout<<arr[n];
    for(int i = 4; i < n + 1; i++){
        //cout<<i;
        if(i%3 == 0 && i%2 == 0){
            arr[i] = minthree(arr[i/3] + 1, arr[i/2] + 1, arr[i-1] + 1);
        }
        else if(i%3 == 0 && i%2 != 0){
            //cout<<i;
            arr[i] = mintwo(arr[i/3] + 1, arr[i-1] + 1);
        }
        else if(i%2 == 0){
            //cout<<"sd";
            arr[i] = mintwo(arr[i/2] + 1, arr[i-1] + 1);
        }
        else{
            arr[i] = arr[i-1] + 1;
        }
    }
    cout<<arr[n]<<endl;
}