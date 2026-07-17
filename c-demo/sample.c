#include<stdio.h>
#define MAX 100

int list[MAX];
int size = 0;


void insert(int val){
    if(size==MAX){
        printf("List is full");
        return;
    }
    list[size]=val;
    size++;
}

void delete(int pos){
    if(size==0){
        printf("List is Empty");
        return;
    }

    if(pos<0 || pos>=size){
        printf("Invalid Position");
        return;
    }

    for(int i=pos;i<size;i++){
        list[i]=list[i+1];
    }
    size--;
}

int get(int pos){
    if(pos<0 || pos>=size){
        printf("Invalid Position");
        return -1;
    }
    return list[pos];
}

void display(){
    if(size==0){
        printf("List is Empty");
        return;
    }

    for(int i=0;i<size;i++){
        printf("%d ",list[i]);
    }
    printf("\n");
}

int main(){

    int val;
    
    do{
        scanf("%d",&val);
        if(val!=-1)
            insert(val);
    }while(val!=-1);

    display();

    int pos;
    scanf("%d",&pos);
    delete(pos);
    display();
    printf("%d\n",get(pos));
    return 0;
}