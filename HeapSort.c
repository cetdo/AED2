#include <stdio.h>
#include <stdlib.h>

/*
O HEAPSORT FUNCIONA ASSIM:
TENDO UM VETOR DESORDENADO
CRIA-SE UM VETOR AUXILIAR DESSE VETOR(HEAP OU ARVORE)
USA-SE UMA FUNCAO CHAMADO HEAPFY NO AUXILIAR, QUE FAR� OS NUMEROS MAIORES "FLUTUAREM" PARA CIMA(ESQUERDA)
DEPOIS PEGA ESSE NUMERO MAIOR E COLOCA NO FINAL
RETIRA-SE ESSE NUMERO DO HEAP
REPETE-SE O PROCESSO COM O RESTO
*/

void heapfy(int vet[], int tam, int i){
    int troca;
    int maior = i;
    int esq = i*2 + 1;
    int dir = i*2 + 2;

    if(esq < tam && vet[esq] > vet[maior]){ /*SE O FILHO ESQUERDO ESTIVER DENTRO DO TAMANHO E ELE FOR MAIOR QUE O PAI*/
        maior = esq;
    }

    if(dir < tam && vet[dir] > vet[maior]){ /*SE O FILHO DIREITO ESTIVER DENTRO DO TAMANHO E ELE FOR MAIOR QUE O MAIOR*/
        maior = dir;
    }

    if(maior != i){ /*SE MAIOR != i, SIGFNIFICA QUE NAO EXISTE MAIOR QUE ELE */
        troca = vet[i];
        vet[i] = vet[maior];
        vet[maior] = troca;

        heapfy(vet,tam,maior);
    }
}

void heapSort(int vet[],int tam){

    int temp;

    //ORGANIZAR EM HEAPS
    for(int i = (tam/2) - 1 ; i >= 0 ; i-- ){
        heapfy(vet,tam,i);

    }

    //SORT
    for(int i = tam-1 ; i >= 0 ; i--){
        temp = vet[0];
        vet[0] = vet[i]; //COLOCAR O MAIOR NUMERO NO FINAL
        vet[i] = temp;

        heapfy(vet,i,0); //FAZER O HEAPFY NOS OUTROS NUMEROS
    }

}

void printVetor(int vetor[], int tam){
    
    for (int i=0; i < tam; i++){
        printf("%i ", vetor[i]);
    }
    printf("\n");
}

int main()
{

    int vet[12];
    int i;
    int tam = 12;

    for (i=0;i<tam;i++){
        vet[i] = rand() % 100 + 1; //numeros aleatorios de 1 a 100
    }
    
    printf("Vetor Desordenado: ");
    printVetor(vet, tam);

    heapSort(vet, tam);

    printf("Vetor Ordenado: ");
    printVetor(vet, tam);
    

    return 0;
}
