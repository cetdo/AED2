#include<iostream>
#include<stdlib.h>
#include <time.h>
#define TAM 1000

using namespace std;

void heapify(int array[], int i);
void constHeap(int array[], int n);
void heapSort(int array[], int n);
void imprimeVetor(int array[], int i);
void criaVetCrescente(int array[], int tam);
void criaVetDecrescente(int array[], int tam);
void criaVetAleatorio(int array[], int tam);

int tamHeap = 0, comp = 0, trocas = 0;

int main(){
	int lista[TAM];
	//criaVetCrescente(lista,TAM);
	//criaVetDecrescente(lista, TAM);
	criaVetAleatorio(lista, TAM);
	imprimeVetor(lista, TAM);
	cout << endl;
	heapSort(lista, TAM);
	imprimeVetor(lista,TAM);
	cout << "Comparacoes feitas: "<< comp << endl;
	cout << "Trocas feitas: "<< trocas << endl;
	return 0;
}

void heapify(int array[], int i){
	int l = 2*i + 1;
	int r = 2*i + 2;
	int m = i;
	int temp;
	comp++;
	if(l < tamHeap && array[l] > array[m]){
		m = l;
		
	}
	comp++;
	if(r < tamHeap && array[r] > array[m]){
		m = r;
	}
	if(m!= i){
		temp = array[i];
		array[i] = array[m];
		array[m] = temp;
		trocas ++;
		heapify(array,m);
	}
}

void constHeap(int array[], int n){
	tamHeap = n;
	for(int i = n/2 - 1; i>=0; i--){
		heapify(array,i);
	}
}

void heapSort(int array[], int n){
	int temp;
	constHeap(array, n);
	for (int i = n-1; i>= 0; i--){
		temp = array[0];
		array[0]= array[i];
		array[i] = temp;
		trocas ++;
		tamHeap --;
		heapify(array, 0);
	}
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
