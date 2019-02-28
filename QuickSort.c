#include <stdio.h>
#include <stdlib.h>

/*
QUICKSORT FUNCIONA ASSIM:
TENDO UM VETOR DESORDENADO
ESCOLHE-SE UM PIVO
DESSE PIVO PEGA-SE UM NUMERO MAIOR QUE ELE A ESQUERDA
DESSE PIVO PEGA-SE UM NUMERO MENOR QUE ELE A DIREITA
TROCA-SE ESSES DOIS NUMEROS
RECURSIVAMENTE FACA COM AS DUAS METADES (COMECO ATE O NUMERO PEGO A DIREITAA) E (NUMERO PEGO A ESQUERDA ATE O FIM)

*/

void quicksort(int vet[], int com, int fim)
{
	int i, j, pivo, aux;
	i = com;
	j = fim-1;
	pivo = vet[(com + fim) / 2]; //PONTO MEDIO
	while(i <= j) //ISSO GARANTIRA QUE OS DOIS PONTOS NAO SE CRUZEM
	{
		while(vet[i] < pivo && i < fim) //IR ATE ENCONTRAR O VALOR MAIOR QUE O PIVO A ESQUERDA
		{
			i++;
		}
		while(vet[j] > pivo && j > com) //IR ATE ENCONTRAR O VALOR MENOR QUE O PIVO A DIREITA
		{
			j--;
		}
		if(i <= j) //SE NAO TIVEREM SE CRUZADO, TROCAR
		{
			aux = vet[i];
			vet[i] = vet[j];
			vet[j] = aux;
			i++;
			j--;
		}
	}
	if(j > com)
		quicksort(vet, com, j+1);
	if(i < fim)
		quicksort(vet, i, fim);
}

void printVetor(int vetor[], int tam){
    
    for (int i=0; i < tam; i++){
        printf("%i ", vetor[i]);
    }
    printf("\n");
}


int main(){

    int vet[12];
    int tam = 12;

    for (int i=0;i<tam;i++){
        vet[i] = rand() % 100 + 1; //numeros aleatorios de 1 a 100
    }

    printf("Vetor Desordenado: ");
    printVetor(vet, tam);

    quicksort(vet,0,tam);

    printf("Vetor Ordenado:");
    printVetor(vet, tam);

    return 0;
}
