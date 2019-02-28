#include <stdio.h>
#include <stdlib.h>

/*
MERGESORT FUNCIONA ASSIM:
TENDO UM VETOR DESORDENADO
RECURSIVAMENTE PEGA-SE TODO VETOR
ATRAVES DAS PARTES MENORES ORGANIZA-SE OS VALORES


*/
void merge(int vetor[], int comeco, int meio, int fim) {
    int com1 = comeco, com2 = meio+1, comAux = 0, tam = fim-comeco+1;
    int *vetAux;
    vetAux = (int*)malloc(tam * sizeof(int));

    while(com1 <= meio && com2 <= fim){ //ISSO ACONTECERA ATE O COM1 e COM2 CHEGAREM AOS SEUS RESPECTIVOS FINAIS
        if(vetor[com1] < vetor[com2]) {
            vetAux[comAux] = vetor[com1];
            com1++;
        } else {
            vetAux[comAux] = vetor[com2];
            com2++;
        }
        comAux++;
    }

    while(com1 <= meio){  //CASO O NUMERO DOS DOIS VETORES FOR DESIGUAL, ELE COLOCARA OS VALORES NO VETOR, PRIMEIRA METADE
        vetAux[comAux] = vetor[com1];
        comAux++;
        com1++;
    }

    while(com2 <= fim) {  //CASO O NUMERO DOS DOIS VETORES FOR DESIGUAL, ELE COLOCARA OS VALORES NO VETOR, SEGUNDA METADE
        vetAux[comAux] = vetor[com2];
        comAux++;
        com2++;
    }

    for(comAux = comeco; comAux <= fim; comAux++){  //JOGA OS NUMEROS ORGANIZADOS NA PARTICAO QUE FOI ESCOLHIDA
        vetor[comAux] = vetAux[comAux-comeco];
    }

    free(vetAux); //LIBERAR MEMORIA
}

void printVetor(int vetor[], int tam){
    
    for (int i=0; i < tam; i++){
        printf("%i ", vetor[i]);
    }
    printf("\n");
}

void mergeSort(int vetor[], int comeco, int fim){
    if (comeco < fim) {
        int meio = (fim+comeco)/2;

        mergeSort(vetor, comeco, meio);
        mergeSort(vetor, meio+1, fim);
        merge(vetor, comeco, meio, fim);
    }
}

int main(){
    int vet[12];
    int tam = 12;

    for (int i=0;i<tam;i++){
        vet[i] = rand() % 100 + 1; //numeros aleatorios de 1 a 100
    }

    printf("Vetor Desordenado");
    printVetor(vet, tam);

    mergeSort(vet, 0, tam);

    printf("Vetor Ordenado: ");
    printVetor(vet, tam);

    return 0;
}
