#include<iostream>
#include<stdlib.h>
#include <time.h>
#define TAM 1000

using namespace std;

void imprimeVetor(int array[], int i);
void criaVetCrescente(int array[], int tam);
void criaVetDecrescente(int array[], int tam);
void criaVetAleatorio(int array[], int tam);

int comp = 0, trocas = 0;

int main(){
	int lista[TAM];
	//criaVetCrescente(lista,TAM);
	//criaVetDecrescente(lista, TAM);
	criaVetAleatorio(lista, TAM);
	imprimeVetor(lista, TAM);
	int trocou = -1;
	while(trocou != 0){
		trocou = 0;
		for (int j = 0; j < TAM-1; j++){			
			if(lista[j] > lista[j+1]){
				int aux = lista[j];
				lista[j] = lista[j+1];
				lista[j+1]= aux;
				trocou = -1;
				trocas++;
			}
			comp++;
		}
	}
	imprimeVetor(lista, TAM);
	cout << "Comparacoes: "<< comp<< endl;
	cout << "Trocas :"<< trocas<< endl;
	
	
	return 0;
}

void imprimeVetor(int array[], int i){
	cout << "[";
	for (int a = 0; a < i; a++){
		if(a ==(i-1)){
			cout << array[a] << "]"<< endl;
		}else{
			cout << array[a] << ", ";
		}
	}
}

void criaVetCrescente(int array[], int tam){
	for (int i = 0; i < tam; i++){
		array[i]= i+1;
	}
}

void criaVetDecrescente(int array[], int tam){
	for (int i = 0; i < tam; i++){
		array[i] = tam - i;
	}
}

void criaVetAleatorio(int array[], int tam){
	srand (time(NULL));
	for (int i = 0; i < tam; i++){
		array[i]= rand() % tam;
	}
}

